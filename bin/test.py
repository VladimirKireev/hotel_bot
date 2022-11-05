my_list = [
    {
        "geoId": "2114",
        "destinationId": "549499",
        "landmarkCityDestinationId": 'null',
        "type": "CITY",
        "redirectPage": "DEFAULT_PAGE",
        "latitude": 51.50746,
        "longitude": -0.127673,
        "searchDetail": 'null',
        "caption": "<span class='highlighted'>\u041b\u043e\u043d\u0434\u043e\u043d</span>, \u0410\u043d\u0433\u043b\u0438\u044f, \u0412\u0435\u043b\u0438\u043a\u043e\u0431\u0440\u0438\u0442\u0430\u043d\u0438\u044f",
        "name": "\u041b\u043e\u043d\u0434\u043e\u043d"
    },

		{
			"geoId": "2114",
			"destinationId": "549500",
			"landmarkCityDestinationId": 'null',
			"type": "HZ",
			"redirectPage": "DEFAULT_PAGE",
			"latitude": 51.50746,
			"longitude": -0.127673,
			"searchDetail": 'null',
			"caption": "<span class='highlighted'>\u041b\u043e\u043d\u0434\u043e\u043d</span>, \u0410\u043d\u0433\u043b\u0438\u044f, \u0412\u0435\u043b\u0438\u043a\u043e\u0431\u0440\u0438\u0442\u0430\u043d\u0438\u044f",
			"name": "\u041b\u043e\u043d\u0434\u043e\u043d"
		},


{
			"geoId": "2114",
			"destinationId": "549502",
			"landmarkCityDestinationId": 'null',
			"type": "HZ",
			"redirectPage": "DEFAULT_PAGE",
			"latitude": 51.50746,
			"longitude": -0.127673,
			"searchDetail": 'null',
			"caption": "<span class='highlighted'>\u041b\u043e\u043d\u0434\u043e\u043d</span>, \u0410\u043d\u0433\u043b\u0438\u044f, \u0412\u0435\u043b\u0438\u043a\u043e\u0431\u0440\u0438\u0442\u0430\u043d\u0438\u044f",
			"name": "\u041b\u043e\u043d\u0434\u043e\u043d"
		},
{
			"geoId": "2114",
			"destinationId": "549504",
			"landmarkCityDestinationId": 'null',
			"type": "CITY",
			"redirectPage": "DEFAULT_PAGE",
			"latitude": 51.50746,
			"longitude": -0.127673,
			"searchDetail": 'null',
			"caption": "<span class='highlighted'>\u041b\u043e\u043d\u0434\u043e\u043d</span>, \u0410\u043d\u0433\u043b\u0438\u044f, \u0412\u0435\u043b\u0438\u043a\u043e\u0431\u0440\u0438\u0442\u0430\u043d\u0438\u044f",
			"name": "\u041b\u043e\u043d\u0434\u043e\u043d"
}
	]

result = []

for i_elem in my_list:
	if i_elem['type'] == 'CITY':
		result.append(i_elem)
		land = i_elem['caption'].split()[-1]

		print(land)

print(result)