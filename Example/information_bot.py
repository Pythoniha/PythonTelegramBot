#Pythoniha.ir
#MohamadReza Hassani
#Python 3+up

#import Modules
from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters

# Set token
updater = Updater('1338191387:AAFezuyrd4-OwPnOJfmw3bEhHVy5zeHazRQ', use_context = True)

#Start Def
def start(update, context):
    '''Send a Message when the Command /start is issued.'''
    context.bot.send_message(chat_id = update.message.chat_id, text = 'test')
    context.bot.send_message(chat_id = update.message.chat_id, text="Hello : {} \n Your Chat id : {} \n You is a Bot ? : {} ".format(update.message.from_user.first_name ,update.message.chat_id, update.message.from_user.is_bot))
    
# dispatcher to dp
dp = updater.dispatcher

#Set Handler
dp.add_handler(CommandHandler('start', start))


# Start Bot
updater.start_polling()

# Closed Bot Ctrl+C
updater.idle()
