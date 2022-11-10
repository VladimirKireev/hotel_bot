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

def get_user_history(user_id):
    with sqlite3.connect((DB)) as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT command, request_date, city, finded_hotels FROM users_history "
                       f"WHERE user_id = {user_id}")
        result = cursor.fetchall()
        history_result = []
        for i in result:
            command, date, city, hotels = i
            if len(hotels) > 1:
                reply_row = f'{date} по команде {command[1:]} в {city} были найдены отели: {hotels}'
            else:
                reply_row = f'{date} по команде {command[1:]} в {city} был найден отель: {hotels}'
            history_result.append(reply_row)
            # print(reply_row)
            # print(history_result)

        # for i in history_result:
        #     print(i)
        return history_result
#
# get_user_history(1028158464)