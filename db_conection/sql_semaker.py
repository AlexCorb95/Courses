from sqlalchemy import create_engine
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from sql_alch import Base, Student,Lockers, Address
from sqlalchemy.sql.functions import func
from sqlalchemy.exc import IntegrityError,InvalidRequestError
CONNECTION_STRING = f"mysql+pymysql://{'root'}:{'root'}@localhost/new_schema"
engine = create_engine(CONNECTION_STRING)
# ======================insert===========
# with Session(engine) as s:
#     s.add_all(
#         [
#             Student(first_name="Mike", last_name="Wazowski"),
#             Student(first_name="Netti", last_name="Nashe"),
#             Student(first_name="Jessamine", last_name="Addison"),
#             Student(first_name="Brena", last_name="Bugdale")
#         ])
#     s.commit()
# ======================select==============
# with Session(engine) as s:
#     rows = s.query(Student).all()
#     for row in rows:
#         print(row)
#     print("***")
#     # 2.x
#     rows = s.execute(select(Student)).scalars().all()
#     for row in rows:
#         print(row)
#
#     print("---")
#     total = s.query(Student).count()
#     print(f"Total: {total}")
#     print("***")
#     # 2x
#     total_ = s.execute(select(func.count(Student.id))).scalar()
#     print(f"Total: {total_}")
#
#     print("---")
#     query_result = s.query(Student).filter(Student.id >= 3, Student.last_name.like("A%"))
#     print("Found students: ")
#     for row in query_result:
#         print(row)
#
#     print("***")
#     query_result = s.execute(select(Student).filter(Student.id >= 3, Student.last_name.like("A%"))).scalars().all()
#     print("Found students: ")
#     for row in query_result:
#         print(row)
# ============================lockers to students===
# with Session(engine) as s:
#     try:
#         s.add_all([
#             Lockers(number=1,student=2),
#             Lockers(number=2,student=1),
#             Lockers(number=3,student=4),
#             Lockers(number=4,student=3)
#         ])
#         s.commit()
#     except IntegrityError:
#         s.rollback()
#         print("Au fost create deja")
#
#     rows = s.query(Student, Lockers).join(Lockers).filter(Lockers.number==4)
#     for row in rows :
#         student,locker=row
#         print(f"Student with locker {locker.number}:{student}")
with Session(engine) as s:
    try:
        s.add_all([
            Address(student=1,street_name="Traian Vuia",number=112,city="Cluj-Napoca"),
            Address(student=2,street_name="Observatorului",number=78,city="Bucuresti"),
            Address(student=3,street_name="Bucium",number=33,city="Iasi"),
            Address(student=4,street_name="Republicii",number=12,city="Barlad")
        ])
    except IntegrityError:
        s.rollback()
        print("A deja adrese")
    rows=s.query(Student,Address).join(Address)
    for row in rows:
        student,address=row
        print(row)