import { Bot, Context, InputFile } from 'grammy';
import { AgentController } from '../../core/agent/AgentController.js';
import { ProviderFactory } from '../../infra/providers/ProviderFactory.js';
import { WhisperSTT } from '../../infra/stt/WhisperSTT.js';
import { EdgeTTS } from '../../infra/tts/EdgeTTS.js';
import path from 'path';
import fs from 'fs';
import https from 'https';

export class TelegramInputHandler {
    private bot: Bot;
    private allowedUserIds: number[];
    private controller: AgentController;
    private stt: WhisperSTT;
    private tts: EdgeTTS;

    constructor(token: string) {
        this.bot = new Bot(token);
        const rawAllowed = process.env.TELEGRAM_ALLOWED_USER_IDS || '[]';
        try {
            const parsed = JSON.parse(rawAllowed);
            this.allowedUserIds = Array.isArray(parsed) ? parsed : [parsed];
        } catch (e) {
            this.allowedUserIds = rawAllowed.split(',').map(id => parseInt(id.trim())).filter(id => !isNaN(id));
        }
        
        const provider = ProviderFactory.create();
        this.controller = new AgentController(provider);
        this.stt = new WhisperSTT();
        this.tts = new EdgeTTS();

        this.setupMiddlewares();
        this.setupCommands();
    }

    private setupMiddlewares() {
        this.bot.use(async (ctx, next) => {
            const userId = ctx.from?.id;
            if (!userId || !this.allowedUserIds.includes(userId)) {
                console.log(`[Telegram] unauthorized access attempt from: ${userId}`);
                return;
            }
            await next();
        });
    }

    private setupCommands() {
        // Text messages
        this.bot.on('message:text', async (ctx) => {
            const userId = ctx.from.id.toString();
            const text = ctx.message.text;

            await ctx.replyWithChatAction('typing');

            try {
                const result = await this.controller.process(userId, text);
                await this.handleResponse(ctx, result.content, result.metadata.involves_voice);
            } catch (error: any) {
                console.error('[Telegram] Error processing message:', error);
                await ctx.reply('⚠️ Sorry, an error occurred while processing your request.');
            }
        });

        // Voice and Audio
        this.bot.on(['message:voice', 'message:audio'], async (ctx) => {
            const userId = ctx.from.id.toString();
            const audio = ctx.message.voice || ctx.message.audio;
            if (!audio) return;

            await ctx.replyWithChatAction('record_voice');
            
            const tmpDir = path.resolve(process.cwd(), 'tmp');
            if (!fs.existsSync(tmpDir)) fs.mkdirSync(tmpDir, { recursive: true });
            const filePath = path.join(tmpDir, `audio_${Date.now()}.ogg`);

            try {
                const file = await ctx.getFile();
                const fileUrl = `https://api.telegram.org/file/bot${this.bot.token}/${file.file_path}`;
                await this.downloadFile(fileUrl, filePath);

                console.log(`[Telegram] Transcribing audio: ${filePath}`);
                const transcription = await this.stt.transcribe(filePath);
                
                if (!transcription || transcription.trim() === '') {
                    await ctx.reply('⚠️ Audio seems empty or was not understood.');
                    return;
                }

                console.log(`[Telegram] Transcription: ${transcription}`);
                const result = await this.controller.process(userId, transcription, { involves_voice: true });
                await this.handleResponse(ctx, result.content, true);

            } catch (error: any) {
                console.error('[Telegram] Voice Error:', error);
                await ctx.reply('⚠️ Failed to process audio. Ensure Whisper is installed.');
            } finally {
                if (fs.existsSync(filePath)) fs.unlinkSync(filePath);
            }
        });

        // Documents (PDF / MD)
        this.bot.on('message:document', async (ctx) => {
            const doc = ctx.message.document;
            const userId = ctx.from.id.toString();
            const text = ctx.message.caption || 'Analyze this document';

            const supportedTypes = ['application/pdf', 'text/markdown', 'text/x-markdown'];
            const isSupported = supportedTypes.includes(doc.mime_type || '') || doc.file_name?.endsWith('.md');

            if (isSupported) {
                await ctx.replyWithChatAction('typing');
                
                const tmpDir = path.resolve(process.cwd(), 'tmp');
                if (!fs.existsSync(tmpDir)) fs.mkdirSync(tmpDir, { recursive: true });
                const filePath = path.join(tmpDir, doc.file_name || `doc_${Date.now()}`);

                try {
                    const file = await ctx.getFile();
                    const fileUrl = `https://api.telegram.org/file/bot${this.bot.token}/${file.file_path}`;
                    await this.downloadFile(fileUrl, filePath);

                    const type = (doc.mime_type === 'application/pdf') ? 'pdf' : 'md';
                    const result = await this.controller.process(userId, text, { 
                        attachments: [{ type: type as any, path: filePath }] 
                    });
                    
                    await this.handleResponse(ctx, result.content, result.metadata.involves_voice);

                } catch (error: any) {
                    console.error('[Telegram] Document Error:', error);
                    await ctx.reply('⚠️ Failed to process document.');
                } finally {
                    if (fs.existsSync(filePath)) fs.unlinkSync(filePath);
                }
            } else {
                await ctx.reply('⚠️ Supported types: PDF, Markdown (.md).');
            }
        });
    }

    private async handleResponse(ctx: Context, text: string, useVoice: boolean) {
        if (useVoice) {
            try {
                await ctx.replyWithChatAction('record_voice');
                const voicePath = await this.tts.synthesize(text);
                await ctx.replyWithVoice(new InputFile(voicePath));
                if (fs.existsSync(voicePath)) fs.unlinkSync(voicePath);
            } catch (e) {
                console.error('[Telegram] TTS Fallback to text:', e);
                await this.sendLongMessage(ctx, text);
            }
        } else {
            await this.sendLongMessage(ctx, text);
        }
    }

    private downloadFile(url: string, dest: string): Promise<void> {
        return new Promise((resolve, reject) => {
            const file = fs.createWriteStream(dest);
            https.get(url, (response) => {
                response.pipe(file);
                file.on('finish', () => {
                    file.close();
                    resolve();
                });
            }).on('error', (err) => {
                fs.unlink(dest, () => reject(err));
            });
        });
    }

    private async sendLongMessage(ctx: Context, text: string) {
        const CHUNK_SIZE = 4000;
        if (text.length <= CHUNK_SIZE) {
            try {
                await ctx.reply(text, { parse_mode: 'Markdown' });
            } catch (e) {
                await ctx.reply(text);
            }
            return;
        }

        for (let i = 0; i < text.length; i += CHUNK_SIZE) {
            const chunk = text.substring(i, i + CHUNK_SIZE);
            await ctx.reply(chunk).catch(console.error);
        }
    }

    public start() {
        console.log('[Telegram] Bot started...');
        this.bot.start();
    }
}
