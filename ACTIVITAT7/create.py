import psycopg2 as pg
from connection import create_connection

def create_user():
    try:
        conn = create_connection()
        connection = conn.cursor()
        print(connection)

        query = "INSERT INTO USERS(user_name,user_surname,user_age,user_email) VALUES(%s,%s,%s,%s);"

        values = ("Paul","Maigua","22","paul@hotmail.es")

        connection.execute(query, values)
        conn.commit()
    except(Exception, pg.Error) as error:
        print("Error: ", error)
    finally:
        conn.close()