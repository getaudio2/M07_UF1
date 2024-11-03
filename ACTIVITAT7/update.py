import psycopg2 as pg
from connection import create_connection

def update_user(id, name, surname, age, email):
    try:
        conn = create_connection()
        connection = conn.cursor()

        query = '''UPDATE USERS 
                    SET user_name = %s, user_surname = %s,
                    user_age = %s, user_email = %s 
                    WHERE user_id = %s;'''

        values = (name, surname, age, email, id)
        connection.execute(query, values)

        conn.commit()
    except(Exception, pg.Error) as error:
        print("Error: ", error)
    finally:
        conn.close()
