from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__="students"
    id=Column(Integer,primary_key=True,autoincrement=True)
    first_name=Column(String(255))
    last_name=Column(String(255))

    def __str__(self):
        return f"<Student #{self.id} {self.first_name} {self.last_name}>"


# CONNECTION_STRING = "mysql+pymysql://{'root'}:{'root'}@{'localhost'}/{'default'}"
CONNECTION_STRING = "mysql+pymysql://{user}:{password}@{host}/{db}"

eng = create_engine(
    CONNECTION_STRING.format(
        host="localhost",
        user="root",
        password="root",
        db=""
    )
)
Base.metadata.create_all(eng)
