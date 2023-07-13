from dotenv import load_dotenv
from os import getenv
import telebot
from utils.banner import banner

load_dotenv()
token = getenv("TOKEN")

message_sorry = """
Sorry I didn't understand your message (click on one of the alternatives below):

    /option1 - lorem ipsum
    /option2 - lorem ipsum
    /help    - show help
"""

message_help = """
Help:

    /option1 - lorem ipsum
    /option2 - lorem ipsum
    /option3 - lorem ipsum
    /option4 - lorem ipsum
    /option5 - lorem ipsum
    /option6 - lorem ipsum
    /option7 - lorem ipsum
"""

class main:
    def __init__(self, token):
        self.token = token
        banner()
        print("Bot is running...\n")        


    def create_bot(self):
        bot = telebot.TeleBot(token)

        def verify(message): 
            return True if message else False
        
        @bot.message_handler(commands=["help"])
        def res(message): 
            bot.send_message(message.chat.id, message_help) 
        
        @bot.message_handler(commands=["hi"])
        def res(message):
            bot.send_message(message.chat.id, "hi :)")       

        @bot.message_handler(func=verify)
        def res(message):
            bot.send_message(message.chat.id, message_sorry)

        bot.polling()


main(token).create_bot()    
