import psycopg2 as pg

def create_connection():
    try:
        conn = pg.connect(
            database="postgres",
            user='admin',
            password='1234',
            host='localhost',
            port='5432'
        )

        return conn
    except(Exception, pg.Error) as error:
        print("Error: ", error)