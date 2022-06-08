import csv

import pymysql
# with open ('london-bikes.csv') as csv_file:
import datetime

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="example"
)
with connection.cursor() as c:
    c.execute(
        "create table if not exists `bikesharing`"
        '('
        'tstamp timestamp,'
        'cnt integer,'
        'temperature decimal(5,2),'
        'temperature_feels decimal (5,2),'
        'humidity decimal (4,1),'
        'wind_speed decimal(5,2),'
        'weather_code integer,'
        'is_holiday boolean,'
        'is_weekend boolean,'
        'season integer'
        ');'
    )
    connection.commit()
connection.close()

