import json
import requests
from telebot import types


def search_city(city):
    url = "https://hotels4.p.rapidapi.com/locations/v2/search"

    querystring = {"query": f"{city}", "locale": "en_US", "currency": "USD"}

    headers = {
        "X-RapidAPI-Key": "3b7f345943msh65de7279456f1e0p12e253jsn55b13eb898e0",
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    result = json.loads(response.text)

    citi_location = result['suggestions'][0]['entities'][0]['destinationId']
    print(citi_location)
    return citi_location


def get_photo(hotel_id, count):
    url = "https://hotels4.p.rapidapi.com/properties/get-hotel-photos"

    querystring = {"id": f"{hotel_id}"}

    headers = {
        "X-RapidAPI-Key": "3b7f345943msh65de7279456f1e0p12e253jsn55b13eb898e0",
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = json.loads(response.text)
    pictures = data['hotelImages']
    photos_list = []

    for photo_number, i_photo in enumerate(pictures):
        pic_url = str(i_photo['baseUrl']).replace('{size}', 'z')
        photo_object = types.InputMediaPhoto(pic_url)
        photos_list.append(photo_object)
        if photo_number + 1 == count:
            break

    return photos_list


def hotel_list(destination_id, hotel_count,  photo_count=0):
    url = "https://hotels4.p.rapidapi.com/properties/list"

    querystring = {"destinationId": f"{destination_id}", "pageNumber": "1", "pageSize": f"{hotel_count}",
                   "checkIn":"2022-09-01","checkOut":"2022-10-08", "adults1": "1", "sortOrder": "PRICE",
                   "locale": "en_US", "currency": "USD"}

    headers = {
        "X-RapidAPI-Key": "3b7f345943msh65de7279456f1e0p12e253jsn55b13eb898e0",
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)

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
            photo_urls = get_photo(hotel_id, photo_count)
            hotels_list += f'{hotel_name}, '
            result_text = f'{hotel_name}, расположенный по адресу: {hotel_adress}, расположенный на {center_distance} миль от центра по цене {price} за ночь.'

            top_hotels[f'hotels_info'].extend([{'result_message': result_text, 'photo_url_list': photo_urls}])
            # top_hotels[f'{hotel_id}'] = {'result_message': result_text, 'photo_url_list': photo_urls}

        top_hotels['hotels_list'] = hotels_list
        return top_hotels

    else:
        for i_hotel in result:
            hotel_id = i_hotel['id']
            hotel_name = i_hotel['name']
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

# search_city('Париж')
# res = get_photo()
# print(res)