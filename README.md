# 🤖 Telegram Expense Tracking Bot - Connector Service

📱 Important URLs
Live Bot Service: https://darwin-test-oti1.onrender.com
Live Connector Service: https://conn-service.onrender.com
Telegram Bot: @newdartest8398_bot

Frontend service handling Telegram interactions and message forwarding.

## 🎯 Features

- Telegram message processing
- Simple input format ("Item Price")
- Forwarding requests to Bot Service

## 🛠 Tech Stack

- Node.js 18+
- Telegram Bot API

## 📋 Requirements

- Node.js 18+
- Telegram Bot Token from [@BotFather](https://t.me/botfather)

## 🚀 Setup

1. Clone the repository
2. Create `.env` file using the template:

## 🔑 Environment Variables 
TELEGRAM_BOT_TOKEN=your_bot_token
BOT_SERVICE_URL=http://localhost:8000 # or production URL


## Install dependencies:

pnpm install

## 💻 Local Development
npm run dev
## 🌎 Deployment (Render)
Configure build settings:

    Build Command: cd connector-service && pnpm install
    Start Command: cd connector-service && pnpm start
    Set environment variables in Render dashboard


## 🚨 Try it!
-Open @newdartest8398_bot
--Send "Coffee 5" or similar message
---Bot will respond with categorized expense

## ⚠️ Notes
Ensure Bot Service is running and accessible
Monitor rate limits on Telegram API
Use webhook setup for production deployments

