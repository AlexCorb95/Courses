from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy import create_engine

connection_string = f"mysql+pymysql://{'root'}:{'root'}@localhost/new_schema"

# print(connection_string)
eng = create_engine(connection_string)

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(255))
    last_name = Column(String(255))

    def __repr__(self):
        return f"<Student #{self.id} {self.first_name} {self.last_name}>"


class Lockers(Base):
    __tablename__ = "lockers"
    number = Column(Integer, primary_key=True, autoincrement=True)
    student = Column(Integer, ForeignKey(Student.id), primary_key=True)

    def __repr__(self):
        return f"<Lockers {self.number}: {self.student}>"


class Address(Base):
    __tablename__ = "address"
    student = Column(Integer, ForeignKey(Student.id), primary_key=True)
    street_name = Column(String(255))
    number = Column(Integer)
    city = Column(String(255))

    def __repr__(self):
        return f"<Address #{self.city} {self.street_name} {self.number}:{self.student}>"


Base.metadata.create_all(eng)
