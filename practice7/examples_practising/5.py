import psycopg2

conn = psycopg2.connect(
    host = "localhost", dbname = "pp2_db", user=  "admin" , password = "12345678"
)
cur = conn.cursor()

cur.execute(
    "update books set price = %s where title = %s;",
    (3000, "second book")
)

conn.commit()
cur.close()
conn.close()