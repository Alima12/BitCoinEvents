from telegram.ext import Updater
 


updater = Updater(token='5149975683:AAHs-IJtlgZR7hNvKpMZZ3XO7YUDxriLLfg', use_context=True)
bot = updater.bot

reciver_list = ("1074680699",)


def send_notification(message:str)->None:
    for user in reciver_list:
            bot.send_message(user,message)