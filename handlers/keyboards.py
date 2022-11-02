from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
def command_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.row_width = 1
    keyboard.add(   InlineKeyboardButton(text=" /help - помощь по командам бота ", callback_data="help"),
                    InlineKeyboardButton(text='/lowprice - топ самых дешевых отелей в городе', callback_data='lowprice'),
                    InlineKeyboardButton(text='/highprice - топ самых дорогих отелей в городе', callback_data='highprice'),
                    InlineKeyboardButton(text='/bestdeal - топ отелей в заданном диапазоне цены и удаленности от центра', callback_data='bestdeal'),
                    InlineKeyboardButton(text='/history - история поиска отелей', callback_data='history')
            )
    return keyboard


def help_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text=" /help - помощь по командам бота ", callback_data="help"))
    return keyboard