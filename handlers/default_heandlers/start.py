from telebot.types import Message
from python_basic_diploma.loader import bot

@bot.message_handler(commands=['start'])
def bot_start(message: Message):
    bot.send_message(message.from_user.id, f"Привет, {message.from_user.full_name}!\n"
                              f"Чтобы узнать, что я могу, введи команду /help")
