# Modules Import
from telegram.ext import Updater, MessageHandler, Filters

# Token Set
token = Updater("1068226999:AAGTogylBzLjzCEBTuRY9S2rVVnX2k1C_z4", use_context=True)


# Function's
def input(update, context):
  a = update.message.text
  a
  context.bot.send_message(chat_id = update.message.chat_id, text = 'a ' + "544" )


# Set Handler
token.dispatcher.add_handler(MessageHandler(Filters.text, input))


# Stsart Bot
token.start_polling()
token.idle()
