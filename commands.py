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

    citi_location = result['suggestions'][0]['entities'][0]['destinationId']
    print(citi_location)
    return citi_location


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


def hotel_list(destination_id=549499, hotel_count=3, sort='PRICE_HIGHEST_FIRST', photo_count=0):
    url = "https://hotels4.p.rapidapi.com/properties/list"

    querystring = {"destinationId": f"{destination_id}", "pageNumber": "1", "pageSize": f"{hotel_count}",
                   "checkIn":"2022-09-01","checkOut":"2022-10-08", "adults1": "1", "sortOrder": f"{sort}",
                   "locale": "en_US", "currency": "RUB"}

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

    if photo_count > 0:
        for i_hotel in result:
            hotel_id = i_hotel['id']
            hotel_name = i_hotel['name']
            hotel_adress = i_hotel['address']['streetAddress']
            center_distance = i_hotel['landmarks'][0]['distance']
            price = i_hotel['ratePlan']['price']['current']
            hotels_list += f'{hotel_name}, '
            result_text = f'{hotel_name}, расположенный по адресу: {hotel_adress}, расположенный на {center_distance} миль от центра по цене {price} за ночь.'
            photo_urls = get_photo(hotel_id, result_text, photo_count)

            top_hotels[f'hotels_info'].extend([{'result_message': result_text, 'photo_url_list': photo_urls}])
            # top_hotels[f'{hotel_id}'] = {'result_message': result_text, 'photo_url_list': photo_urls}

        top_hotels['hotels_list'] = hotels_list
        return top_hotels

    else:
        for i_hotel in result:
            hotel_id = i_hotel['id']
            print(hotel_id)
            hotel_name = i_hotel['name']
            print(hotel_name)
            hotel_adress = i_hotel['address']['streetAddress']
            center_distance = i_hotel['landmarks'][0]['distance']
            price = i_hotel['ratePlan']['price']['current']
            hotels_list += f'{hotel_name}, '
            result_text = f'{hotel_name}, расположенный по адресу: {hotel_adress}, расположенный на {center_distance} миль от центра по цене {price} за ночь.'
            top_hotels[f'{hotel_id}'] = {'result_message': result_text}
            # top_hotels[f'hotels_info'].append({f'{hotel_id}': {'result_message': result_text}})
            top_hotels[f'hotels_info'].append({'result_message': result_text})



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