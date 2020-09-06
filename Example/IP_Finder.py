# Import Modules
from telegram.ext import Updater, MessageHandler, Filters
from requests import get


# Token Here !
token = Updater("Tokennn .... HEREEE ''''", use_context=True)

# Find IP With API
ip = get('https://api.ipify.org').text
print('My public IP address is:', ip)


#Funciton For MessageHandler
def input(update, context):
  a = update.message.text
  a
  context.bot.send_message(chat_id = update.message.chat_id, text = a  + "shomare Ip : "+ ip )
  

# Set Dispatcher..
token.dispatcher.add_handler(MessageHandler(Filters.text, input))


# Start Bot
token.start_polling()


# Closed IDLE BackEnd Code
token.idle()
