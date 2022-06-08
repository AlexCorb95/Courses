"""

1.Sa se scrie o functie care afiseaza un tabel cu 3 coloane, populat cu o lista de tuple de 3 valori.
2.Sa se defineasca o interfata pentru o metoda care sa returneze tupla de 3 valori.
3.Sa se implementeze interfata pe clasele Product: name, description, price si Service: title, description, contact_person.
4.Sa se trimita cate o lista de obiecte din fiecare fel functiei.

"""
import abc


class TabelInterface(abc.ABC):
    @abc.abstractmethod
    def as_tabel_row(self) -> tuple:
        pass


class Product(TabelInterface):
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def as_tabel_row(self) -> tuple:
        return self.name, self.description, self.price


class Service(TabelInterface):
    def __init__(self, title, description, contact_person):
        self.title = title
        self.description = description
        self.contact_person = contact_person

    def as_tabel_row(self) -> tuple:
        return self.title, self.description, self.contact_person, 17


def line_verify (lst,size):
    i=0
    for item in lst:
        if len(item) >  size:

            lst[i]=[item[x:size-1] for x in range(0,len(lst[i]),size) ]

    return lst



def colum_tabel(lista_tuple, row_size=60):
    tuple_length = len(lista_tuple[0].as_tabel_row())
    col_size = (row_size - tuple_length + 1) // tuple_length
    row_size = col_size * tuple_length + tuple_length + 1
    print("-" * row_size)

    for entity in lista_tuple:
        tuple_ = entity.as_tabel_row()
        obj = [str(tuple_[i]).center(col_size) for i in range(len(tuple_))]
        # a=line_verify(obj,col_size)
        lines = 0
        # print(a)

        # for small_obj in obj:
        #     lines = len(small_obj) // col_size

            # print(lines)
            # if len(small_obj)> col_size:
            #     obj.append(" "*col_size)
            # break
        # obj=(lambda i:tuple_[i].center(col_size) for i in range(3) )
        # obj1=str(tuple_[1]).center(col_size)
        # obj2=str(tuple_[2]).center(col_size)

        obj_str = "|" + "|".join(obj) + "|"
        print(f"{obj_str}")

        # print(
        # f"|{str(tuple_[0]).center(col_size)}"
        # f"|{str(tuple_[1]).center(col_size)}"
        # f"|{str(tuple_[2]).center(col_size)}|")
    print("-" * row_size)


if __name__ == '__main__':
    products = [
        Product("Tricou", "Negru", 45),
        Product("Blugi", "Regular-Fit", 80),
        Product("Ochelari", "Polarizati", 45),
        Product("Blugi", "Regular-Fit", 80)
    ]
    services = [
        Service("Retur", "E-Mag", "Ion"),
        Service("Mecanic", "Auto", "Vericu"),
        Service("Instalator", "Sanitar", "Dorel"),
        Service("Mecanic", "Auto", "Vericu")
    ]
    colum_tabel(services)
    colum_tabel(products)
    # colum_tabel([
    #     (1, 2, 3),
    #     (4, 5, 8),
    #     (7, 8, 9)
    # ])
# ==================================================Merge================================================================
# import abc
# from abc import ABC
# from math import ceil
#
#
# class TableInterface(abc.ABC):
#     @abc.abstractmethod
#     def as_table_row(self) -> tuple:
#         pass
#
#
# class Product(TableInterface):
#     def as_table_row(self) -> tuple:
#         return self.name, self.description, self.price
#
#     def __init__(self, name, description, price):
#         self.name = name
#         self.description = description
#         self.price = price
#
#
# class Service(TableInterface):
#     def as_table_row(self) -> tuple:
#         return self.title, self.description, self.contact_person
#
#     def __init__(self, title, description, contact_person):
#         self.title = title
#         self.description = description
#         self.contact_person = contact_person
#
#
# def column_table(list_tuple, row_size=60):
#     col_size: int = int((row_size - 4) / 3)
#     row_size = col_size * 3 + 4
#     print('-' * row_size)
#     for entity in list_tuple:
#         t = entity.as_table_row()
#         obj1 = str(t[0])
#         obj2 = str(t[1])
#         obj3 = str(t[2])
#         lines1 = len(obj1) / col_size
#         lines2 = len(obj2) / col_size
#         lines3 = len(obj3) / col_size
#         lines = ceil(max(lines1, lines2, lines3))
#         for i in range(lines):
#             from_ = i * col_size
#             to_ = (i + 1) * col_size
#             print(
#                 f'|{obj1[from_: to_].center(col_size)}|{obj2[from_: to_].center(col_size)}|{obj3[from_: to_].center(col_size)}|')
#
#     print('-' * row_size)
#
#
# if __name__ == '__main__':
#     products = [Product('tricou', 'alb', 36), Product('sapca', 'rosie', 25.30)]
#     services = [Service('retur', 'gratis', 'Mirela'), Service('probare', 'gratis', 'Ionut'),
#                 Service('garantie',
#                         "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has "
#                         "been the industry's standard dummy text ever since the 1500s, when an unknown printer took a "
#                         "galley of type and scrambled it to make a type specimen book. It has survived not only five"
#                         " centuries, but also the leap into electronic typesetting, remaining essentially unchanged. "
#                         "It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum "
#                         "passages, and more recently with desktop publishing software like Aldus PageMaker including "
#                         "versions of Lorem Ipsum",
#                         'Ana')]
#     column_table(products)
#     column_table(services)