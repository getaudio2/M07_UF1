import psycopg2 as pg
from connection import create_connection

def update_user(id, col):
    try:
        conn = create_connection()
        connection = conn.cursor()
        print(connection)

        query = "update USERS SET user_email = %s WHERE user_id = %s;"

        values = (col, id)
        connection.execute(query, values)
        updated_recs = connection.rowcount

        conn.commit()
    except(Exception, pg.Error) as error:
        print("Error: ", error)
    finally:
        conn.close()

    return updated_recs