import psycopg2
import os

path = './Anomaly_new 1.txt'

conn = psycopg2.connect(
    dbname=os.environ.get('DB_NAME'),
    user=os.environ.get('DB_USER'),
    password=os.environ.get('DB_PASSWORD'),
    host=os.environ.get('DB_HOST'),
    port=os.environ.get('DB_PORT')
)

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

query= f'CREATE TABLE "TASKS" (\n ' + ",\n ".join(fields) + "\n);"

cur = conn.cursor()
try:
    cur.execute(query)
    conn.commit()
except Exception as e:
    print(e)
finally:
    cur.close()
    conn.close()