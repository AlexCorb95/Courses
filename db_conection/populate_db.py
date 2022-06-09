import csv

import pymysql
import datetime

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="example"
)

with connection.cursor() as c:
    with open('london-bikes.csv') as csv_file:
        for i, line in enumerate(csv_file):
            if i == 0:
                columns = line
                # print(coloms)
                continue
            else:
                values = line.split(",")
                values[0] = datetime.datetime.strptime(values[0], "%Y-%m-%d %H:%M:%S")

                columns_values = ",".join(["%s" for elem in values])
                c.execute(f"insert into `bikesharing`({columns}) values ({columns_values})", values)
            if i % 100 == 0:
                connection.commit()
connection.close()