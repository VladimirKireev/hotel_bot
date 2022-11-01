from loader import bot
from python_basic_diploma import handlers
from utils.set_bot_commands import set_default_commands


if __name__ == '__main__':
    set_default_commands(bot)



    # @bot.message_handler(commands=['help'])
    # def get_text_messages(message):
    #     bot.reply_to(message, 'Помочь?')

    # @bot.message_handler(commands=['start'])
    # def bot_start(message):
    #     bot.send_message(message.from_user.id, f"Привет, {message.from_user.full_name}!\n"
    #                                            f"Чтобы узнать, что я могу, введи команду /help")

    bot.infinity_polling()
