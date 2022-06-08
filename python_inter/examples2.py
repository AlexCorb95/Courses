# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         value_returned = self.func(a, b)
#         return value_returned ** 2
#
#
# @Power
# def multiply(a, b):
#     return a * b
#
#
# print(multiply(2, 3))
# ===========================================================================================
# DECORATE A CLASS USING A FUNCTION DECORATOR
# def decorator(x):
#     def new_display(self):
#         print(f"The name of the student: {self.name}")
#         print(f"The class subject is Programming")
#
#     x.display = new_display
#     x.another_display = new_display
#     return x
#
#
# @decorator
# class Student:
#     def __init__(self, name):
#         self.name = name
#
#     def display(self):
#         print(f"The name of the student: {self.name}")
#
#
# s1 = Student("Andrei")
# s1.display()
# s1.another_display()

# ===========================================================================================
# DECORATE A CLASS USING A CLASS DECORATOR
class book_decorator:
    def __init__(self, book):
        self.book = book

    def __call__(self, author):
        def new_display(self):
            print(f"The author of the book is: {self.author}")
            print("Title of the book is 'Amintiri din copilarie'")

        self.book.display = new_display
        bookObj = self.book(author)
        return bookObj


@book_decorator
class Book:
    def __init__(self, author):
        self.author = author

    def display(self):
        print(f"The author of the book is: {self.author}")


b1 = Book("Ion Creanga")
b1.display()
