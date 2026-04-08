import { ILlmProvider, ChatMessage } from '../../infra/providers/IProvider.js';
import { AgentLoop } from './AgentLoop.js';
import { ToolRegistry } from './ToolRegistry.js';
import { SkillLoader, Skill } from '../skills/SkillLoader.js';
import { SkillRouter } from '../skills/SkillRouter.js';
import { MemoryManager } from '../memory/MemoryManager.js';
import { CreateFileTool, ReadFileTool, ListDirTool } from './tools/FileTools.js';
import { ProviderFactory } from '../../infra/providers/ProviderFactory.js';
import { PdfParser } from '../../shared/PdfParser.js';
import { LessTokens } from '../utils/LessTokens.js';
import fs from 'fs';

export interface ProcessResult {
    content: string;
    metadata: {
        involves_voice: boolean;
        [key: string]: any;
    };
}

export class AgentController {
    private toolRegistry: ToolRegistry;
    private skillLoader: SkillLoader;
    private memoryManager: MemoryManager;

    constructor(private provider: ILlmProvider) {
        this.toolRegistry = new ToolRegistry();
        this.memoryManager = new MemoryManager();
        this.skillLoader = new SkillLoader();

        // Register default tools
        this.toolRegistry.register(new CreateFileTool());
        this.toolRegistry.register(new ReadFileTool());
        this.toolRegistry.register(new ListDirTool());
    }

    async process(userId: string, text: string, options?: { 
        attachments?: { type: 'pdf' | 'md' | 'voice', path: string }[],
        involves_voice?: boolean,
        skill?: string,
        conversationId?: string
    }): Promise<ProcessResult> {
        // 1. Get or create conversation
        const providerName = ProviderFactory.getProviderName();
        const conversationId = options?.conversationId || await this.memoryManager.getOrCreateConversation(userId, providerName);

        // 2. Handle attachments
        let enrichedText = text;
        let finalInvolvesVoice = options?.involves_voice || false;

        if (options?.attachments) {
            for (const att of options.attachments) {
                try {
                    if (att.type === 'pdf') {
                        console.log(`[AgentController] Parsing PDF: ${att.path}`);
                        const pdfText = await PdfParser.parse(att.path);
                        enrichedText += `\n\n[Content of attached PDF (${att.path})]:\n${pdfText}`;
                    } else if (att.type === 'md') {
                        console.log(`[AgentController] Reading Markdown: ${att.path}`);
                        let mdText = fs.readFileSync(att.path, 'utf-8');
                        // Apply LessTokens pruning for large files
                        mdText = LessTokens.prune(mdText);
                        enrichedText += `\n\n[Content of attached MD (${att.path})]:\n${mdText}`;
                    }
                } catch (e: any) {
                    enrichedText += `\n(Error processing attachment ${att.path}: ${e.message})`;
                }
            }
        }

        // 3. Check for voice keywords in text
        if (text.toLowerCase().includes('responda em áudio') || text.toLowerCase().includes('fale comigo')) {
            finalInvolvesVoice = true;
        }

        // 4. Load context and apply LessTokens compression
        let history = await this.memoryManager.getContext(conversationId);
        history = LessTokens.compactHistory(history);
        
        // 5. Load skills and Detect Tags
        const allSkills = SkillLoader.loadAll();
        const activeSkillNames = new Set<string>();
        
        // Add skill from options (manual selection)
        if (options?.skill) activeSkillNames.add(options.skill);
        
        // Detect tags [skill:name] in text
        const skillTagRegex = /\[skill:(.*?)\]/g;
        let match;
        while ((match = skillTagRegex.exec(enrichedText)) !== null) {
            activeSkillNames.add(match[1].trim());
        }

        // If no explicit skills, try automatic routing
        if (activeSkillNames.size === 0) {
            const skillRouter = new SkillRouter(this.provider);
            const routedSkill = await skillRouter.route(enrichedText, allSkills);
            if (routedSkill) activeSkillNames.add(routedSkill);
        }

        let systemPrompt = `You are PeixotoClaw, a professional and powerful local AI agent.
Your responses must be:
1. Highly structured using Markdown (titles, bold text, lists).
2. Clean and organized.
3. ABSOLUTELY in the same language as the user's message (e.g., if user speaks Portuguese, you MUST respond in Portuguese).`;

        for (const sName of activeSkillNames) {
            const skill = allSkills.find(s => s.metadata.name === sName);
            if (skill) {
                console.log(`[AgentController] Loading skill: ${sName}`);
                systemPrompt += `\n\n[ACTIVE SPECIALIZED SKILL: ${skill.metadata.name}]\n${skill.content}\n[END OF SPECIALIZED SKILL]`;
            }
        }

        // Final reinforcement of language and structure (Recency Bias handling)
        systemPrompt += `\n\nREMEMBER:
- Language: ALWAYS match the user's language.
- Structure: Use professional Markdown formatting.`;

        // 6. Smart Routing Logic
        const isHighTierTask = activeSkillNames.has('architecture-guardian') || 
                               activeSkillNames.has('architecture-blueprint-generator') || 
                               activeSkillNames.has('feature-builder') ||
                               activeSkillNames.has('coder') ||
                               enrichedText.toLowerCase().includes('[model:pro]');

        const forceLowTier = enrichedText.toLowerCase().includes('[model:free]') || 
                             activeSkillNames.has('documentation-scribe') ||
                             activeSkillNames.has('escriba');

        if (forceLowTier) {
            this.provider.setModel('gemini-2.0-flash');
            console.log(`[AgentController] Smart Routing: Selected FREE/FAST tier.`);
        } else if (isHighTierTask) {
            this.provider.setModel('gemini-2.0-pro-exp-02-05');
            console.log(`[AgentController] Smart Routing: Selected PRO/HIGH tier.`);
        } else {
            // Default to flash for casual chat
            this.provider.setModel('gemini-2.0-flash');
        }

        // 7. Run Agent Loop
        const agentLoop = new AgentLoop(this.provider, this.toolRegistry);
        const userMessage: ChatMessage = { role: 'user', content: enrichedText };
        
        const loopMessages = [...history, userMessage];

        const response = await agentLoop.run(loopMessages, systemPrompt);

        // 7. Persist messages
        const metadata = { involves_voice: finalInvolvesVoice };
        await this.memoryManager.saveMessage(conversationId, 'user', text, metadata);
        await this.memoryManager.saveMessage(conversationId, 'assistant', response, metadata);

        return {
            content: response,
            metadata
        };
    }

    public async listConversations(userId: string): Promise<any[]> {
        return this.memoryManager.listConversations(userId);
    }

    public async getConversationHistory(conversationId: string): Promise<any[]> {
        return this.memoryManager.getFullHistory(conversationId);
    }

    public async createConversation(userId: string): Promise<string> {
        const providerName = ProviderFactory.getProviderName();
        return this.memoryManager.createNewConversation(userId, providerName);
    }

    public async deleteConversation(conversationId: string): Promise<void> {
        return this.memoryManager.deleteConversation(conversationId);
    }
}
