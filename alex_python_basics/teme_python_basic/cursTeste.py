#                                        Make loops as long as n is less than 5
# n = 0
# while n < 5:
#     n += 1  # increment n with each loop loop
#     if n == 4:  # if n is 4, end the loop
#         break
#     if n == 1:  # if n is 1, start a new iteration
#         continue
# print(n)
#

#                                            sa se afiseze numerele pare 0-20
# x = 0
# while x <= 20:
#     x += 1
#     if x % 2 == 0:
#         print(f"numar par {x}")
#


#                                  sa se afiseze toate numerele care nu sunt divizibile cu 7

# n = 0
# while n <= 100:
#     if n % 7 == 0:
#         print(f"Numar nediv cu 7 {n}")
#     n += 1
#                                           sirul lui fibonaci pana la 100

# a = 0
# b = 1
# while b <= 100:
#     c = a + b
#     a = b
#     b = c
#     print(a)

#                           Fiind date 2 string-uri, stergeti din al doilea string toate literele care se regasesc in primul.(WHILE)

# a = """The Fibonacci numbers were first described in Indian mathematics,[2][3][4] as early as 200 BC in work by Pingala on enumerating possible patterns of Sanskrit poetry formed from syllables of two lengths. They are named after the Italian mathematician Leonardo of Pisa, later known as Fibonacci, who introduced the sequence to Western European mathematics in his 1202 book Liber Abaci.[5]Fibonacci numbers appear unexpectedly often in mathematics, so much so that there is an entire journal dedicated to their study, the Fibonacci Quarterly. Applications of Fibonacci numbers include computer algorithms such as the Fibonacci search technique and the Fibonacci heap data structure, and graphs called Fibonacci cubes used for interconnecting parallel and distributed systems. They also appear in biological settings, such as branching in trees, the arrangement of leaves on a stem, the fruit sprouts of a pineapple, the flowering of an artichoke, an uncurling fern, and the arrangement of a pine cone's bracts"""
# b = "ci,"
# # text= text.replace("c"," ",-1)
# # text= text.replace("C"," ",-1)
# # text= text.replace("I"," ",-1)
# # text= text.replace("i"," ",-1)
# # print(text)
# index = 0
# while index < len(b):
#     caracter = a[index]
#     a = a.replace(caracter, " ")
#     a = a.replace(caracter.upper(), " ")
#     index += 1
#
# print(a)
#
#
#
#
#                           Fiind date 2 string-uri, stergeti din al doilea string toate literele care se regasesc in primul.(FOR)
# a = """The Fibonacci numbers were first described in Indian mathematics,[2][3][4] as early as 200 BC in work by Pingala on enumerating possible patterns of Sanskrit poetry formed from syllables of two lengths. They are named after the Italian mathematician Leonardo of Pisa, later known as Fibonacci, who introduced the sequence to Western European mathematics in his 1202 book Liber Abaci.[5]Fibonacci numbers appear unexpectedly often in mathematics, so much so that there is an entire journal dedicated to their study, the Fibonacci Quarterly. Applications of Fibonacci numbers include computer algorithms such as the Fibonacci search technique and the Fibonacci heap data structure, and graphs called Fibonacci cubes used for interconnecting parallel and distributed systems. They also appear in biological settings, such as branching in trees, the arrangement of leaves on a stem, the fruit sprouts of a pineapple, the flowering of an artichoke, an uncurling fern, and the arrangement of a pine cone's bracts"""
# b = "ci,"
# index = 0
# for caracter in b:
#     a = a.replace(caracter, " ")
#     a = a.replace(caracter.upper(), " ")
# print(a)
# Ask the user to enter data and write it out
# print("Welcome.")
# user_name = input("Enter your name: ")
# print(f"Hello, {user_name}! ")
# print(type(user_name))
#
# cantitate = input("Enter your quantity: ")
# #print(int(cantitate)*2)
# total = int(cantitate) * 2
# print(total)
#                                       Add a sys library to the program to help you read the parameters you specify() introduci din terminal
# import sys
#
# # print(f"Program: {sys.argv[0]}")
# # print(f"First argument: {sys.argv[1]}")
# # print(f"Second argument: {sys.argv[2]}")\
# print(sys.argv)
#


#                   Fiind data lista [1, 5, 7, 2, 7, 3, 9, 6, 3, 7, 8, 4, 2], sa se elimine duplicatele.

# lista = [1, 5, 7, 2, 7, 3, 9, 6, 3, 7, 8, 4, 2]
# set_=set(lista)
# print(lista)
# print(set_)


#                                   fiind data o tupla sa se calculeze mediaq aritmetica


# tupla_elem = 2, 3, 4, 5, 6, 7, 8, 9
# count = len(tupla_elem)
# print(count)
# suma = sum(tupla_elem)
# media = suma / count
# print(media)


#                   fiind dat un dictionar cu perechi sa se afle cine are cea mai mare nota

# catalog = {
#     "Elev1": 9,
#     "Elev2": 7,
#     "Elev8": 10,
#     "Elev3": 6,
#     "Elev4": 5,
#     "Elev5": 10
# }
# # comparam
# lista_note = catalog.values()
# final = max(lista_note)
# for key in catalog:
#     if catalog[key] == final:
#         print(key, final)
# # print(final)
#                                Se se verifice daca un numar este palindrom (ex: 11233211)

# numar=123
# numar = 1122332211
# numar_txt = str(numar)
# #   lista = list(numar_txt)
# numar_txt_intors = numar_txt[::-1]
# if numar_txt_intors == numar_txt:
#     print(f"{numar} este palindrom")

# numar = 123
# # numar = 11233211
# numar_txt = str(numar)
# numar_txt_intors = numar_txt[::-1]
# print(numar_txt == numar_txt_intors)

# #       fiind date doua liste cu elemente sa se afiseze toate perechile de elem posibile din combinarea celor 2 liste
#
# list1 = [1, 2, 3, 4, 5, 67, 8, 98, 678, 96]
# list2 = [2, 3, 4, 56, 7, 8, 987, 789, 7]
# lista3 = []
# for element in list1:
#     for elem in list2:
#         x = (element, elem)
#         lista3.append(x)
# print(lista3)

#                            Sa se afiseze primele 20 de numere prime

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 123, 1233, 42, 53, 213, 312, 221, 33, 12, 44, 17, 22, 42, 44, 32, 78, 81, 83,
#          33]

# numar = 2
# count = 0
# lista = []
# while count < 100:
#     prim = True
#     for divizor in range(2, int(numar ** 1 / 2)):
#         if numar % divizor == 0:
#             prim = False
#         # print("numarul nu este prim")
#     if prim:
#         count += 1
#         lista.append(numar)
#     numar += 1
#
# print(lista)
#


# Fiind date numere romane sa se transforme in arabe
# numar_roman = "LX"
# numar = 0
# dic_cor = {"L": 50, "X": 10, "V": 5, "I": 1}
# first_numeral = numar_roman[0]
# numar += dic_cor[first_numeral]
# for numeral in numar_roman:
#     if first_numeral >= numeral:
#         numar += dic_cor[numeral]
#     else:
#         numar = dic_cor[numeral] - numar
#
#
# print(numar)
# # tradus din rom in arab
# numar_roman = "L"
# numar = 0
# dic_cor = {"L": 50, "X": 10, "V": 5, "I": 1}
# index_n = 0
# numar_arab = 0
# lenghtListaTradusa = 0
# # creeaza o lista cu caracterele romane separate
#
# lista = list(numar_roman)
# print(lista)
#
# # creeaza o lista cu caracterele romane traduse
#
# lista_tr = list()
# lenghtListaTradusa = len(numar_roman)
# print(lenghtListaTradusa)
# for index in lista:
#     numar = dic_cor[index]
#     lista_tr.append(numar)
# print(lista_tr)
#
# # luam indexul cel mai mic cu val cea mai mare
# biggestNumber = max(lista_tr)
# numar_arab = biggestNumber
# # print(biggestNumber)
# # comparam indexul la nr mare cu restu indexilor daca e mai mic scadem daca e mai mare adunam
#
# while index_n < lista_tr.index(biggestNumber):
#     numar_arab = numar_arab - lista_tr[index_n]
#     index_n += 1
# print(numar_arab)
# index_n +=1
# print(index_n)
# while lista_tr.index(biggestNumber) < index_n < lenghtListaTradusa:
#     numar_arab = numar_arab + lista_tr[index_n]
#     index_n += 1
# print(numar_arab)
#
# # # numbers = []
# # # for i in range(1000):
# #     numbers.append(i)
# # print(len(numbers))  # Prints 1000
# numbers = [i+15 for i in range(1000)]
# print(numbers)  # Prints 1000
# #patratele numerelor pana la 100
# numbers = [i**2 for i in range(101)]
# print(numbers)

# def media_aritmetica(a, b, c):
#     average = (a + b + c) / 3
#     return average


# print(media_aritmetica(2, 3, 5))
# print(media_aritmetica(8, 10, 10))
# sa se faca media aritmetica a numerelor dintr-o lista


# def media_aritmetica(lista_numere):
#     average = sum(lista_numere) / len(lista_numere)
#     return average
#
#
# lista_numere = [1, 2, 3, 4, 5, 6, 7, 8, 200]
# print(media_aritmetica(lista_numere))

# def media_aritmetica_args(*args):
#     average = sum(args) / len(args)
#     return average
#
#
# print(media_aritmetica_args(1, 3, 5, 7))
# Add any number of ingredients
# def add_ingredients(**kwargs):
#     result = 0
#     for key in kwargs:
#         result += kwargs[key]
#     return result
#
#
# print(add_ingredients(eggs=3, spam=5, cheese=2))


# sa se faca functia care ne afiseaza fiecare pereche/cheie/valoare din kwargs pe un rand separat

# def print_ingredients(**legume):
#     for leguma in legume:
#         print(leguma, legume[leguma])
#     # print(legume)
#
#
# print_ingredients(eggs=3, spam=5, cheese=2)
# Add any number of ingredients
# def add_ingredients(*args, **kwargs):
#     result = 0
#     for arg in args:
#         result += arg
#     for key in kwargs:
#         result += kwargs[key]
#     return result
#
#
# print(add_ingredients(1, 2, 3, eggs=3, spam=5, cheese=2))  # Will print 16
# # 1. Scrieti o functie care intoarce un dictionar cu numarul de aparitii al fiecarui caracter dintr-un string dat ca parametru, ignorand litere mici/mari.
# # Ex: pentru "Python the Basics", vom avea {'p':1, 'y':1, 't':2,'h':2, ...}
# def litere_count(text):
#     result = {}
#     for letter in text:
#         result[letter] = text.count(letter)
#     return result
#
#
# print(litere_count("python the basics"))
#
#
def aparitie_dict_comprihansion(text="python the basics"):
    result = {letter: text.count(letter) for letter in text}
    return result


print(aparitie_dict_comprihansion())
#
# # 1. Scrieti un algoritm care transforma un string in forma lui L33t. Adica inlocuieste caracterele
# # E/e -> 3
# # i/I -> 1
# # O/o -> 0
# # A/a -> 4
# # S/s -> 5
# # T/t -> 7
#
# # 2. Scrieti o functie care transforma un titlu in forma lui URL:
# # - diacriticele devin variantele lor fara diacritice
# # - literele mari devin litere mici,
# # - spatiile devin minus-uri
# # - Eliminam caracterele non-alfanumerice, exceptand _, @, !, $, ;, %
# proof of concept command line application

# def interpret_command(command):
#     if command == '3':
#         print("Running tests...")
#
#
# def afisare_meniu():
#     print("0. Iesire...")
#     print("1. Adaugare...")
#     print("2. Stergere...")
#     print("3. Testare...")
#
#
# afisare_meniu()
# command = input("Intorduceti o comanda: ")
# while command != '0':
#     interpret_command(command)
#     afisare_meniu()
#     command = input("Intorduceti o comanda: ")