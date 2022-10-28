import telebot

bot = telebot.TeleBot('5707824022:AAHZzhzXSm_kMQkzg8n2tVTBXEHn3qh27JM')

def lowprice_perform(message):
	@bot.message_handler(content_types=['text'])
	def info_request(message):
		print('погнали')
		bot.send_message(message.from_user.id, 'Введите город поиска')

		bot.send_message(message.from_user.id, message.text)

# bot.polling(none_stop=True, interval=0)

# def lowprice_perform(city='Алматы', hotel_count=10, need_photos=False, photo_count=0):
# 	print('текст')


# city = input('Введите город ')
# hotel_count = input('Введите количество отелей, которое необходимо вывести ')
# foto_request = 'Нужно ли загружать и выводить фотографии для каждого отеля? '
# if foto_request == 'да':
#     is_photo = True
# else:
#     is_photo = False
#
# if is_photo:
#     foto_count = int(input('Введите количество необходимых фотографий к каждому отелю'))


# url = "https://hotels4.p.rapidapi.com/locations/v2/search"
#
# querystring = {f"query":f"{city}","locale":"en_US","currency":"USD"}
#
# headers = {"X-RapidAPI-Key": "3b7f345943msh65de7279456f1e0p12e253jsn55b13eb898e0", "X-RapidAPI-Host": "hotels4.p.rapidapi.com"}
#
# response = requests.request("GET", url, headers=headers, params=querystring)


# with open('search_results.json', 'r') as file:
# 	data = json.load(file)
# citi_location = data['suggestions'][0]['entities'][0]['destinationId']
# print(citi_location)


# url = "https://hotels4.p.rapidapi.com/properties/list"
#
# querystring = {"destinationId":"737341","pageNumber":"1","pageSize":"10","checkIn":"2022-01-11","checkOut":"2022-11-11","adults1":"1","sortOrder":"PRICE","locale":"en_US","currency":"USD"}
#
# headers = {
# 	"X-RapidAPI-Key": "3b7f345943msh65de7279456f1e0p12e253jsn55b13eb898e0",
# 	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
# }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# data = json.loads(response.text)
#
# with open('list_result.json', 'r') as file:
# 	data = json.load(file)
#
# intro_text = f'По запросу {city} выведено {hotel_count} результатов:'
# results = data['data']['body']['searchResults']['results']
# top_hotels = []
# for i_hotel in results:
# 	# print(i_hotel)
# 	hotel_name = i_hotel['name']
# 	hotel_adress = i_hotel['address']['streetAddress']
# 	center_distance = i_hotel['landmarks'][0]['distance']
# 	price = i_hotel['ratePlan']['price']['current']
#
# 	result_text = f'{hotel_name}, расположенный по адресу: {hotel_adress}, расположенный на {center_distance} миль от центра по цене {price} за ночь.'
# 	top_hotels.append(result_text)
#
# print(intro_text)
# for i_result in top_hotels:
# 	print(i_result)