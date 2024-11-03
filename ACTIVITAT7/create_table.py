import psycopg2 as pg
from connection import create_connection

def create_table():
    try:
        conn = create_connection()
        connection = conn.cursor()

        sql = '''CREATE TABLE USERS(
                        user_id SERIAL PRIMARY KEY,
                        user_name VARCHAR(255) NOT NULL,
                        user_surname VARCHAR(255) NOT NULL,
                        user_age BIGINT NOT NULL,
                        user_email VARCHAR(255) NOT NULL
        )'''

        connection.execute(sql)
        conn.commit()
    except(Exception, pg.Error) as error:
        print("Error: ", error)
    finally:
        conn.close()