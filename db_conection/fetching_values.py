import pymysql


connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="example"
)
# =============================== 1.fetch total sum of new shares by season ========================
# with connection.cursor() as c:
#     c.execute(
#         "SELECT cnt,season from bikesharing"
#     )
#     s1=0
#     s2=0
#     s3=0
#     s4=0
#     # c.fetchall()
#     for item in c.fetchall():
#         if item[1] == 0:
#             s1+=item[0]
#         elif item[1] == 1:
#             s2+=item[0]
#         elif item[1] == 2:
#             s3+=item[0]
#         elif item[1] == 3:
#             s4+=item[0]
#
#
#     print(f'season 1 {s1},season 2 {s2},season 3 {s3},season 4 {s4}')
# connection.close()

# ================================== 1.2.fetch total sum of new shares by season ===================
# with connection.cursor() as c:
#     c.execute(
#         "SELECT sum(cnt),season from bikesharing group by season order by season;"
#     )
#     results=c.fetchall()
#     for i in results:
#         print(f'For season {i[1]} we got {i[0]} shares')
#     print(c.fetchall())
# connection.close()

# ================================== 2.fetch total sum of new shares during thunderstorms =======================
# with connection.cursor() as c:
#     weather_code=int(input("Enter a weather code from 0-3:"))
#     c.execute(
#         "SELECT sum(cnt),weather_code from bikesharing where weather_code = %s;",weather_code
#     )
#     results=c.fetchone()
#     print(f'Number of shares is {results[0]} during weather code {results[1]} ')
# connection.close()
# # ================================ 3. fetch the date and hour with the most new shares =====================
# with connection.cursor() as c:
#     c.execute(
#         "SELECT sum(cnt),tstamp from bikesharing group by tstamp order by sum(cnt) desc;"
#     )
#     results=c.fetchone()
#     print(f'Moste shares where {results[0]} on {results[1]}')
# connection.close()

# =================================== 4.How many entries with thunderstorms(weather code 3) we have for year 2016=========
# with connection.cursor() as c:
#     c.execute(
#         "SELECT count(tstamp),weather_code from bikesharing where year(tstamp)=2016 and weather_code=3;"
#     )
#     results=c.fetchone()
#     print(f'Number of shares during weather code {results[1]} were {results[0]}')
# connection.close()
# ========5. update cnt and increment with 10
# with connection.cursor() as c:
#     c.execute(
#         "update bikesharing set cnt = cnt + 10 where date(tstamp)= '2015-01-09';"
#     )
#     connection.commit()
# connection.close()

# ==================6 delete entries from 2017-01-03
# with connection.cursor() as c:
#     c.execute(
#         "delete from bikesharing where date(tstamp)= '2017-01-03';"
#     )
#     connection.commit()
# connection.close()