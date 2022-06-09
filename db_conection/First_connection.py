import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database=""
)
with connection.cursor() as c:
    c.execute("SELECT VERSION()")
    version= c.fetchone()
    c.execute("CREATE SCHEMA IF NOT EXISTS `example1` DEFAULT CHARACTER SET utf8;")
    print(f"Database version: {version[0]}")
    connection.commit()
connection.close()