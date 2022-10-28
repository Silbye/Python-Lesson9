from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

def hello(update: Update, context: CallbackContext):
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /hello - To be greeted by bot
    /add - To add new data and export it to file
    /help_add - To see available separators
    /import - To import data from file
    /send - To ask bot to send you the file
    send your file to overwrite current data in the file""")

def help_add(update: Update, context: CallbackContext):
    update.message.reply_text("Available Separators: (,) (;) (:) (None or none)")

def add_data(update: Update, context: CallbackContext):
    file = open('bots\phone\phones.csv', 'a+')
    entered = update.message.text
    data = entered.split()
    data.pop(0)
    if len(data) == 5:
        separate = data[4]
        data.pop(4)
        update.message.reply_text("Data added!")
        if separate == 'None' or separate == 'none':
            for i in data:
                file.write(f"{i}\n")
            file.write(f"\n")
        else:
            file.write(separate.join(data))
            file.write(f"\n")
    else:
        update.message.reply_text("Please make sure to only enter 5 variables(Surname, Name, Phone number, Commentary, Separator( (,) (;) (:) (None) )")

def import_data(update: Update, context: CallbackContext):
    file = open('bots\phone\phones.csv', 'r')
    data = []
    t = []
    for line in file:
        if ',' in line:
            temp = line.strip().split(',')
            data.append(temp)
        elif ';' in line:
            temp = line.strip().split(';')
            data.append(temp)
        elif ':' in line:
            temp = line.strip().split(':')
            data.append(temp)
        elif line != '':
            if line != '\n':
                t.append(line.strip())
            else:
                data.append(t)
                t= []
    if len(data) > 0:
        for info in data:
            update.message.reply_text(f"{info}")
    else:
        update.message.reply_text("The list is empty!")

def send_document(update, context):
    chat_id = update.message.chat_id
    document = open('bots\phone\phones.csv', 'rb')
    context.bot.send_document(chat_id, document)

def downloader(update, context):
    context.bot.get_file(update.message.document).download()

    with open('bots\phone\phones.csv', 'wb') as f:
        context.bot.get_file(update.message.document).download(out=f)