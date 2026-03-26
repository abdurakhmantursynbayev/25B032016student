import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    dbname = "pp2_db",
    user = "admin",
    password = "12345678"
)

cur = conn.cursor()
cur.execute("select version();")
print(cur.fetchone())

cur.close()
conn.close()