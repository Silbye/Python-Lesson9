from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def log(update: Update, context: CallbackContext):
    file = open('bots\calculator\log.csv', 'a')
    file.write(f'{update.effective_user.first_name},{update.effective_user.id}, {update.message.text}\n')
    file.close()

def hello(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def help(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text("""Available Commands :-
    /hello - To be greeted by bot
    /summ with 2 numbers - to get summ of numbers
    /divide with 2 numbers - to get private of numbers
    /multiply with 2 numbers - to get multiplication of numbers
    /substract with 2 numbers - to get difference of numbers""")

def summ(update: Update, context: CallbackContext):
    log(update, context)
    entered = update.message.text
    data = entered.split()
    data.pop(0)
    if len(data) == 2:
        x = float(data[0])
        y = float(data[1])
        update.message.reply_text(summ_command(x, y))
    else:
        update.message.reply_text("Please make sure to only enter 2 numbers!")

def multiply(update: Update, context: CallbackContext):
    log(update, context)
    entered = update.message.text
    data = entered.split()
    data.pop(0)
    if len(data) == 2:
        x = float(data[0])
        y = float(data[1])
        update.message.reply_text(multiply_command(x, y))
    else:
        update.message.reply_text("Please make sure to only enter 2 numbers!")

def divide(update: Update, context: CallbackContext):
    log(update, context)
    entered = update.message.text
    data = entered.split()
    data.pop(0)
    if len(data) == 2:
        x = float(data[0])
        y = float(data[1])
        update.message.reply_text(divide_command(x, y))
    else:
        update.message.reply_text("Please make sure to only enter 2 numbers!")

def substract(update: Update, context: CallbackContext):
    log(update, context)
    entered = update.message.text
    data = entered.split()
    data.pop(0)
    if len(data) == 2:
        x = float(data[0])
        y = float(data[1])
        update.message.reply_text(substract_command(x, y))
    else:
        update.message.reply_text("Please make sure to only enter 2 numbers!")

def summ_command(x, y):
    result = x + y
    if result % 1 == 0:
        result = int(result)
    return result

def divide_command(x, y):
    if y == 0:
        return 'Cannot be divided by 0!'
    else:
        result = x / y
        if result % 1 == 0:
            result = int(result)
        return result

def multiply_command(x, y):
    result = x * y
    if result % 1 == 0:
        result = int(result)
    return result

def substract_command(x, y):
    result = x - y
    if result % 1 == 0:
        result = int(result)
    return result