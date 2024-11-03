import psycopg2 as pg
from connection import create_connection

def read_all():
    try:
        conn = create_connection()
        connection = conn.cursor()

        query = "SELECT * FROM USERS;"

        connection.execute(query)

        usuaris = connection.fetchall()
    except(Exception, pg.Error) as error:
        print("Error: ", error)
    finally:
        conn.close()

    return usuaris