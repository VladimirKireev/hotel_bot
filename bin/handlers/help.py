from telebot.types import Message
from python_basic_diploma.loader import bot


print('это команда хелп')
# bot.send_message(258281993, 'тест хелп')

# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     print(message.text)


@bot.message_handler(content_types=["text"])
def bot_help(message: Message):
    bot.send_message(message.from_user.id, 'Это ')

#
# @bot.message_handler(commands=['help'])
# def get_text_messages(message: Message):
#     bot.reply_to(message, 'Помочь?')
