import TelegramBot from 'node-telegram-bot-api';
import dotenv from 'dotenv';
import fetch from 'node-fetch';

dotenv.config();

console.log('Bot starting...');
console.log(`Service URL: ${process.env.BOT_SERVICE_URL}`);

const bot = new TelegramBot(process.env.TELEGRAM_BOT_TOKEN, { polling: true });

console.log('Bot connected and listening for messages...');
const BOT_SERVICE_URL = process.env.BOT_SERVICE_URL || 'http://localhost:8000';

bot.on('message', async (msg) => {
    console.log('Message received:', msg.text);
    const chatId = msg.chat.id;
    
    try {
        // Send message to the Bot Service
        const response = await fetch(`${BOT_SERVICE_URL}/process-message`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                telegram_id: chatId.toString(),
                message: msg.text
            })
        });

        const data = await response.json();

        // Only respond if the message was processed as an expense
        if (data.status === 'success') {
            bot.sendMessage(chatId, data.message);
        }
    } catch (error) {
        console.error('Error:', error);
        // No error message is sent to the user to keep it simple
    }
});
