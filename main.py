import time
import psycopg2
import os
from dotenv import load_dotenv

path = './Anomaly_new 1.txt'

load_dotenv()

db_params = {
    "dbname":os.getenv('DB_NAME'),
    "user":os.getenv('DB_USER'),
    "password":os.getenv('DB_PASSWORD'),
    "host":os.getenv('DB_HOST'),
    "port":os.getenv('DB_PORT')
}

def wait_for_db():
    for attempt in range(3):
        try:
            connession = psycopg2.connect(**db_params)
            print("Connesso al postresql")
            return connession
        except Exception as err:
            print(err)
            time.sleep(3)
    raise Exception("Impossibile connettersi")

conn = wait_for_db()

_type =  {
    "datetime": "TIMESTAMP",
    "integer": "INTEGER",
    "float": "DOUBLE PRECISION"
}

fields = []

with open(path, 'r', encoding='utf-8') as f:
    for riga in f:
        if 'Campo:' in riga:
            parts = riga.strip().split('"')
            name_field = parts[1]
            sql_split = riga.split('(')[-1].replace(')', '').strip()
            sql_type = _type.get(sql_split, "TEXT")
            fields.append(f'"{name_field}" {sql_type}')

query= f'CREATE TABLE IF NOT EXISTS "Anomaly_new" (\n ' + ",\n ".join(fields) + "\n);"

print("Query SQL generata:\n", query)

cur = conn.cursor()
try:
    cur.execute(query)
    conn.commit()
except Exception as e:
    print(e)
finally:
    cur.close()
    conn.close()