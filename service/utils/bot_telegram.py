import os
from dotenv import load_dotenv
import telebot


# Carrega o .env somente se estiver rodando localmente
if os.getenv('RAILWAY_ENVIRONMENT') is None:
    load_dotenv()

# Lê as variáveis de ambiente
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

def enviar_mensagem(mensagem, CHAT_ID = '5588207726',BOT_TOKEN = os.getenv('BOT_TOKEN')):

    #BOT_TOKEN = '7294948712:AAEj57qIFRaXmS8ZB__0nq6SETufOIb6hzQ'

    bot = telebot.TeleBot(BOT_TOKEN)

    # ID do chat para onde você quer enviar a mensagem
    #CHAT_ID = '5588207726' # meu id

    # Mensagem que você quer enviar
    #MENSAGEM = mensagem

    # Enviando a mensagem
    bot.send_message(CHAT_ID, mensagem)
