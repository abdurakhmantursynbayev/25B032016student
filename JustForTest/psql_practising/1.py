import psycopg2
conn = psycopg2.connect(
    host = "localhost",
    database = "pp2_db",
    user = "admin",
    password = "12345678"
)