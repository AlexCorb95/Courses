import dataclasses
from heapq import heappop, heappush


def heap_sort(array):
    heap = []
    for element in array:
        heappush(heap, element)

    ordered = []

    # While we have elements left in the heap
    while heap:
        ordered.append(heappop(heap))

    return ordered


# array = [13, 21, 15, 5, 26, 4, 17, 18, 24, 2]
# print(heap_sort(array))


# @dataclasses
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"Name {self.name} and age {self.age}"
    def __lt__(self, other):
        return  other.__gt__(self)

    def __gt__(self, other):
        return self.age > other.age

    def __eq__(self, other):
        return self.age == other.age

    def __ne__(self, other):
        return not self.__eq__(self)


pers1=Person("Alex",28)
pers2=Person("Ciprian",36)
pers3=Person("Radu",14)
pers4=Person("Stefan",32)
pers5=Person("Silviu",30)

array=[pers1,pers2,pers3,pers4,pers5]

for person in heap_sort(array):
    print(person)

print(heap_sort(array))