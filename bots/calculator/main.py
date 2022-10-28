from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *

updater = Updater('5533646159:AAGVlgXzQgaMtUcemBlOqGsiSF6uCW_azcw', use_context=True)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('summ', summ))
updater.dispatcher.add_handler(CommandHandler('divide', divide))
updater.dispatcher.add_handler(CommandHandler('multiply', multiply))
updater.dispatcher.add_handler(CommandHandler('substract', substract))
print('Started')

updater.start_polling()
updater.idle()