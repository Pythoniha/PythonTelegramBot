# Import modules in python
from telegram.ext import Updater
from telegram.ext import CommandHandler

# import Logging Modules in python for Write Error in file text For debug
import logging

# Debug save Error
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                     level=logging.INFO)

# Set Token
updater = Updater(token='1338191387:AAFezuyrd4-OwPnOJfmw3bEhHVy5zeHazRQ', use_context=True)

# Def for Keyline keyword And Action
def start(update, context):
    context.bot.send_message(chat_id= update.message.chat_id, text = 'Hellooooo Word !')

def help1(update, context):
    context.bot.send_message(chat_id = update.message.chat_id, text='Help Menu , Enter to /info')
    
def info(update, context):
    context.bot.send_message(chat_id = update.message.chat_id, text = "Please Enter Your Company INfo ! ")


# Plus Dispatcher for Set def + Keyline in Telegram bot
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help1))
updater.dispatcher.add_handler(CommandHandler('info', info))



# Start The robot in python
updater.start_polling()
updater.idle()
