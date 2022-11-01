from loader import bot
import python_basic_diploma.handlers
from utils.set_bot_commands import set_default_commands


if __name__ == '__main__':
    set_default_commands(bot)


    # @bot.message_handler(commands=['help'])
    # def get_text_messages(message):
    #     bot.reply_to(message, 'Помочь?')
    bot.infinity_polling()
