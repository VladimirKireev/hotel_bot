import json
import requests


url = "https://hotels4.p.rapidapi.com/properties/v2/get-offers"

payload = {
	"currency": "USD",
	"eapid": 1,
	"locale": "en_US",
	"siteId": 300000001,
	"propertyId": "9209612",
	"checkInDate": {
		"day": 6,
		"month": 10,
		"year": 2022
	},
	"checkOutDate": {
		"day": 9,
		"month": 10,
		"year": 2022
	},
	"destination": {
		"coordinates": {
			"latitude": 12.24959,
			"longitude": 109.190704
		},
		"regionId": "6054439"
	},
	"rooms": [
		{
			"adults": 2,
			"children": [{"age": 5}, {"age": 7}]
		},
		{
			"adults": 2,
			"children": []
		}
	]
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "3b7f345943msh65de7279456f1e0p12e253jsn55b13eb898e0",
	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)

response = requests.request("POST", url, json=payload, headers=headers)



data = json.loads(response.text)
res = json.dumps(data, indent=4)
print(res)