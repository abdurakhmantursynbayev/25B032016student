import psycopg2

conn = psycopg2.connect(
    host = "localhost", dbname = "pp2_db", user = "admin", password = "12345678"
)

cur = conn.cursor()

cur.execute("""
    create table if not exists books(
        id serial primary key,
        title varchar(200) not null,
        author varchar(100) not null,
        price float,
        in_stock boolean default true    
    );

""")
conn.commit()
print("table created")
cur.close()
conn.close()