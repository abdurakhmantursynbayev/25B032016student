import psycopg2

conn = psycopg2.connect(
    host="localhost", dbname="pp2_db",
    user="admin", password="12345678"
)
cur = conn.cursor()
books = [
    ("first book", "beko", 100),
    ("second book", "second author", 101),
    ("third book", "third author", 2000)
]

# Always use %s placeholders — NEVER format strings directly (SQL injection risk)
cur.executemany(
    "insert into books(title, author, price) values(%s, %s, %s);",
    books
)

conn.commit()
print("Row inserted.")


cur.close()
conn.close()