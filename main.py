import telebot
bot = telebot.TeleBot('5707824022:AAHZzhzXSm_kMQkzg8n2tVTBXEHn3qh27JM')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/lowprice':
        bot.send_message(message.from_user.id, 'тут пойдет исполнение команды LP')
    elif message.text == '/highprice':
        bot.send_message(message.from_user.id, 'тут пойдет исполнение команды HP')
    elif message.text == '/bestdeal':
        bot.send_message(message.from_user.id, 'тут пойдет исполнение команды BD')
    elif message.text == '/history':
        bot.send_message(message.from_user.id, 'тут пойдет исполнение команды history')
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Список команд:\n'
                                               '/lowprice - вывод самых дешевых отелей в городе\n'
                                               '/highprice - вывод самых дорогих отелей в городе\n'
                                               '/bestdeal - вывод отелей, наиболее подходящих по цене и расположению от центра\n'
                                               '/history - вывод истории поиска отелей\n')
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю. Чтобы узнать список команд напиши /help')

bot.polling(none_stop=True, interval=0)


