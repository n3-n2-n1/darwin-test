# 🤖 Bot de Gastos para Telegram

Buenas!

## 🎯 ¿Qué hace?

- Registra tus gastos directamente desde Telegram
- Categoriza automáticamente usando IA (gracias OpenAI!)
- Te guarda todo en una base de datos (Supabase)
- Es tan simple como mandarle "Pizza 2500" y ya te lo registra

## 🛠 Tecnologías

- **Bot Service**: Python + FastAPI (porque Flask ya fue)
- **Connector Service**: Node.js (para el webhook de Telegram)
- **Base de Datos**: Supabase (PostgreSQL pero sin tener que mantener nada)
- **Deploy**: Render (porque Heroku ahora es caro y Railway tiene límite de horas)

## 📋 Requisitos para levantar este repositorio (local)

- Node.js 18 o superior
- Python 3.9 o superior
- Cuenta en Supabase (gratis)
- API Key de OpenAI
- Bot Token de Telegram (gratis, gracias [@BotFather](https://t.me/botfather))

## 🚀 Setup

1. Cloná el repo
2. Creá un `.env` en cada servicio usando los `.env.example` como base
3. Instalá las dependencias:

```bash
# Bot Service (Python)
cd bot-service
pip install -r requirements.txt

# Connector Service (Node)
cd ../connector-service
npm install
```

## 🔑 Variables de Entorno

Necesitás configurar:

```bash
# Bot Service
SUPABASE_URL=tu_url_de_supabase
SUPABASE_KEY=tu_key_de_supabase
OPENAI_API_KEY=tu_api_key_de_openai

# Connector Service
TELEGRAM_BOT_TOKEN=token_de_tu_bot
BOT_SERVICE_URL=http://localhost:8000 # En local
```

## 💻 Desarrollo Local

```bash
# Bot Service
cd bot-service
uvicorn main:app --reload

# Connector Service
cd connector-service
npm run dev
```

## 🌎 Deploy

El proyecto está preparado para deployar en Render. Solo tenés que:

1. Crear un nuevo Web Service en Render
2. Conectar con tu repo de GitHub
3. Configurar las variables de entorno
4. Render se encarga del resto 🙌

### URLs importantes para el deploy:

- Webhook de Telegram: `https://tu-app.onrender.com/webhook`
- Endpoint del Bot Service: `https://tu-bot-service.onrender.com`

## 📱 Probalo!

1. Buscá el bot en Telegram: [link_a_tu_bot]
2. Mandále cualquier gasto tipo "Café con medialunas 1200"
3. El bot te va a responder con la categoría y  lo guarda



## ⚠️ Notas

- Ojo que OpenAI es pago
- La versión free de Supabase va como piña para empezar
- En Render podés usar el free tier, pero te conviene el hobby si querés que no se duerma

