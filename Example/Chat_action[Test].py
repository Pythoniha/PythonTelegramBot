# import Lib !
from telegram.ext import Updater ,CommandHandler


# Set Token
updater = Updater("Tokeeeen Heeereeee !!!! ", use_context=True)

# Line command
def start(bot, context):
  context.bot.send_message(chat_id= bot.message.chat_id, text='Hello')
  
  # This line for Chat is typing action ....
  context.bot.send_chat_action(chat_id=bot.message.chat_id, action="typing")
  


# Set Dispatchers !
updater.dispatcher.add_handler(CommandHandler('start',start))



# Start Bot !
updater.start_polling()

# Closed IDLE Command Back-End Bot :|
updater.idle()
