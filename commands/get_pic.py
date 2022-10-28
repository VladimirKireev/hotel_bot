import json
import requests

def command():
	url = "https://hotels4.p.rapidapi.com/properties/get-hotel-photos"

	querystring = {"id":"1071625120"}

	headers = {
		"X-RapidAPI-Key": "3b7f345943msh65de7279456f1e0p12e253jsn55b13eb898e0",
		"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)


	data = json.loads(response.text)
	with open('pic_res.json', 'w') as file:
		json.dump(data, file, indent=4)

with open('pic_res.json', 'r') as file:
	res = json.load(file)

# print(res)
img_url = str(res['hotelImages'][0]['baseUrl'])
result = img_url.replace('{size}', 'z')
print(result)