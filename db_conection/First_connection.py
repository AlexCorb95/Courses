import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="Kjkszpjaezakami1",
    database=""
)
with connection.cursor() as c:
    c.execute("SELECT VERSION()")
    version= c.fetchone()
    print(f"Database version: {version[0]}")
c.close()