import sqlite3
from sqlite3 import Error

def record_to_db(dt, topic, value):
    try:
        conn = sqlite3.connect('./data/picoDB.db')
    except Exception as e:
        print(e)
    else:
        sql = """
            insert into pico_data(time, device, value)  values (?, ? , ?)
            """
        cursor = conn.cursor()
        cursor.execute(sql,(dt, topic, value))
        conn.commit()
        cursor.close()
        conn.close()