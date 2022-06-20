from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy import create_engine, select, or_, and_, text
from sqlalchemy.orm import sessionmaker

connectio_string = f"mysql+pymysql://{'root'}:{'root'}@{'localhost'}/{'example'}"

eng = create_engine(connectio_string)

Base = declarative_base()


class Directors(Base):
    __tablename__ = "table_directors"
    director_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    surname = Column(String(255))
    rating = Column(Integer)

    def __repr__(self):
        return f"<Directors #{self.director_id} {self.name} {self.surname} {self.rating}>"


class Movies(Base):
    __tablename__ = "table_movies"
    movie_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50))
    year = Column(Integer)
    category = Column(String(50))
    director_id = Column(ForeignKey(Directors.director_id))
    rating = Column(Integer)

    def __repr__(self):
        return f"<Movies #{self.movie_id} {self.title} {self.year} {self.category} {self.rating}>"


Base.metadata.create_all(eng)

Session = sessionmaker(bind=eng)

directors = [{'name': 'Frank', 'surname': 'Darabont', 'rating': 7},
             {'name': 'Francis Ford', 'surname': 'Coppola', 'rating': 8},
             {'name': 'Quentin', 'surname': 'Tarantino', 'rating': 10},
             {'name': 'Christopher', 'surname': 'Nolan', 'rating': 9},
             {'name': 'David', 'surname': 'Fincher', 'rating': 7}]
movies = [{'title': 'The Shawshank Redemption', 'year': 1994, 'category': 'Drama', 'director_id': 1, 'rating': 8},
          {'title': 'The Green Mile', 'year': 1999, 'category': 'Drama', 'director_id': 1, 'rating': 6},
          {'title': 'The Godfather', 'year': 1972, 'category': 'Crime', 'director_id': 2, 'rating': 7},
          {'title': 'The Godfather III', 'year': 1990, 'category': 'Crime', 'director_id': 2, 'rating': 6},
          {'title': 'Pulp Fiction', 'year': 1994, 'category': 'Crime', 'director_id': 3, 'rating': 9},
          {'title': 'Inglourious Basterds', 'year': 2009, 'category': 'War', 'director_id': 3, 'rating': 8},
          {'title': 'The Dark Knight', 'year': 2008, 'category': 'Action', 'director_id': 4, 'rating': 9},
          {'title': 'Interstellar', 'year': 2014, 'category': 'Sci-fi', 'director_id': 4, 'rating': 8},
          {'title': 'The Prestige', 'year': 2006, 'category': 'Drama', 'director_id': 4, 'rating': 10},
          {'title': 'Fight Club', 'year': 1999, 'category': 'Drama', 'director_id': 5, 'rating': 7},
          {'title': 'Zodiac', 'year': 2007, 'category': 'Crime', 'director_id': 5, 'rating': 5},
          {'title': 'Seven', 'year': 1995, 'category': 'Drama', 'director_id': 5, 'rating': 8},
          {'title': 'Alien 3', 'year': 1992, 'category': 'Horror', 'director_id': 5, 'rating': 5}]
# directors_objects = [Directors(**director) for director in directors]
# # directors_objects=[Directors(name=director["name"],surname=director["surname"],rating=director["rating"]) for director in directors]
#
# movies_objects=[Movies(**movie) for movie in movies]
#
# with Session.begin() as s:
#     s.add_all(directors_objects)
#     s.add_all(movies_objects)
# ======================TASK 5
# s = Session()
#
# result = s.execute(select(Movies).filter(Movies.category == 'Drama')).scalars().all()
# for movie in result:
#     print(movie)
#
# result = s.query(Movies).filter(Movies.category == 'Drama').all()
# print(result)
# ==========================TASK 6
# s = Session()
# res = s.execute(select(Movies).filter(Movies.category == "Crime", Movies.year > 1994)).scalars().all()
# for elem in res:
#     print(elem)
# res = s.query(Movies).filter(Movies.category == "Crime", Movies.year > 1994).all()
# print(res)
# ==================TASK (extra): filme 2 categorii de filme. Crime,Drama >1994
# s=Session()
# res=s.execute(select(Movies).filter(or_(Movies.category=="Crime",Movies.category=="Drama"),Movies.year>1994)).scalars().all()
# for elem in res:
#     print(elem)
# ====================TASK 7
# s=Session()
# res=s.execute(select(Movies).order_by(Movies.rating>7).filter(Movies.year.between(2000,2010))).scalars().all()
# for elem in res:
#     print(elem)

# res=s.query(Movies).order_by(Movies.rating>7).filter(Movies.year.between(2000,2010)).all()
# for elem in res:
#     print(elem)

# =====================TASK 8

# s=Session()
# res=s.query(Directors).filter(Directors.rating>=6,or_(Directors.name.like("D%"),Directors.name.like("%n"))).all()
# for elem in res:
#     print(elem)
# res=s.execute(select(Directors).filter(Directors.rating>=6,or_(Directors.name.like("D%"),Directors.name.like("%n")))).scalars().all()
# for elem in res:
#     print(elem)

# ===ADVANCED
# ================== TASK 1
# List the names and surnames of all directors whose films were made between 2011 and 2014, and the rating of their films is less than 9. Use query ()

# s = Session()
#
# query = s.query(Directors.name,Directors.surname).join(Movies).filter(Movies.year.between(2011, 2014), Movies.rating < 9)
# res=query.all()
# print(res)

# ================TASK 2
# List the total number of films created for each director, his full name, and the average rating for each director based on the ratings of their films. Use query () and select().
# s=Session()
# rows_movies = s.query(Directors.name, Directors.surname, func.count(Movies.title),
#                                  func.avg(Movies.rating)).join(Movies).group_by(Directors.name).all()
# for r in rows_movies:
#     print(r)
# print('\n')
#
# query = select([Directors.name, Directors.surname, func.count(Movies.title), func.avg(Movies.rating)]).join(
#     Movies).group_by(Directors.name)
# res = s.execute(query)
# for i in res:
#     print(i)
# =================TASK 3 works with task 1
# print(query.statement)
# print(query.statement.compile(eng,compile_kwargs=dict(literal_binds=True)))
# =====================TASK 4
# ====== var 1
# s = Session()
# stmt = text("SELECT table_directors.name, table_directors.surname "
#             "FROM table_directors JOIN table_movies ON table_directors.director_id = table_movies.director_id "
#             "WHERE table_movies.year BETWEEN :year_1 AND :year_2 AND table_movies.rating < :rating_1;")
#
# res = s.execute(stmt,{"year_1":2000, "year_2":2014, "rating_1":9}).fetchall()
# print(res)
# ===== var 2
# s = Session()
# stmt = text("SELECT table_directors.name, table_directors.surname "
#             "FROM table_directors JOIN table_movies ON table_directors.director_id = table_movies.director_id "
#             "WHERE table_movies.year BETWEEN :year_1 AND :year_2 AND table_movies.rating < :rating_1")
# stmt = stmt.bindparams(year_1=2001, year_2=2014, rating_1=9)
# resu = s.execute(stmt).fetchall()
# print(resu)
def get_direction_statements(year1=None,year2=None,rating=None):
    s=Session()
    year1=int(input("Select first year:"))
    year2=int(input("Select second year:"))
    rating=int(input("Select movie rating:"))
    query=text("SELECT table_directors.name, table_directors.surname "
            "FROM table_directors JOIN table_movies ON table_directors.director_id = table_movies.director_id "
            "WHERE table_movies.year BETWEEN :year_1 AND :year_2 AND table_movies.rating < :rating_1")
    query=query.bindparams(year_1=year1, year_2=year2, rating_1=rating)
    results=s.execute(query).fetchall()
    return results
x=get_direction_statements()
print(x)