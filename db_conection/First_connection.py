import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database=""
)
with connection.cursor() as c:
    c.execute("SELECT VERSION()")
    c.execute("CREATE SCHEMA IF NOT EXISTS `` DEFAULT CHARACTER SET utf8;")
    version= c.fetchone()
    print(f"Database version: {version[0]}")
c.close()