import requests

url = "https://hotels4.p.rapidapi.com/properties/list"

querystring = {"destinationId":"1506246","pageNumber":"1","pageSize":"25","checkIn":"<REQUIRED>","checkOut":"<REQUIRED>","adults1":"1","sortOrder":"PRICE_HIGHEST_FIRST","locale":"en_US","currency":"USD"}

headers = {
	"X-RapidAPI-Key": "bf1948fae7mshea6c4db01483900p1f0237jsn16fcf944b8bd",
	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)