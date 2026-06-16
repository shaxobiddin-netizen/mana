import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

with psycopg2.connect(
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_DATABASE'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD')
) as conn:

    with conn.cursor() as cur:

        cur.execute("SELECT * FROM users")
rows = cur.fetchall()

for row in rows:
    print(f"ID: {row[0]} | Ism: {row[1]} | Maosh: {row[2]}")

query = "SELECT id, ism, maosh FROM xodimlar WHERE maosh > %s"
cur.execute(query, (7000000,))

row = cur.fetchone()

if row:
    print(f"ID: {row[0]} | Ism: {row[1]} | Maosh: {row[2]}")
else:
    print("Natija topilmadi")

cur.close()
conn.close()