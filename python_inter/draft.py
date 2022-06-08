# class Impartire:
#     def __init__(self, deimpartit, impartitor):
#         self.__deimpartit = deimpartit
#         self.__impartitor = impartitor
#
#     def calculeaza(self):
#         return self.__deimpartit / self.__impartitor
#
#     def get_deimpartit(self):
#         return self.__deimpartit
#
#     def set_deimpartit(self, val):
#         self.__deimpartit = val
#
#     def get_impartitor(self):
#         return self.__impartitor
#
#     def set_impartitor(self, val):
#         if val == 0:
#             raise ValueError("Valoarea impartitorului trebuie sa fie mereu diferita de zero")
#         self.__impartitor = val
#
#
# obj = Impartire(12, 3)
# print(obj.calculeaza())
# print(obj.get_deimpartit())
# print(obj.get_impartitor())
# obj.set_impartitor(2)
# print(obj.calculeaza())
# obj.set_impartitor(0)
# print(obj.calculeaza())

# ===============================================================================================
import abc  # abc means Abstract Base Classes


class Animal(abc.ABC):

    @abc.abstractmethod
    def deplasare(self):
        pass

    def habitat(self):
        print("Animalele traiesc in natura")


class Veverita(Animal):

    def __init__(self):
        pass

    def deplasare(self):
        print("Veverita alearga si topaie")


# class Caine(Animal):
#     def __init__(self):
#         pass


vev = Veverita()
vev.habitat()
vev.deplasare()
print(vev.deplasare())
# can = Caine()

def test():
    print("Test")
test()
print(test())



# class Animal:
#     def deplasare(self):
#         pass
#
#
# class Cocor(Animal):
#     def deplasare(self):
#         print("Cocorul zboara")


# class Animal:
#     def deplasare(self):
#         print("Animalul merge intr-un mod generic")
#
#
# class Cocor(Animal):
#     def deplasare(self):
#         print("Cocorul zboara")
#
#
# animal = Animal()
# cocor = Cocor()
# #
# lista_vietati = [animal, cocor]
#
# for vietate in lista_vietati:
#     vietate.deplasare()
# class Adunare:
#     def executa(self, x, y, z=0):
#         return float(x) + float(y) + float(z)
#
#
# obj = Adunare()
# print(obj.executa(4, 7, 8))
# print(obj.executa("7", "5", "1"))
# print(obj.executa(2, 3))
#
# print(obj)
# print(2)
# print("dadasdadas")
