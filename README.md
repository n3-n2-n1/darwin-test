# 🤖 Telegram Expense Tracking Bot

A simple Telegram bot that helps users track their expenses using AI categorization.

## 🎯 Features

- Track expenses directly through Telegram
- Automatic expense categorization using OpenAI
- Data persistence with Supabase
- Simple input format: just send "Pizza 25" to log an expense

## 🛠 Tech Stack

- **Bot Service**: Python + FastAPI
- **Connector Service**: Node.js
- **Database**: Supabase (PostgreSQL)
- **Deployment**: Render

## 📋 Local Development Requirements

- Node.js 18+
- Python 3.9+
- Supabase account
- OpenAI API Key
- Telegram Bot Token (from [@BotFather](https://t.me/botfather))

## 🚀 Setup

1. Clone the repository
2. Create `.env` files in both services using `.env.example` templates
3. Install dependencies:

```bash
# Bot Service (Python)
cd bot-service
pip install -r requirements.txt

# Connector Service (Node)
cd ../connector-service
npm install
```

## 🔑 Environment Variables

```bash
# Bot Service
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
OPENAI_API_KEY=your_openai_api_key

# Connector Service
TELEGRAM_BOT_TOKEN=your_bot_token
BOT_SERVICE_URL=http://localhost:8000 # For local development
```

## 💻 Local Development

```bash
# Bot Service
cd bot-service
uvicorn main:app --reload

# Connector Service
cd connector-service
npm run dev
```

## 🌎 Deployment

This is a monorepo project with two services that need to be deployed separately on Render:

### Bot Service (Python)
1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Configure build settings:
   - Build Command: `pip install -r bot-service/requirements.txt`
   - Start Command: `cd bot-service && uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Root Directory: `/`

### Connector Service (Node.js)
1. Create another Web Service on Render
2. Connect the same GitHub repository
3. Configure build settings:
   - Build Command: `cd connector-service && npm install`
   - Start Command: `cd connector-service && npm start`
   - Root Directory: `/`

Don't forget to set the environment variables in both services on Render.

### Important URLs
- Bot Service: https://darwin-test-oti1.onrender.com
- Telegram Bot: [@newdartest8398_bot](https://web.telegram.org/k/#@newdartest8398_bot)

## 📱 Try it out!

1. Open [@newdartest8398_bot](https://web.telegram.org/k/#@newdartest8398_bot) in Telegram
2. Send a message like "Coffee 5"
3. The bot will categorize and save your expense

## ⚠️ Notes

- OpenAI API requires a paid account
- Supabase free tier is suitable for testing
- Consider using Render's paid tier for production use
