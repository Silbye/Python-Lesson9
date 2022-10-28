from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from bot_commands import *

updater = Updater("5638352626:AAFEwUfaGY-M2gFKfLnTHjBlZp6lwHA8YbU", use_context=True)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('help_add', help_add))
updater.dispatcher.add_handler(CommandHandler('add', add_data))
updater.dispatcher.add_handler(CommandHandler('import', import_data))
updater.dispatcher.add_handler(CommandHandler('send', send_document))
updater.dispatcher.add_handler(MessageHandler(Filters.document, downloader))
print('Started')

updater.start_polling()
updater.idle()