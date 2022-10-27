import json
import requests

def search_city(city='Алматы'):
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


def get_photo(hotel_id=1071625120):
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

    for i_photo in pictures:
        pic_url = i_photo['baseUrl']
        photos_list.append(pic_url)
    return photos_list


def hotel_list(destination_id=737341):
    url = "https://hotels4.p.rapidapi.com/properties/list"

    querystring = {"destinationId": f"{destination_id}", "pageNumber": "1", "pageSize": "3",
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
    for i_hotel in result:
        hotel_id = i_hotel['id']
        hotel_name = i_hotel['name']
        hotel_adress = i_hotel['address']['streetAddress']
        center_distance = i_hotel['landmarks'][0]['distance']
        price = i_hotel['ratePlan']['price']['current']
        photo_urls = get_photo(hotel_id)
        result_text = f'Айди отеля {hotel_id} {hotel_name}, расположенный по адресу: {hotel_adress}, расположенный на {center_distance} миль от центра по цене {price} за ночь.'
        top_hotels[f'{hotel_id}'] = {'result_message': result_text, 'photo_url_list': photo_urls}

    return top_hotels

test = hotel_list()
print(test.items())
#
# for i in test:
#     print(i)


# search_city('Париж')
# res = get_photo()
# print(res)