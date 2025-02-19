# 🤖 Telegram Expense Tracking Bot - Bot Service 

📱 Important URLs  
Bot Render Service: https://darwin-test-oti1.onrender.com  

A simple Telegram bot that helps users track their expenses using AI categorization.

## 🎯 Features  
Track expenses directly through Telegram  
Automatic expense categorization using OpenAI  
Data persistence with Supabase  
Simple input format: just send "Pizza 25" to log an expense  

## 🛠 Tech Stack  
Python + FastAPI  
Supabase (PostgreSQL)  
Deployment on Render  

## 📋 Local Development Requirements  
Python 3.9+  
Supabase account  
OpenAI API Key  

## 🚀 Setup  
Clone the repository  
Create a `.env` file using `.env.example` as a template  
Install dependencies: cd bot-service pip install -r requirements.txt

## 🔑 Environment Variables  
SUPABASE_URL=your_supabase_url 
SUPABASE_KEY=your_supabase_key 
OPENAI_API_KEY=your_openai_api_key

## 💻 Local Development 
cd bot-service uvicorn main:app --reload


## 🌎 Deployment
Start Command:  cd bot-service && uvicorn main:app --host 0.0.0.0 --port $PORT
    Install requirements: pip install -r bot-service/requirements.txt
    Build Command: cd bot-service && uvicorn main:app --host 0.0.0.0 --port $PORT
    Set environment variables on Render  


## ⚠️ Notes  
OpenAI API requires a paid account  
Supabase free tier is suitable for testing  
Consider using Render's paid tier for production use  
