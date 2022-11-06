from loader import bot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def list_processing(result_list):
    pick_cities_list = []
    for i_elem in result_list:
        if i_elem['type'] == 'CITY':
            pick_cities_list.append(i_elem)
            # land = i_elem['caption'].split()[-1]
            # print(land)

    city_keyboard = InlineKeyboardMarkup()
    for i_city in pick_cities_list:
        land = i_city['caption'].split()[-1]
        city = i_city['name']
        city_keyboard.add(InlineKeyboardButton(text=f" {city} = {land} ", callback_data=f"Великобритания"))

    @bot.callback_query_handler(func=lambda call: call.data == 'Великобритания')
    def callback(call):
        bot.delete_message(chat_id=call.message.chat.id,
                           message_id=call.message.message_id)
