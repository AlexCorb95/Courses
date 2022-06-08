import pymysql
# =============================CREATE DB=====================
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database=""
)
with connection.cursor() as c:
    c.execute("CREATE SCHEMA IF NOT EXISTS `example` DEFAULT CHARACTER SET utf8;")
connection.close()

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database=""
)
connection.close()
# ==========================CREATE TABLE============

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="example"
)

with connection.cursor() as c:
    c.execute("CREATE TABLE IF NOT EXISTS `example3`(a integer, b varchar(255));")
    a=int(input("Please provide a integar value for a:"))
    b = input("Please provide value for b: ")[:254]
    c.execute("INSERT INTO `example3` (a,b) VALUES (%s,%s);",(a,b))
    connection.commit()
connection.close()
