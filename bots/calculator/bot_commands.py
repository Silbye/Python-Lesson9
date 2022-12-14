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
    /substract with 2 numbers - to get difference of numbers
    /complex - to get complex equations, example: (1 3 + 4 5) => (1 + 3j + 4 + 5j)""")

def complex_command(update: Update, context: CallbackContext):
    log(update, context)
    entered = update.message.text
    data = entered.split()
    data.pop(0)
    if len(data) == 5:
        try:
            x1 = float(data[0])
            x2 = float(data[1])
            equation = data[2]
            y1 = float(data[3])
            y2 = float(data[4])
            x = complex(x1, x2)
            y = complex(y1, y2)
            if equation == '+':
                update.message.reply_text(str(f"{x} + {y} = {x+y}"))
            elif equation == '-':
                update.message.reply_text(str(f"{x} - {y} = {x-y}"))
            elif equation == '/':
                update.message.reply_text(str(f"{x} / {y} = {x/y}"))
            elif equation == '*':
                update.message.reply_text(str(f"{x} * {y} = {x*y}"))
            else:
                update.message.reply_text("Calculator only supports these equation symbols: (+) (-) (*) (/)")
        except:
            update.message.reply_text("Please make sure to write a proper complex equation, example: (1 3 + 4 5) => (1 + 3j + 4 + 5j)")
    else:
        update.message.reply_text("Please make sure to write a proper complex equation, example: (1 3 + 4 5) => (1 + 3j + 4 + 5j)")
def summ(update: Update, context: CallbackContext):
    log(update, context)
    entered = update.message.text
    data = entered.split()
    data.pop(0)
    if len(data) == 2:
        try:   
            x = float(data[0])
            y = float(data[1])
            update.message.reply_text(summ_command(x, y))
        except:
            update.message.reply_text("Please make sure to enter numbers!")
    else:
        update.message.reply_text("Please make sure to only enter 2 numbers!")

def multiply(update: Update, context: CallbackContext):
    log(update, context)
    entered = update.message.text
    data = entered.split()
    data.pop(0)
    if len(data) == 2:
        try:   
            x = float(data[0])
            y = float(data[1])
            update.message.reply_text(multiply_command(x, y))
        except:
            update.message.reply_text("Please make sure to enter numbers!")
    else:
        update.message.reply_text("Please make sure to only enter 2 numbers!")

def divide(update: Update, context: CallbackContext):
    log(update, context)
    entered = update.message.text
    data = entered.split()
    data.pop(0)
    if len(data) == 2:
        try:   
            x = float(data[0])
            y = float(data[1])
            update.message.reply_text(divide_command(x, y))
        except:
            update.message.reply_text("Please make sure to enter numbers!")  
    else:
        update.message.reply_text("Please make sure to only enter 2 numbers!")

def substract(update: Update, context: CallbackContext):
    log(update, context)
    entered = update.message.text
    data = entered.split()
    data.pop(0)
    if len(data) == 2:
        try:   
            x = float(data[0])
            y = float(data[1])
            update.message.reply_text(substract_command(x, y))
        except:
            update.message.reply_text("Please make sure to enter numbers!")
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