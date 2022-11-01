from telebot.types import Message
from python_basic_diploma.loader import bot


@bot.message_handler(commands=['help'])
def bot_help(message: Message):
    bot.send_message(message.from_user.id, 'Это команда помощи?')
