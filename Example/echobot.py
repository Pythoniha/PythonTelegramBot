from telegram.ext import Updater
from telegram.ext import CommandHandler ,MessageHandler, Filters

updater = Updater('1338191387:AAED9G1bxTftvuQf3BGh7fqg4y971zwCDkQ', use_context = True)


def start(update, context):
    context.bot.send_message(chat_id= update.message.chat_id, text= 'helo')
    print(update.message, sep='|')
    
def echo(update, context):
    update.message.reply_text(update.message.text)
    update.message.reply_text(update.message.photo)
    update.message.reply_text(update.message.from_user.language_code)
    
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
updater.dispatcher.add_handler(CommandHandler('Start', start))

    
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

updater.start_polling()
updater.idle()
