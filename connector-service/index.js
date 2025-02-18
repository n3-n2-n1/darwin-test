import TelegramBot from 'node-telegram-bot-api';
import dotenv from 'dotenv';
import fetch from 'node-fetch';

dotenv.config();

console.log('Bot iniciando...');
console.log(`URL del servicio: ${process.env.BOT_SERVICE_URL}`);


const bot = new TelegramBot(process.env.TELEGRAM_BOT_TOKEN, { polling: true });

console.log('Bot conectado y escuchando mensajes...');
const BOT_SERVICE_URL = process.env.BOT_SERVICE_URL || 'http://localhost:8000';

bot.on('message', async (msg) => {
    console.log('Mensaje recibido:', msg.text);
    const chatId = msg.chat.id;
    
    try {
        // Enviar mensaje al Bot Service
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

        // Solo responder si el mensaje fue procesado como un gasto
        if (data.status === 'success') {
            bot.sendMessage(chatId, data.message);
        }
    } catch (error) {
        console.error('Error:', error);
        // No enviamos mensaje de error al usuario para mantenerlo simple
    }
});
