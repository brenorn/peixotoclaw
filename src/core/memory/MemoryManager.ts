import { ConversationRepository, Conversation } from '../../infra/db/ConversationRepository.js';
import { MessageRepository, Message } from '../../infra/db/MessageRepository.js';
import { ChatMessage } from '../../infra/providers/IProvider.js';

export class MemoryManager {
    private conversationRepo = new ConversationRepository();
    private messageRepo = new MessageRepository();
    private memoryWindow: number;

    constructor() {
        this.memoryWindow = parseInt(process.env.MEMORY_WINDOW_SIZE || '10');
    }

    public async getOrCreateConversation(userId: string, provider: string): Promise<string> {
        let conversation = this.conversationRepo.findByUserId(userId);
        if (!conversation) {
            return this.createNewConversation(userId, provider);
        }
        return conversation.id;
    }

    public async createNewConversation(userId: string, provider: string): Promise<string> {
        const id = Math.random().toString(36).substring(2, 11);
        const conversation = { id, user_id: userId, provider };
        this.conversationRepo.save(conversation);
        return id;
    }

    public async listConversations(userId: string): Promise<Conversation[]> {
        return this.conversationRepo.listAllByUserId(userId);
    }

    public async saveMessage(conversationId: string, role: string, content: string, metadata?: any): Promise<void> {
        this.messageRepo.save({ 
            conversation_id: conversationId, 
            role, 
            content,
            metadata: metadata ? JSON.stringify(metadata) : undefined
        });
    }

    public async getContext(conversationId: string): Promise<ChatMessage[]> {
        const messages = this.messageRepo.getRecentMessages(conversationId, this.memoryWindow);
        const history = messages.map(m => ({
            role: m.role as any,
            content: m.content
        }));

        // Inject a hidden instruction into the very beginning of history to remind the model of the language
        if (history.length > 0) {
            history.unshift({
                role: 'user',
                content: "[REPETIÇÃO DE REGRA]: Responda SEMPRE em Português e mantenha a estrutura profissional."
            });
            history.splice(1, 0, {
                role: 'assistant',
                content: "Entendido, falarei sempre em Português."
            });
        }

        return history;
    }

    public async getFullHistory(conversationId: string): Promise<Message[]> {
        return this.messageRepo.findByConversationId(conversationId, 100);
    }

    public async deleteConversation(conversationId: string): Promise<void> {
        this.messageRepo.deleteAllByConversationId(conversationId);
        this.conversationRepo.delete(conversationId);
    }
}
