import telebot
from python_basic_diploma.commands import *
from telebot import types
from python_basic_diploma.config_data.config import BOT_TOKEN

from DB_commands import add_user_action


bot = telebot.TeleBot(BOT_TOKEN) #Второй бот, первый что-то не работает
# bot = telebot.TeleBot('5707824022:AAHZzhzXSm_kMQkzg8n2tVTBXEHn3qh27JM') #Старый токен который кто-то украл


class Destination:

    def __init__(self, city, destination_id):
        self.city = city
        self.destination_id = destination_id
        self.hotel_count = 0
        self.photos_count = 0

user_dict = dict()


#блок для команды lowprice
@bot.message_handler(commands=['lowprice'])
def get_text_messages(message):
    msg = bot.reply_to(message, 'В какой город вы собираетесь?')
    bot.register_next_step_handler(msg, city_pick_step)


def city_pick_step(message):
    city = message.text
    try:
        desnination_id = search_city(city)
        user_id = message.from_user.id
        user_dict[user_id] = Destination(city, desnination_id)
        print(user_dict[user_id].city)
        msg = bot.reply_to(message, 'Cколько вывести отелей в списке?')
        bot.register_next_step_handler(msg, hotel_count_step)
    except IndexError:
        bot.reply_to(message, 'Не могу найти такой город. Вам необходимо заново выбрать команду и осуществить поиск.')



def hotel_count_step(message):
    hotel_count = message.text
    user_id = message.from_user.id
    user_dict[user_id].hotel_count = hotel_count
    print(user_dict[user_id].hotel_count)
    kb = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    yes_btn = types.KeyboardButton(text='Да')
    no_btn = types.KeyboardButton(text='Нет')
    kb.add(yes_btn, no_btn)

    msg = bot.send_message(message.from_user.id, 'Вам нужны фотографии к отелям?', reply_markup=kb)
    bot.register_next_step_handler(msg, need_photo_step)


def need_photo_step(message):
    answer = message.text
    user_name = message.from_user.first_name
    user_id = message.from_user.id
    nickname = message.from_user.username

    if answer == 'Да':
        user_dict[user_id].need_photos = True
        msg = bot.reply_to(message, 'Сколько вывести картинок?')
        bot.register_next_step_handler(msg, photo_count_step)
    else:
        city = user_dict[user_id].city
        hotel_count = user_dict[user_id].hotel_count
        desnination_id = user_dict[user_id].destination_id

        res = hotel_list(destination_id=desnination_id, hotel_count=hotel_count, sort='PRICE')
        for i in res['hotels_info']:
            bot.send_message(message.from_user.id, i['result_message'])

        hotels_list = res['hotels_list'][:-2]
        add_user_action(user_id, user_name, nickname, '/lowprice', city, hotels_list)


def photo_count_step(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    nickname = message.from_user.username
    city = user_dict[user_id].city
    photo_count = int(message.text)
    hotel_count = user_dict[user_id].hotel_count
    desnination_id = user_dict[user_id].destination_id
    res = hotel_list(destination_id=desnination_id, hotel_count=hotel_count, sort='PRICE', photo_count=photo_count)
    for i in res['hotels_info']:
        photo_list = i['photo_url_list']
        bot.send_media_group(message.from_user.id, photo_list)
    hotels_list = res['hotels_list'][:-2]
    add_user_action(user_id, user_name, nickname, '/lowprice', city, hotels_list)

#блок для команды highprice
@bot.message_handler(commands=['highprice'])
def get_text_messages(message):
    msg = bot.reply_to(message, 'В какой город вы собираетесь?')
    bot.register_next_step_handler(msg, hp_city_pick_step)


def hp_city_pick_step(message):
    city = message.text
    try:
        desnination_id = search_city(city)
        user_id = message.from_user.id
        user_dict[user_id] = Destination(city, desnination_id)
        print(user_dict[user_id].city)
        msg = bot.reply_to(message, 'Cколько вывести отелей в списке?')
        bot.register_next_step_handler(msg, hp_hotel_count_step)
    except IndexError:
        bot.reply_to(message, 'Не могу найти такой город. Вам необходимо заново выбрать команду и осуществить поиск.')


def hp_hotel_count_step(message):
    hotel_count = message.text
    user_id = message.from_user.id
    user_dict[user_id].hotel_count = hotel_count
    print(user_dict[user_id].hotel_count)
    kb = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    yes_btn = types.KeyboardButton(text='Да')
    no_btn = types.KeyboardButton(text='Нет')
    kb.add(yes_btn, no_btn)

    msg = bot.send_message(message.from_user.id, 'Вам нужны фотографии к отелям?', reply_markup=kb)
    bot.register_next_step_handler(msg, hp_need_photo_step)


def hp_need_photo_step(message):
    answer = message.text
    user_name = message.from_user.first_name
    user_id = message.from_user.id
    nickname = message.from_user.username

    if answer == 'Да':
        user_dict[user_id].need_photos = True
        msg = bot.reply_to(message, 'Сколько вывести картинок?')
        bot.register_next_step_handler(msg, hp_photo_count_step)
    else:
        city = user_dict[user_id].city
        hotel_count = user_dict[user_id].hotel_count
        desnination_id = user_dict[user_id].destination_id

        res = hotel_list(destination_id=desnination_id, hotel_count=hotel_count, sort='PRICE_HIGHEST_FIRST')
        for i in res['hotels_info']:
            bot.send_message(message.from_user.id, i['result_message'])

        hotels_list = res['hotels_list'][:-2]
        add_user_action(user_id, user_name, nickname, '/highprice', city, hotels_list)


def hp_photo_count_step(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    nickname = message.from_user.username
    city = user_dict[user_id].city
    photo_count = int(message.text)
    hotel_count = user_dict[user_id].hotel_count
    desnination_id = user_dict[user_id].destination_id
    res = hotel_list(destination_id=desnination_id, hotel_count=hotel_count, sort='PRICE_HIGHEST_FIRST', photo_count=photo_count)
    for i in res['hotels_info']:
        photo_list = i['photo_url_list']
        bot.send_media_group(message.from_user.id, photo_list)
    hotels_list = res['hotels_list'][:-2]
    add_user_action(user_id, user_name, nickname, '/highprice', city, hotels_list)


bot.infinity_polling()

