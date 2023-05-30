
from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()

def connect():
    conn = psycopg2.connect(database=os.environ['POSTGRES_DATABASE'],
                        host=os.environ['POSTGRES_HOST'],
                        user=os.environ['POSTGRES_USER'],
                        password=os.environ['POSTGRES_PASSWORD'],
                        port=os.environ['POSTGRES_PORT'])
    return conn

def init_db():
    conn = connect()
    with conn.cursor() as cursor:
        cursor.execute('CREATE TABLE IF NOT EXISTS noxbackup (username TEXT PRIMARY KEY, data bytea);')
    conn.close()

def get(user: str):
    conn = connect()
    with conn.cursor() as cursor:
        cursor.execute("SELECT data FROM noxbackup WHERE username = %s", (user,))

        result = cursor.fetchone()
        if result:
            return bytes(result[0])
    conn.close()
    return

def save(user: str, data: bytes):
    conn = connect()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO noxbackup VALUES (%s, %s) ON CONFLICT (username) DO UPDATE SET data = EXCLUDED.data", (user, data))
    conn.commit()
    conn.close()