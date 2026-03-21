import Database from 'better-sqlite3';
import path from 'path';
import fs from 'fs';

export class SQLiteDatabase {
    private static instance: Database.Database;

    public static getInstance(): Database.Database {
        if (!SQLiteDatabase.instance) {
            const dbDir = path.resolve(process.cwd(), 'data');
            if (!fs.existsSync(dbDir)) {
                fs.mkdirSync(dbDir, { recursive: true });
            }
            const dbPath = path.join(dbDir, 'db.sqlite');
            SQLiteDatabase.instance = new Database(dbPath);
            SQLiteDatabase.instance.pragma('journal_mode = WAL');
            SQLiteDatabase.initSchema();
        }
        return SQLiteDatabase.instance;
    }

    private static initSchema() {
        const db = SQLiteDatabase.instance;
        db.exec(`
            CREATE TABLE IF NOT EXISTS conversations (
                id TEXT PRIMARY KEY,
                user_id TEXT NOT NULL,
                provider TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                conversation_id TEXT NOT NULL,
                role TEXT NOT NULL,
                content TEXT NOT NULL,
                metadata TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (conversation_id) REFERENCES conversations(id)
            );
        `);

        // Migration: Add metadata column if it doesn't exist
        const tableInfo = db.prepare('PRAGMA table_info(messages)').all() as any[];
        const hasMetadata = tableInfo.some(col => col.name === 'metadata');
        if (!hasMetadata) {
            console.log('[Database] Migrating: Adding metadata column to messages table');
            db.exec('ALTER TABLE messages ADD COLUMN metadata TEXT');
        }
    }
}
