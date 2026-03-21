import express from 'express';
import cors from 'cors';
import multer from 'multer';
import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';
import { AgentController } from './core/agent/AgentController.js';
import { ProviderFactory } from './infra/providers/ProviderFactory.js';
import { SkillLoader } from './core/skills/SkillLoader.js';
import axios from 'axios';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Debug logging to file
const logFile = path.join(process.cwd(), 'server_debug.log');
const log = (msg: string) => {
    const output = `[${new Date().toISOString()}] ${msg}\n`;
    console.log(msg);
    fs.appendFileSync(logFile, output);
};

const app = express();
const port = process.env.PORT || 3001;

app.use(cors());
app.use(express.json());

// Setup multer for file uploads
const upload = multer({ dest: 'tmp/uploads/' });

// Initialize AgentController
const provider = ProviderFactory.create();
const controller = new AgentController(provider);

// Endpoints

// Root route for guidance
app.get('/', (req, res) => {
    res.send(`
        <h1>PeixotoClaw API Bridge 🦞</h1>
        <p>The API is running correctly.</p>
        <p>To access the <b>Neural Dashboard</b>, please open the URL provided by Vite (usually <a href="http://localhost:5173">http://localhost:5173</a>).</p>
        <p>Current API Endpoints:</p>
        <ul>
            <li>POST /api/chat</li>
            <li>GET /api/skills</li>
            <li>POST /api/skills/install</li>
            <li>GET /api/conversations?userId=...</li>
            <li>GET /api/conversations/:id/messages</li>
            <li>POST /api/conversations/new</li>
        </ul>
    `);
});

// 1. Chat
app.post('/api/chat', (req, res, next) => {
    const contentType = req.headers['content-type'] || '';
    if (contentType.includes('multipart/form-data')) {
        upload.array('files')(req, res, next);
    } else {
        next();
    }
}, async (req, res) => {
    log(`[API] Received chat request. Type: ${req.headers['content-type']}`);
    log(`[API] Body: ${JSON.stringify(req.body)}`);
    
    try {
        const { userId, text, conversationId } = req.body;
        if (!text) {
            log('[API] Error: Missing text');
            return res.status(400).json({ error: 'text is required' });
        }

        const files = (req.files as Express.Multer.File[]) || [];
        const attachments = files.map(f => ({
            type: (f.mimetype === 'application/pdf' ? 'pdf' : 'md') as 'pdf' | 'md' | 'voice',
            path: f.path
        }));

        log(`[API] Process: ${userId} -> "${text.substring(0, 50)}..." (${attachments.length} files)`);
        const result = await controller.process(userId || 'web-user', text, { 
            attachments,
            skill: req.body.skill,
            conversationId: conversationId // Pass if provided
        } as any);
        
        log(`[API] Success`);
        res.json(result);
    } catch (error: any) {
        log(`[API] CRITICAL ERROR: ${error.message}`);
        log(`[API] Stack: ${error.stack}`);
        res.status(500).json({ error: error.message, stack: error.stack });
    }
});

// 1.1 List Conversations
app.get('/api/conversations', async (req, res) => {
    try {
        const { userId } = req.query;
        if (!userId) return res.status(400).json({ error: 'userId is required' });
        const list = await controller.listConversations(userId as string);
        res.json(list);
    } catch (error: any) {
        res.status(500).json({ error: error.message });
    }
});

// 1.2 Get Conversation History
app.get('/api/conversations/:id/messages', async (req, res) => {
    try {
        const history = await controller.getConversationHistory(req.params.id);
        res.json(history);
    } catch (error: any) {
        res.status(500).json({ error: error.message });
    }
});

// 1.3 Create New Conversation
app.post('/api/conversations/new', async (req, res) => {
    try {
        const { userId } = req.body;
        if (!userId) return res.status(400).json({ error: 'userId is required' });
        const id = await controller.createConversation(userId);
        res.json({ id });
    } catch (error: any) {
        res.status(500).json({ error: error.message });
    }
});

// 2. List Skills
app.get('/api/skills', (req, res) => {
    try {
        const skills = SkillLoader.loadAll();
        res.json(skills.map(s => ({
            name: s.metadata.name,
            description: s.metadata.description,
            path: s.path
        })));
    } catch (error: any) {
        res.status(500).json({ error: error.message });
    }
});

// 3. Install Skill via Link
app.post('/api/skills/install', async (req, res) => {
    log(`[API] Install request for skill: ${req.body.name}`);
    try {
        const { url, name } = req.body;
        if (!url || !name) return res.status(400).json({ error: 'URL and Name are required' });

        // 1. Resolve URL (Handle GitHub folder links)
        let resolvedUrl = url;
        if (url.includes('github.com') && url.includes('/tree/')) {
            // Transform folder link to raw SKILL.md link
            resolvedUrl = url.replace('github.com', 'raw.githubusercontent.com')
                             .replace('/tree/', '/')
                             + '/SKILL.md';
            log(`[API] Transformed GitHub tree URL to: ${resolvedUrl}`);
        } else if (url.includes('github.com') && url.includes('/blob/')) {
             // Transform blob link to raw link
            resolvedUrl = url.replace('github.com', 'raw.githubusercontent.com')
                             .replace('/blob/', '/');
            log(`[API] Transformed GitHub blob URL to: ${resolvedUrl}`);
        }

        // 2. Download to staging
        const stagingDir = path.resolve(process.cwd(), 'tmp/staging', name);
        if (!fs.existsSync(stagingDir)) fs.mkdirSync(stagingDir, { recursive: true });
        
        log(`[API] Downloading skill: ${resolvedUrl}`);
        const response = await axios.get(resolvedUrl);
        const content = response.data;
        
        // Basic validation: must look like a skill (have frontmatter)
        if (typeof content !== 'string' || !content.startsWith('---')) {
            throw new Error('The URL does not point to a valid SKILL.md file (frontmatter missing). If it is a folder, ensure it contains a SKILL.md.');
        }

        const stagingPath = path.join(stagingDir, 'SKILL.md');
        fs.writeFileSync(stagingPath, content);

        // 2. Automated Audit
        log(`[API] Running safety audit for: ${name}`);
        const auditResult = await controller.process('security-audit', `Audit this skill source code:\n\n${content}`, { 
            skill: 'skill-auditor' 
        } as any);

        const auditReport = auditResult.content;
        log(`[API] Audit completed.`);

        // 3. Security Gate
        const isDangerous = auditReport.includes('Global Risk Level: CRITICAL') || 
                          auditReport.includes('Global Risk Level: HIGH');

        if (isDangerous) {
            log(`[API] INSTALL REJECTED: High risk detected.`);
            // Clean up staging
            fs.unlinkSync(stagingPath);
            return res.status(403).json({ 
                error: 'Security Audit Failed: High risk detected.',
                report: auditReport 
            });
        }

        // 4. Finalize installation
        const finalDir = path.resolve(process.cwd(), '.agents/skills', name);
        if (!fs.existsSync(finalDir)) fs.mkdirSync(finalDir, { recursive: true });
        fs.writeFileSync(path.join(finalDir, 'SKILL.md'), content);
        
        // Clean up staging
        fs.unlinkSync(stagingPath);
        
        log(`[API] Install Success: ${name}`);
        res.json({ 
            message: `Skill ${name} installed and audited successfully.`,
            report: auditReport
        });
    } catch (error: any) {
        log(`[API] Install Error: ${error.message}`);
        res.status(500).json({ error: error.message });
    }
});

app.listen(port, () => {
    console.log(`[Server] PeixotoClaw API Bridge running at http://localhost:${port}`);
});
