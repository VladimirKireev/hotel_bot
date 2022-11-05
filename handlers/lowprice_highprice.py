from loader import bot
from telebot import types
from python_basic_diploma.commands import search_city, hotel_list
from python_basic_diploma.DB_commands import add_user_action


class Destination:

    def __init__(self):
        self.city = None
        self.destination_id = None
        self.hotel_count = 0
        self.photos_count = 0
        self.city_list = dict()
        self.sort = None
        self.command = None

user_dict = dict()


#блок для команды lowprice
@bot.message_handler(commands=['lowprice'])
def get_text_messages(message):
    user_id = message.from_user.id
    # print(message.from_user.text)
    user_dict[user_id] = Destination()
    user_dict[user_id].sort = 'DISTANCE_FROM_LANDMARK'
    user_dict[user_id].command = 'lowprice'

    msg = bot.reply_to(message, 'В какой город вы собираетесь?')
    bot.register_next_step_handler(msg, pick_from_city_list_step)


@bot.message_handler(commands=['highprice'])
def get_text_messages(message):
    user_id = message.from_user.id
    user_dict[user_id] = Destination()
    user_dict[user_id].sort = 'PRICE_HIGHEST_FIRST'
    user_dict[user_id].command = 'highprice'
    msg = bot.reply_to(message, 'В какой город вы собираетесь?')
    bot.register_next_step_handler(msg, pick_from_city_list_step)


@bot.message_handler(commands=['bestdeal'])
def get_text_messages(message):
    user_id = message.from_user.id
    user_dict[user_id] = Destination()
    user_dict[user_id].sort = 'DISTANCE_FROM_LANDMARK'
    user_dict[user_id].command = 'bestdeal'
    msg = bot.reply_to(message, 'В какой город вы собираетесь?')
    bot.register_next_step_handler(msg, pick_from_city_list_step)


@bot.callback_query_handler(func=lambda call: call.data == 'lowprice')
def callback(call):
    user_id = call.from_user.id
    user_dict[user_id] = Destination()
    user_dict[user_id].sort = 'PRICE'
    user_dict[user_id].command = 'lowprice'
    bot.delete_message(chat_id=call.message.chat.id,
                       message_id=call.message.message_id)
    msg = bot.send_message(call.message.chat.id, 'В какой город вы собираетесь?')
    bot.register_next_step_handler(msg, pick_from_city_list_step)


@bot.callback_query_handler(func=lambda call: call.data == 'highprice')
def callback(call):
    user_id = call.from_user.id
    user_dict[user_id] = Destination()
    user_dict[user_id].sort = 'PRICE_HIGHEST_FIRST'
    user_dict[user_id].command = 'highprice'
    bot.delete_message(chat_id=call.message.chat.id,
                       message_id=call.message.message_id)
    msg = bot.send_message(call.message.chat.id, 'В какой город вы собираетесь?')
    bot.register_next_step_handler(msg, pick_from_city_list_step)


def pick_from_city_list_step(message):
    try:
        city_list = search_city(message.text)
        city_keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        user_id = message.from_user.id

        for i_city in city_list:
            destination_id = i_city['destinationId']
            land = i_city['caption'].split()[-1]
            city = i_city['name']
            reply = f'{city} в стране {land}'
            user_dict[user_id].city_list[reply] = destination_id
            button = types.KeyboardButton(text=reply)
            city_keyboard.row(button)
        print(user_dict[user_id].city_list)
        if len(city_list) == 0:
            raise Exception
        msg = bot.send_message(chat_id=message.chat.id,
                         text="Результаты поиска:",
                         reply_markup=city_keyboard)
        bot.register_next_step_handler(msg, city_pick_step)

    except Exception:
        bot.reply_to(message, 'Не могу найти такой город. Вам необходимо заново выбрать команду и осуществить поиск.')

def min_price_step(message): #дописать шаги с запросами минимальной и максимальной цены
    msg = bot.send_message(call.message.chat.id, 'В какой город вы собираетесь?')



def city_pick_step(message):
    user_id = message.from_user.id
    destination_id = user_dict[user_id].city_list[message.text]
    city = message.text.split()[0]
    print(city, destination_id)
    user_dict[user_id].city, user_dict[user_id].destination_id = city, destination_id
    user_dict[user_id].city_list = dict()
    msg = bot.send_message(message.from_user.id, 'Cколько вывести отелей в списке?', reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, hotel_count_step)


def hotel_count_step(message):
    try:
        hotel_count = int(message.text)
        user_id = message.from_user.id
        user_dict[user_id].hotel_count = int(hotel_count)
        if not 0 < hotel_count <= 20:
            raise ValueError

        kb = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        yes_btn = types.KeyboardButton(text='Да')
        no_btn = types.KeyboardButton(text='Нет')
        kb.add(yes_btn, no_btn)

        msg = bot.send_message(message.from_user.id, 'Вам нужны фотографии к отелям?', reply_markup=kb)
        bot.register_next_step_handler(msg, need_photo_step)
    except ValueError:
        bot.reply_to(message, 'Вы либо ввели неверное количество отелей, либо произошла ошибка ввода. Повторите поиск заново.')


def need_photo_step(message):
    answer = message.text
    user_name = message.from_user.first_name
    user_id = message.from_user.id
    nickname = message.from_user.username
    sort = user_dict[user_id].sort

    if answer == 'Да':
        user_dict[user_id].need_photos = True
        msg = bot.send_message(message.from_user.id, 'Сколько вывести картинок?', reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, photo_count_step)
    else:
        city = user_dict[user_id].city
        hotel_count = user_dict[user_id].hotel_count
        desnination_id = user_dict[user_id].destination_id
        res = hotel_list(destination_id=desnination_id, hotel_count=hotel_count, sort=sort)
        if len(res['hotels_info']) == 0:
            bot.send_message(message.from_user.id,
                             'По заданным параметрам ничего не найдено. '
                             'Попробуйте изменить диапазон цены, либо расстояние от центра города.',
                             reply_markup=types.ReplyKeyboardRemove())
        for i in res['hotels_info']:
            bot.send_message(message.from_user.id, i['result_message'], reply_markup=types.ReplyKeyboardRemove())

        command = user_dict[user_id].command
        hotels_list = res['hotels_list'][:-2]
        add_user_action(user_id, user_name, nickname, command, city, hotels_list)


def photo_count_step(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    nickname = message.from_user.username
    city = user_dict[user_id].city
    sort = user_dict[user_id].sort
    photo_count = int(message.text)
    hotel_count = user_dict[user_id].hotel_count
    desnination_id = user_dict[user_id].destination_id
    res = hotel_list(destination_id=desnination_id, hotel_count=hotel_count, sort=sort, photo_count=photo_count)
    for i in res['hotels_info']:
        photo_list = i['photo_url_list']
        bot.send_media_group(message.from_user.id, photo_list)
    hotels_list = res['hotels_list'][:-2]
    add_user_action(user_id, user_name, nickname, sort, city, hotels_list)