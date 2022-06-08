# tradus din rom in arab
numar_roman = "XLIV"
numar = 0
dic_cor = {"L": 50, "X": 10, "V": 5, "I": 1}
index_n = 0
numar_arab = 0
lenght_lista_tradusa = 0
# creeaza o lista cu caracterele romane separate

lista = list(numar_roman)
print(lista)

# creeaza o lista cu caracterele romane traduse

lista_tr = list()
lenght_lista_tradusa = len(numar_roman)
print(lenght_lista_tradusa)
for index in lista:
    numar = dic_cor[index]
    lista_tr.append(numar)
print(lista_tr)

# luam indexul cel mai mic cu val cea mai mare
biggest_number = max(lista_tr)
numar_arab = biggest_number
# print(biggestNumber)
# comparam indexul la nr mare cu restu indexilor daca e mai mic scadem daca e mai mare adunam

while index_n < lista_tr.index(biggest_number):
    numar_arab = numar_arab - lista_tr[index_n]
    index_n += 1
print(numar_arab)
index_n += 1
print(index_n)

# for index_n in range(lenght_lista_tradusa):
#     if lista_tr[index_n] <

while lista_tr.index(biggest_number) < index_n < lenght_lista_tradusa:
    if len(lista_tr) > (index_n + 1) and lista_tr[index_n] >= lista_tr[index_n + 1]:
        numar_arab = numar_arab + lista_tr[index_n]
    else:
        numar_arab = numar_arab - lista_tr[index_n]
    index_n += 1
print(numar_arab)
