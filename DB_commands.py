import sqlite3
import os
import datetime


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(ROOT_DIR, 'database.db')

print(f'{DB}  ')
def add_user_action():
    dtime = datetime.datetime.now()
    with sqlite3.connect((DB)) as conn:
        cursor = conn.cursor()
        cursor.execute("""
                INSERT INTO 'users_history' (user_id, user_name, user_nickname, command, request_date, finded_hotels)
                                    VALUES (?, ?, ?, ?, ?, ?);
                """, (1454, 'Bobby', 'Vlad', 'history', dtime, 'Four seasons'))

add_user_action()