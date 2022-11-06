from telebot.types import Message
from python_basic_diploma.handlers import keyboards
from loader import bot
from python_basic_diploma.DB_commands import get_user_history


@bot.message_handler(commands=['history'])
def bot_help(message: Message):
    user_id = message.from_user.id
    result = get_user_history(user_id)
    # print(result)
    for i_result in result:
        bot.send_message(chat_id=message.chat.id,
                         text=i_result)


