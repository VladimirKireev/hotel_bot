import json
import requests

url = "https://hotels4.p.rapidapi.com/properties/list"

querystring = {"destinationId":"737341","pageNumber":"1","pageSize":"10","checkIn":"2022-01-11","checkOut":"2022-11-11","adults1":"1","sortOrder":"PRICE","locale":"en_US","currency":"USD"}

headers = {
	"X-RapidAPI-Key": "3b7f345943msh65de7279456f1e0p12e253jsn55b13eb898e0",
	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)


data = json.loads(response.text)
with open('list_result_HP.json', 'w') as file:
	json.dump(data, file, indent=4)

