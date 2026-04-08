import { SQLiteDatabase } from './Database.js';

export interface Message {
    id?: number;
    conversation_id: string;
    role: string;
    content: string;
    metadata?: string; // JSON string for flags like { involves_voice: true }
    created_at?: string;
}

export class MessageRepository {
    private db = SQLiteDatabase.getInstance();

    public save(message: Message): void {
        const stmt = this.db.prepare('INSERT INTO messages (conversation_id, role, content, metadata) VALUES (?, ?, ?, ?)');
        stmt.run(message.conversation_id, message.role, message.content, message.metadata || null);
    }

    public findByConversationId(conversationId: string, limit: number = 20): Message[] {
        const stmt = this.db.prepare('SELECT * FROM messages WHERE conversation_id = ? ORDER BY created_at ASC LIMIT ?');
        return stmt.all(conversationId, limit) as Message[];
    }

    public getRecentMessages(conversationId: string, limit: number): Message[] {
        const stmt = this.db.prepare(`
            SELECT * FROM (
                SELECT * FROM messages 
                WHERE conversation_id = ? 
                ORDER BY created_at DESC 
                LIMIT ?
            ) ORDER BY created_at ASC
        `);
        return stmt.all(conversationId, limit) as Message[];
    }

    public deleteAllByConversationId(conversationId: string): void {
        const stmt = this.db.prepare('DELETE FROM messages WHERE conversation_id = ?');
        stmt.run(conversationId);
    }
}
