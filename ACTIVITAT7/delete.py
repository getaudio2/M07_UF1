import psycopg2 as pg
from connection import create_connection

def delete_user(id):
    try:
        conn = create_connection()
        connection = conn.cursor()

        query = "DELETE FROM USERS WHERE user_id = %s;"

        connection.execute(query, (id,)) # Executem la query per eliminar l'usuari segons l'id

        conn.commit()
    except(Exception, pg.Error) as error:
        print("Error: ", error)
    finally:
        conn.close()
