import telebot
from commands.subcommands import *


bot = telebot.TeleBot('5707824022:AAHZzhzXSm_kMQkzg8n2tVTBXEHn3qh27JM')

class Destination:

    def __init__(self, city):
        self.city = city
        self.hotel_count = 0
        self.need_photos = False
        self.photos_count = 0

user_dict = dict()

@bot.message_handler(commands=['lowprice'])
def get_text_messages(message):
    msg = bot.reply_to(message, 'В какой город вы собираетесь?')


    bot.register_next_step_handler(msg, city_pick_step)

def city_pick_step(message):
    city = message.text
    user_id = message.from_user.id
    user_dict[user_id] = Destination(city)
    print(user_dict[user_id].city)
    msg = bot.reply_to(message, 'Cколько вывести отелей в списке?')
    bot.register_next_step_handler(msg, hotel_count_step)


def hotel_count_step(message):
    hotel_count = message.text
    user_id = message.from_user.id
    user_dict[user_id].hotel_count = hotel_count
    print(user_dict[user_id].hotel_count)
    msg = bot.reply_to(message, 'Вам нужны фотографии к отелям? (да/нет)')
    bot.register_next_step_handler(msg, need_photo_step)


def need_photo_step(message):
    answer = message.text
    # print(answer)
    user_id = message.from_user.id

    if answer == 'да':
        user_dict[user_id].need_photos = True
        msg = bot.reply_to(message, 'Сколько вывести картинок?')
        bot.register_next_step_handler(msg, photo_count_step)
    else:
        city = user_dict[user_id].city
        hotel_count = user_dict[user_id].hotel_count
        need_photos = user_dict[user_id].need_photos #убрать из класса Destination потом
        desnination_id = search_city(city)

        res = hotel_list(desnination_id, hotel_count)
        for i in res.values():
            print(i['result_message'])




def photo_count_step(message):
    user_id = message.from_user.id
    city = user_dict[user_id].city
    photo_count = int(message.text)
    hotel_count = user_dict[user_id].hotel_count
    desnination_id = search_city(city)
    res = hotel_list(desnination_id, hotel_count, photo_count)
    for i in res.values():
        bot.send_message(message.from_user.id, i['result_message'])
        for i_photo in i['photo_url_list']:
            bot.send_photo(message.from_user.id, i_photo)





bot.polling(none_stop=True, interval=0)




# @bot.message_handler(commands=['start', 'help', 'lowprice', 'highprice', 'bestdeal', 'history'])
# def get_text_messages(message):
#
#     user_id = message.from_user.id
#     nickname = message.from_user.username
#     user_name = message.from_user.first_name
#     # print(message.text)
#
#     if message.text == '/start' or message.text == '/help':
#         bot.send_message(message.from_user.id, 'Список команд:\n'
#                                                '/lowprice - вывод самых дешевых отелей в городе\n'
#                                                '/highprice - вывод самых дорогих отелей в городе\n'
#                                                '/bestdeal - вывод отелей, наиболее подходящих по цене и расположению от центра\n'
#                                                '/history - вывод истории поиска отелей\n')
#
#
#     elif message.text == '/lowprice':
#         # lowprice_perform(message)
#         bot.send_message(message.from_user.id, 'тут пойдет исполнение команды LP')
#
#         # sent = bot.reply_to(message, 'Введите город поиска')
#         # bot.register_next_step_handler(sent, city)
#         # sent2 = bot.reply_to(message, 'Введите количество отелей для поиска')
#         # bot.register_next_step_handler(sent2, city)
#
#
#         bot.reply_to(message, 'Введите город поиска')
#         @bot.message_handler(content_types=['text'])
#         def send_hello(message):
#             print(message.text)
#             city = city_message.text
#
#
#
#         # bot.send_message(message.from_user.id, 'Сколько отелей Вам показать?')
#         # @bot.message_handler(content_types=['text'])
#         # def city_information(hotel_count_message):
#         #     print(hotel_count_message.text)
#         #     hotel_count = int(hotel_count_message.text)
#         #
#         # is_photo = False
#         # bot.send_message(message.from_user.id, 'Нужно ли показать фотографии отеля?')
#         # @bot.message_handler(content_types=['text'])
#         # def photo_information(photo_info_message):
#         #     print(photo_info_message.text)
#         #     if photo_info_message.text.lower == 'да':
#         #         bot.send_message(message.from_user.id, 'Сколько фото показать?')
#         #         @bot.message_handler(content_types=['text'])
#         #         def photo_count_info(photo_count_message):
#         #             print(photo_count_message.text)
#         #             is_photo = True
#         #             photo_count = int(photo_count_message.text)
#         #
#
#         # url = ['https://exp.cdn-hotels.com/hotels/34000000/33460000/33457100/33457035/182cede3_z.jpg', 'https://exp.cdn-hotels.com/hotels/34000000/33460000/33457100/33457035/b7ff0af5_z.jpg']
#
#         # for i_photo in url:
#         #     bot.send_photo(message.from_user.id, i_photo)
#
#
#
#
#
#     elif message.text == '/highprice':
#         bot.send_message(message.from_user.id, 'тут пойдет исполнение команды HP')
#     elif message.text == '/bestdeal':
#         bot.send_message(message.from_user.id, 'тут пойдет исполнение команды BD')
#     elif message.text == '/history':
#         bot.send_message(message.from_user.id, 'тут пойдет исполнение команды history')
#     else:
#         bot.send_message(message.from_user.id, 'Я тебя не понимаю. Чтобы узнать список команд напиши /help')


