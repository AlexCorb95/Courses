# numar_roman = "XXLXXXIV"
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
# numar_arab = 0
# # print(biggestNumber)
# # comparam indexul la nr mare cu restu indexilor daca e mai mic scadem daca e mai mare adunam
#
# while index_n < lista_tr.index(biggestNumber):
#     # if lista_tr[index_n] < lista_tr[index_n+1]:
#     numar_arab = numar_arab + lista_tr[index_n]
#     # else:
#     #     numar_arab = numar_arab - lista_tr[index_n]
#     index_n += 1
# print(numar_arab)
# index_n +=1
# print(index_n)
# while lista_tr.index(biggestNumber) < index_n+1 < lenghtListaTradusa:
#     # if index_n+1 < lenghtListaTradusa:
#     if lista_tr[index_n] < lista_tr[index_n+1]:
#         numar_arab = numar_arab - lista_tr[index_n]
#     else:
#         numar_arab = numar_arab + lista_tr[index_n]
#     index_n += 1
# print(numar_arab)
# from timeit import timeit
# code=""
# from time import sleep
#
# def method():
#   sleep(1)
#
# method()
# ""
# print(timeit(code,number=1))
import re
sum=0
pattern="back"
if re.match(pattern,"backup.txt"):
 sum+=1
if re.match(pattern,"text.back"):
 sum+=2
if re.search(pattern,"backup.txt"):
 sum+=4
if re.search(pattern,"text.back"):
 sum+=8

print(sum)