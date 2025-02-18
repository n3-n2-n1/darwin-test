from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from supabase import create_client

load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "healthy"}

# Configuración de Supabase
supabase = create_client(
    os.getenv('SUPABASE_URL'),
    os.getenv('SUPABASE_KEY')
)

# Configuración de LangChain
llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", openai_api_key=os.getenv('OPENAI_API_KEY'))
categorize_prompt = PromptTemplate(
    input_variables=["description"],
    template="Categoriza este gasto en una de las siguientes categorías: Housing, Transportation, Food, Utilities, Insurance, Medical/Healthcare, Savings, Debt, Education, Entertainment, Other. Solo responde con la categoría, nada más. Descripción: {description}"
)
categorize_chain = LLMChain(llm=llm, prompt=categorize_prompt)

class ExpenseMessage(BaseModel):
    telegram_id: str
    message: str

def is_user_authorized(telegram_id: str) -> Optional[int]:
    # Primero busca si el usuario existe
    response = supabase.table('users').select('id').eq('telegram_id', telegram_id).execute()
    if response.data:
        return response.data[0]['id']
    
    # Si no existe, lo registra automáticamente
    response = supabase.table('users').insert({"telegram_id": telegram_id}).execute()
    return response.data[0]['id'] if response.data else None

def parse_expense(message: str):
    # Busca un número en el mensaje
    words = message.split()
    amount = None
    description = []
    
    for word in words:
        # Intenta convertir la palabra en número
        try:
            # Elimina caracteres no numéricos excepto el punto
            clean_number = ''.join(c for c in word if c.isdigit() or c == '.')
            amount = float(clean_number)
            continue
        except ValueError:
            description.append(word)
    
    if amount is None:
        return None
        
    return {
        'amount': amount,
        'description': ' '.join(description)
    }

@app.post("/process-message")
async def process_message(expense_msg: ExpenseMessage):
    print(f"Telegram ID recibido: {expense_msg.telegram_id}")
    # Verificar o registrar usuario
    user_id = is_user_authorized(expense_msg.telegram_id)
    if not user_id:
        raise HTTPException(status_code=403, detail="No se pudo autorizar al usuario")

    # Parsear el mensaje
    expense_data = parse_expense(expense_msg.message)
    if not expense_data:
        return {"status": "ignored", "message": "No se detectó un gasto válido"}

    # Categorizar el gasto
    category = categorize_chain.run(expense_data['description']).strip()

    # Guardar en la base de datos
    try:
        data = {
            'user_id': user_id,
            'description': expense_data['description'],
            'amount': expense_data['amount'],
            'category': category,
            'added_at': datetime.now().isoformat()
        }
        supabase.table('expenses').insert(data).execute()
        return {"status": "success", "message": f"{category} expense added ✅"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
