# class Rectangle:
#
#     def __init__(self, latime, lungime):
#         self.latime = latime
#         self.lungime = lungime
#
#     def area(self):
#         return self.latime * self.lungime
#
#
# a = Rectangle(2, 3)
# print(a.latime)
# print(a.lungime)
# print(a)
# a.latime = 4
#
# print(a.area())

from dataclasses import dataclass


class Figure:
    pass


class Rectangle(Figure):

    def __init__(self, a, b):
        self.a = a
        self.b = b

@dataclass
class Rectangle(Figure):
    a: int
    b: int

    def circuit(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b

    # def __repr__(self):
    #     return f"Rectangle(a={self.a}, b={self.b})"
    #
    # def __eq__(self, other):
    #     return isinstance(other, Rectangle) and (self.a, self. b) == (other.a, other.b)


class Rectangle2(Figure):

    def __init__(self, a, b):
        self.a = a
        self.b = b


@dataclass
class Rectangle(Figure):
    a: int
    b: int

    def circuit(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b

    def __repr__(self):
        return f"Rectangle(a={self.a}, b={self.b})"

    def __eq__(self, other):
        return isinstance(other, Rectangle) and (self.a, self. b) == (other.a, other.b)


a = Rectangle(2, 3)
b = Rectangle(2, 8)
c = Rectangle(2, 3)
# d = Rectangle2(2, 3)
# print(a.__eq__(b))
# print(a.__eq__(c))
# print(a.__eq__(d))
print(isinstance(a, Rectangle))
print(isinstance(a, Rectangle2))
print(isinstance(a, Figure))
