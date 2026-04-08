import { SQLiteDatabase } from './Database.js';

export interface Conversation {
    id: string;
    user_id: string;
    provider: string;
    created_at?: string;
}

export class ConversationRepository {
    private db = SQLiteDatabase.getInstance();

    public save(conversation: Conversation): void {
        const stmt = this.db.prepare('INSERT OR REPLACE INTO conversations (id, user_id, provider) VALUES (?, ?, ?)');
        stmt.run(conversation.id, conversation.user_id, conversation.provider);
    }

    public findById(id: string): Conversation | undefined {
        const stmt = this.db.prepare('SELECT * FROM conversations WHERE id = ?');
        return stmt.get(id) as Conversation | undefined;
    }

    public findByUserId(userId: string): Conversation | undefined {
        const stmt = this.db.prepare('SELECT * FROM conversations WHERE user_id = ? ORDER BY created_at DESC LIMIT 1');
        return stmt.get(userId) as Conversation | undefined;
    }

    public listAllByUserId(userId: string): Conversation[] {
        const stmt = this.db.prepare('SELECT * FROM conversations WHERE user_id = ? ORDER BY created_at DESC');
        return stmt.all(userId) as Conversation[];
    }

    public delete(id: string): void {
        const stmt = this.db.prepare('DELETE FROM conversations WHERE id = ?');
        stmt.run(id);
    }
}
