from telebot.types import Message
from python_basic_diploma.loader import bot

print('Это хэлпер')

@bot.message_handler(commands=['help'])
def bot_help(message: Message):
    bot.reply_to(message, 'Это хэлпер из файла хэлпер')