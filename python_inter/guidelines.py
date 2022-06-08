"""
Guidelines:

- o clasa reprezinta o structura logica care defineste starea si comportamentul obiectelor
(dupa ce definim o clasa, ea poata fi utilizata pentru a crea obiecte de tipul respectiv)
- pentru definierea unei clase, in Python, folosim cuvant cheie class, urmat de denumire clasei
- corpul clasei cuprinde instructiuni ce permit definirea membrilor clasei respective
- una dintre cele mai folositoare methode ar fi __init__,
ce foloseste si pentru instantierea obiectelor din clasa respectiva
(aceasta metoda se mai numeste si constructorul clasei)
- initializarea unui obiect este facuta prin sintaxa: obiect = numeClasa()

- variabila self: reprezinta obiectul ceva fi instantiat din clasa respectiva

- atribute de instanta: pentru a crea un atribut de tipul instanta folosim sintaxa
self.nume_atribut = valoare

- atribute de clasa: atributele de clasa vor apartine intregii clase, reprezentand o caracteristica
a intregii clase, pe care toate obiectele si-o vor insusi



"""

class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(M.mro())


# class Animal:
#     def __init__(self, specie):
#         self.specie = specie
#
#     def deplasare(self):
#         print("Animalul se deplaseaza")
#
#
# class Papagal(Animal):
#     def __init__(self, culoare):
#         self.culoare = culoare
#
#     def deplasare(self):
#         print("Papagalul se deplaseaza zburand")
#
#     def deplasare_parinte(self):
#         super().deplasare()
#
#
# p = Papagal("verde")
# a = Animal("catel")
# a.deplasare()
# p.deplasare()
# p.deplasare_parinte()

