import json
import requests
from telebot import types


def search_city(city):
    url = "https://hotels4.p.rapidapi.com/locations/v2/search"

    querystring = {"query": f"{city}", "locale": "ru_RU", "currency": "RUB"}

    headers = {
        "X-RapidAPI-Key": "bf1948fae7mshea6c4db01483900p1f0237jsn16fcf944b8bd",
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    result = json.loads(response.text)

    with open('Cities.json', 'w') as file:
        json.dump(result, file, indent=4)

    result_cities = result['suggestions'][0]['entities']
    pick_cities_list = []
    for i_elem in result_cities:
        if i_elem['type'] == 'CITY':
            pick_cities_list.append(i_elem)

    return pick_cities_list


def get_photo(hotel_id, hotel_name, count):
    url = "https://hotels4.p.rapidapi.com/properties/get-hotel-photos"

    querystring = {"id": f"{hotel_id}"}

    headers = {
        "X-RapidAPI-Key": "bf1948fae7mshea6c4db01483900p1f0237jsn16fcf944b8bd",
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = json.loads(response.text)
    pictures = data['hotelImages']
    photos_list = []

    for photo_number, i_photo in enumerate(pictures):
        pic_url = str(i_photo['baseUrl']).replace('{size}', 'z')
        if photo_number == 0:
            photo_object = types.InputMediaPhoto(pic_url, caption=hotel_name)
        else:
            photo_object = types.InputMediaPhoto(pic_url)
        photos_list.append(photo_object)
        if photo_number + 1 == count:
            break

    return photos_list


def hotel_list(destination_id, hotel_count,
               sort, max_distance,
               min_price, max_price, photo_count=0):
    url = "https://hotels4.p.rapidapi.com/properties/list"

    querystring = {"destinationId": f"{destination_id}", "pageNumber": "1", "pageSize": f"100",
                   "checkIn":"2022-09-01","checkOut":"2022-10-08", "adults1": "1", "sortOrder": f"{sort}",
                   "priceMin": {min_price}, "priceMax": {max_price},
                   "locale": "en_US", "currency": "RUB", "landmarkIds": "city_center"}

    headers = {
        "X-RapidAPI-Key": "bf1948fae7mshea6c4db01483900p1f0237jsn16fcf944b8bd",
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    with open('HP_RESULT.json', 'w') as file:
        json.dump(data, file, indent=4)

    result = data['data']['body']['searchResults']['results']
    top_hotels = dict()
    top_hotels[f'hotels_info'] = []
    hotels_list = ''
    count = 0

    if photo_count > 0:
        for i_hotel in result:
            if count == int(hotel_count):
                break

            try:
                hotel_id = i_hotel['id']
                hotel_name = i_hotel['name']
                hotel_adress = i_hotel['address']['streetAddress']
                center_distance = round(float(i_hotel['landmarks'][0]['distance'][:-6]) * 1.609, 1)
                price = i_hotel['ratePlan']['price']['current']
                hotels_list += f'{hotel_name}, '
                result_text = f'{hotel_name}, расположенный по адресу: {hotel_adress}, расположенный на {center_distance} км от центра по цене {price} за ночь.'
                photo_urls = get_photo(hotel_id, result_text, photo_count)
                if float(center_distance) <= float(max_distance):
                    top_hotels[f'hotels_info'].extend([{'result_message': result_text, 'photo_url_list': photo_urls}])
                    count += 1

            except KeyError:
                pass

        top_hotels['hotels_list'] = hotels_list
        return top_hotels

    else:
        for i_hotel in result:
            if count == int(hotel_count):
                break
            try:
                hotel_id = i_hotel['id']
                # print(hotel_id)
                hotel_name = i_hotel['name']
                # print(hotel_name)
                hotel_adress = i_hotel['address']['streetAddress']
                center_distance = round(float(i_hotel['landmarks'][0]['distance'][:-6]) * 1.609, 1)
                price = i_hotel['ratePlan']['price']['current']
                hotels_list += f'{hotel_name}, '
                result_text = f'{hotel_name}, расположенный по адресу: {hotel_adress}, расположенный на {center_distance} км от центра по цене {price} за ночь.'
                top_hotels[f'{hotel_id}'] = {'result_message': result_text}
                if float(center_distance) <= float(max_distance):
                    top_hotels[f'hotels_info'].append({'result_message': result_text})
                    count += 1
            except KeyError:
                pass

        top_hotels['hotels_list'] = hotels_list
        return top_hotels

# test = hotel_list()
# print(test.items())
# print()
# for i in test.items():
#     print(i)
#
# print()
# for i in test.keys():
#     print(i)
#
# print()
# for i in test.values():
#     print(i)

# search_city('Лондон')
# res = get_photo()
# print(res)