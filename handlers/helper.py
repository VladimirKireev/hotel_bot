from telebot.types import Message
from python_basic_diploma.handlers import keyboards
from loader import bot


@bot.message_handler(commands=['help', 'start'])
def bot_help(message: Message):
    bot.send_message(chat_id=message.chat.id,
                     text="Вот что я умею:",
                     reply_markup=keyboards.command_keyboard())


@bot.callback_query_handler(func=lambda call: call.data == 'help')
def callback(call):
    # bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
    bot.delete_message(chat_id=call.message.chat.id,
                       message_id=call.message.message_id)
    bot_help(call.message)

