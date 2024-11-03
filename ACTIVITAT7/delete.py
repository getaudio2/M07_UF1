import psycopg2 as pg
from connection import create_connection

def delete_user(id):
    try:
        conn = create_connection()
        connection = conn.cursor()
        print(connection)

        query = "DELETE FROM USERS WHERE user_id = %s;"

        connection.execute(query, (id,))
        rows_updated = connection.rowcount

        conn.commit()
    except(Exception, pg.Error) as error:
        print("Error: ", error)
    finally:
        conn.close()

    return rows_updated