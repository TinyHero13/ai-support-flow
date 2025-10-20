from langchain.tools import tool
from telegram import Bot
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@tool("ticket_tool")
def ticket_node(query: str) -> str:
    """
    Use esta ferramenta sempre que o usuário quiser precisar de um suporte que não esteja no FAQ.
    
    Ao chamar esta ferramenta, você DEVE formatar a query de forma detalhada incluindo:
    - Título do ticket
    - Descrição completa do problema ou solicitação do usuário
    - Qualquer informação adicional relevante mencionada pelo usuário
    
    Exemplo de formato:
    Título: Reset de senha
    Descrição: O usuário está solicitando o reset de senha da conta.
    """
    try:
        async def send_telegram_message():
            bot = Bot(token=TELEGRAM_BOT_TOKEN)
            await bot.send_message(chat_id=CHAT_ID, text=f"Novo Ticket aberto\n\n{query}")
        
        asyncio.run(send_telegram_message())
        return f"Ticket aberto com sucesso! Mensagem enviada: {query}"
    except Exception as e:
        return f"Erro ao abrir ticket: {e}"
