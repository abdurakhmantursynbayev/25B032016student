import psycopg2

conn = psycopg2.connect(
    host= "localhost", dbname = "pp2_db",
    user = "admin", password = "12345678"
)
cur = conn.cursor()

cur.execute("""
    create table if not exists students(
        id serial primary key,
        name varchar(100) not null,
        student_id integer unique not null,
        email varchar(100) unique not null,
        grade float,
        enrolled boolean default true,
        created_at timestamp default current_timestamp
    );
""")


cur.execute("""
    create table if not exists enrollments(
        id serial primary key,
        student_id integer references students(student_id) on delete cascade,
        name varchar(100)     
    );
""")
conn.commit()
print("table created")
cur.close()
conn.close()