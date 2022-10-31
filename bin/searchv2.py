import json
import requests


url = "https://hotels4.p.rapidapi.com/locations/v2/search"

querystring = {"query":"алматы","locale":"en_US","currency":"USD"}

headers = {
	"X-RapidAPI-Key": "3b7f345943msh65de7279456f1e0p12e253jsn55b13eb898e0",
	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}


response = requests.request("GET", url, headers=headers, params=querystring)


data = json.loads(response.text, i)
with open('search_results.json', 'w') as file:
	json.dump(data, file, indent=4)
