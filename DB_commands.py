import sqlite3
import os
import datetime


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(ROOT_DIR, 'database.db')

def add_user_action(user_id, user_name, user_nickname, command, city, hotels):
    dtime = str(datetime.datetime.now())[:-7]
    with sqlite3.connect((DB)) as conn:
        cursor = conn.cursor()
        cursor.execute("""
                INSERT INTO 'users_history' (user_id, user_name, user_nickname, command, request_date, city, finded_hotels)
                                    VALUES (?, ?, ?, ?, ?, ?, ?);
                """, (user_id, user_name, user_nickname, command, f'{dtime}', city, hotels))

def get_user_history():
    with sqlite3.connect((DB)) as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT command, request_date, finded_hotels FROM users_history "
                       f"WHERE user_id = 1454")
        result = cursor.fetchall()
        for i in result:
            string = str(f'команда: {i[0]}, дата: {i[1]}, отель: {i[2]}')
            print(string)

# add_user_action('Four seasons')
# add_user_action('Гостиница моя')
# add_user_action('Гостиница Россия')
# get_user_history()