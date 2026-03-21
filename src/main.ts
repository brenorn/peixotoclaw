import dotenv from 'dotenv';
import { TelegramInputHandler } from './interfaces/telegram/TelegramInputHandler.js';

dotenv.config();

function main() {
    const token = process.env.TELEGRAM_BOT_TOKEN;
    if (!token) {
        console.error('TELEGRAM_BOT_TOKEN is required in .env file');
        process.exit(1);
    }

    const bot = new TelegramInputHandler(token);
    bot.start();
}

main();
