import json
import psycopg2

username = 'Zemlyanuy_Daniel'
password = 'postgres'
database = 'Laboratory5'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

data = {}
with conn:

    cur = conn.cursor()

    for table in ('person', 'video', 'device'):
        cur.execute('SELECT * FROM ' + table)
        rows = []
        fields = [x[0] for x in cur.description]

        for row in cur:
            rows.append(dict(zip(fields, row)))

        data[table] = rows

with open('Zemlyanuy_DB.json', 'w') as outf:
    json.dump(data, outf, default=str)