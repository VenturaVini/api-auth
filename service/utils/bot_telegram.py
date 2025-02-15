import telebot

def enviar_mensagem(mensagem, CHAT_ID = '5588207726',BOT_TOKEN = '7294948712:AAEj57qIFRaXmS8ZB__0nq6SETufOIb6hzQ'):

    #BOT_TOKEN = '7294948712:AAEj57qIFRaXmS8ZB__0nq6SETufOIb6hzQ'

    bot = telebot.TeleBot(BOT_TOKEN)

    # ID do chat para onde você quer enviar a mensagem
    #CHAT_ID = '5588207726' # meu id

    # Mensagem que você quer enviar
    #MENSAGEM = mensagem

    # Enviando a mensagem
    bot.send_message(CHAT_ID, mensagem)
