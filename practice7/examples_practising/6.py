import psycopg2

conn = psycopg2.connect(
    host = "localhost", dbname = "pp2_db", user=  "admin" , password = "12345678"
)
cur = conn.cursor()

cur.execute(
    "update books set in_stock = false where price > %s;",
    (40,)
)

cur.execute(
    "update books set price = price * 0.9;"
)

conn.commit()
cur.close()
conn.close()