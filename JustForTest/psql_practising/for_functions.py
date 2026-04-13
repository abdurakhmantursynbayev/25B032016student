import psycopg2
with open("functions.sql", "r", encoding = "utf-8") as f:
    funct = f.read()

part_id = int(input())
try:
    conn = psycopg2.connect( host = "localhost", dbname = "pp2_db", user = "admin", password = "12345678")
    with conn.cursor() as cur:
        cur.execute(funct)
    with conn.cursor() as cur:
        cur.execute(
            "select * from get_vendors_for_part(%s)",
            (part_id, )
        )
        print(cur.fetchall())

except Exception as e:
    print(e)
finally:
    conn.close()