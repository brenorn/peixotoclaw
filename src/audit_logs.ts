import { MessageRepository } from './infra/db/MessageRepository.js';
import { SQLiteDatabase } from './infra/db/Database.js';

async function checkLogs() {
    try {
        const db = SQLiteDatabase.getInstance();
        const messages = db.prepare('SELECT role, content FROM messages ORDER BY created_at DESC LIMIT 10').all();
        console.log('--- RECENT BOT ACTIVITY ---');
        messages.reverse().forEach((msg: any) => {
            console.log(`[${msg.role.toUpperCase()}]: ${msg.content.substring(0, 100)}${msg.content.length > 100 ? '...' : ''}`);
        });
        console.log('---------------------------');
    } catch (e) {
        console.error('Error reading logs:', e);
    }
}

checkLogs();
