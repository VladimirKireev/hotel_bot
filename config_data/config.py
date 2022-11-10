import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

DEFAULT_COMMANDS = (
    ('start', "Запустить бота"),
    ('help', "Вывести справку"),
    ('lowprice', "Вывод самых дешевых отелей"),
    ('highprice', "Вывод самых дорогих отелей"),
    ('bestdeal', "Вывод отелей по заданной конфигурации"),
    ('history', "Вывести историю поиска")
)
