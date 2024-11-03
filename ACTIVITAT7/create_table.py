import psycopg2 as pg
from connection import create_connection

def create_table():
    try:
        # Agafem la conexió a la BBDD de connection.py
        conn = create_connection()
        connection = conn.cursor()

        sql = '''CREATE TABLE USERS(
                        user_id SERIAL PRIMARY KEY,
                        user_name VARCHAR(255) NOT NULL,
                        user_surname VARCHAR(255) NOT NULL,
                        user_age BIGINT NOT NULL,
                        user_email VARCHAR(255) NOT NULL
        )'''

        # Enviem la query per crear la taula USERS
        connection.execute(sql)
        # Commit per fer efectius els canvis de la query a la BBDD
        conn.commit()
    except(Exception, pg.Error) as error:
        print("Error: ", error)
    finally:
        # Tanquem la connexió a la base de dades
        conn.close()