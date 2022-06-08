class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"


class Employee(Person):
    def __init__(self, name, age, rate, working_hours):
        Person.__init__(self, name, age)
        self.rate = rate
        self.working_hours = working_hours

    def show_finance(self):
        return self.rate * self.working_hours


e = Employee("Ionut", 25, 50, 168)
print(e.show_finance())
print(e)


class Student(Person):
    def __init__(self, name, age, scholarship):
        Person.__init__(self, name, age)
        self.scholarship = scholarship

    def show_finance(self):
        return self.scholarship


class WorkingStudent(Employee, Student):
    def __init__(self, name, age, rate, working_hours, scholarship):
        super().__init__(name, age, rate, working_hours)
        super().__init__(name, age, scholarship)

    def show_finance(self):
        return self.rate * self.working_hours + self.scholarship


os1 = Person("Henry", 54)
os2 = Employee("Jack", 36, 20, 160)
os3 = Student("Agatha", 22, 1000)
os4 = WorkingStudent("Cata", 21, 30, 80, 1000)
print(os1)
print(os2)
print(os3)
# print(os4.scholarship)
print(os4)
print(os4.show_finance())

#
# class Student(Person):
#     def __init__(self, name, age, scholarship):
#         if self.is_name_correct(name):
#             Person.__init__(self, name, age)
#             self.scholarship = scholarship
#
#     def show_finance(self):
#         return self.scholarship
#
#     @classmethod
#     def create_from_string(cls, sentence):
#         name, age, scholarship = sentence.split()
#         age, scholarship = int(age), float(scholarship)
#         if cls.is_name_correct(name):
#             return cls(name, age, scholarship)
#
#     @staticmethod
#     def is_name_correct(name):
#         if name[0].isupper() and len(name) > 3:
#             return True
#         return False
#
#
# stud1 = Student("Marcela", 29, 60)
# # print(stud1)
# stud2 = Student.create_from_string("John 21 6000")
# # print(stud2)
#
# a = Student.create_from_string("John 21 6000")
# b_classic_method = stud1.show_finance()
# b_class_method = stud1.create_from_string("John 21 6000")
# b_static_method = stud1.is_name_correct("Alex")
# print(b_classic_method, b_class_method, b_static_method)


