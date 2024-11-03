import psycopg2 as pg
from connection import create_connection

def create_user(name, surname, age, email):
    try:
        conn = create_connection()
        connection = conn.cursor()

        query = "INSERT INTO USERS(user_name,user_surname,user_age,user_email) VALUES(%s,%s,%s,%s);"

        values = (name,surname,age,email)

        connection.execute(query, values)
        conn.commit()
    except(Exception, pg.Error) as error:
        print("Error: ", error)
    finally:
        conn.close()