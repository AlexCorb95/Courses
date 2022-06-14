import pymysql

movies = [('The Shawshank Redemption', 1994, 'Drama', 1, 8),
          ('The Green Mile', 1999, 'Drama', 1, 6), ('The Godfather', 1972, 'Crime', 2, 7),
          ('The Godfather III', 1990, 'Crime', 2, 6), ('Pulp Fiction', 1994, 'Crime', 3, 9),
          ('Inglourious Basterds', 2009, 'War', 3, 8), ('The Dark Knight', 2008, 'Action', 4, 9),
          ('Interstellar', 2014, 'Sci-fi', 4, 8), ('The Prestige', 2006, 'Drama', 4, 10),
          ('Fight Club', 1999, 'Drama', 5, 7), ('Zodiac', 2007, 'Crime', 5, 5),
          ('Seven', 1995, 'Drama', 5, 8), ('Alien 3', 1992, 'Horror', 5, 5)]

directors = [('Frank', 'Darabont', 7),
             ('Francis Ford', 'Coppola', 8),
             ('Quentin', 'Tarantino', 10),
             ('Christopher', 'Nolan', 9),
             ('David', 'Fincher', 7)]

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="cinematic"
)
with connection.cursor() as c:
    # # ===================creat db cinematic===============
    # c.execute("CREATE SCHEMA IF NOT EXISTS `cinematic` DEFAULT CHARACTER SET utf8;")
    # # =============Creat doua tabele:(directors,movies)===========
    c.execute("CREATE TABLE IF NOT EXISTS `directors`("
              "director_id int PRIMARY KEY AUTO_INCREMENT,"
              "name VARCHAR(25),"
              "surname VARCHAR(25), "
              "rating int);")
    c.execute("CREATE TABLE IF NOT EXISTS `movies`("
              "movies_id int PRIMARY KEY AUTO_INCREMENT,"
              "title VARCHAR(25),"
              "year int,"
              "category VARCHAR(25),"
              "director_id int ,"
              "rating VARCHAR(25),"
              "FOREIGN KEY (director_id) REFERENCES directors(director_id));")
    # # ==================populare tabele============
    # for elem in directors:
    #     c.execute("INSERT INTO `directors` (name,surname,rating) VALUES (%s,%s,%s);",elem)
    #     connection.commit()
    # for elem in movies:
    #
    #     c.execute("INSERT INTO `movies` (title,year,category,director_id,rating) VALUES (%s,%s,%s,%s,%s);",elem)
    #     connection.commit()
    # ========================data manipulation=============
    c.execute("SELECT * FROM `movies` WHERE year>=2002;")
    m=c.fetchall()
    movies=[elem[1]+'('+str(elem[2])+')' for elem in m]
    print(f"Movie after 2002 :{movies}")
    # =======================Delete tabels========
    # c.execute("DROP TABLE `movies`;")
    # c.execute("DROP TABLE `directors`;")
connection.close()
