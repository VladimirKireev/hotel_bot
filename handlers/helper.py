from telebot.types import Message
from python_basic_diploma.handlers import keyboards
from loader import bot

print('Это хэлпер')

@bot.message_handler(commands=['help'])
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


# @bot.callback_query_handler(func=lambda call: call.data == 'lowprice')
# def callback(call):
#     # bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
#     bot.delete_message(chat_id=call.message.chat.id,
#                        message_id=call.message.message_id)
#     bot.send_message(call.message.chat.id, 'Я колбэк команды lowprice')



# def help_keyboard():
#     keyboard = InlineKeyboardMarkup()
#     keyboard.add(InlineKeyboardButton(text=" /help - помощь по командам бота ", callback_data="help"))
#     return keyboard
#
# def command_keyboard():
#     keyboard = InlineKeyboardMarkup()
#     keyboard.row_width = 1
#     keyboard.add(
#                     InlineKeyboardButton(text='/lowprice - топ самых дешевых отелей в городе', callback_data='lowprice'),
#                     InlineKeyboardButton(text='/highprice - топ самых дорогих отелей в городе', callback_data='highprice'),
#                     InlineKeyboardButton(text='/bestdeal - топ отелей в заданном диапазоне цены и удаленности от центра', callback_data='bestdeal'),
#                     InlineKeyboardButton(text='/history - история поиска отелей', callback_data='history')
#             )
#     return keyboard