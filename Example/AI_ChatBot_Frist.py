# Import Moduls
from telegram.ext import Updater, MessageHandler, Filters



# Token Here !
token = Updater("Token Hereeee ", use_context=True)


#Funciton For MessageHandler
def input(update, context):
  # Text Plan a
  a = update.message.text
  a
  if a =="سلام":
    context.bot.send_message(chat_id = update.message.chat_id, text = a  + "سلام خوش آمدید !")
  else:
    context.bot.send_message(chat_id = update.message.chat_id, text = a  + "سلام بده")
  # Text Plain B
  b = update.message.text
  b
  if b =="خوبی":
    context.bot.send_message(chat_id = update.message.chat_id, text = a  + "سلام خوش آمدید !")
  else:
    context.bot.send_message(chat_id = update.message.chat_id, text = a  + "سلام بده")

  

# Set Dispatcher..
token.dispatcher.add_handler(MessageHandler(Filters.text, input))


# Start Bot
token.start_polling()


# Closed IDLE BackEnd Code
token.idle()
