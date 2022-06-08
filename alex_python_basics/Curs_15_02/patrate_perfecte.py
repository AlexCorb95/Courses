# perfect_square=[]
# for numbers in range (1,101):
#     perfect_square.append(numbers**3)
# print(perfect_square)

# perfect_square=[ numbers**3 for numbers in range (1,101) ]
# print(perfect_square)

# 1. Sa se scrie o functie care primeste o lista de numere, si intoarce o lista cu cuburile lor (fiecare numar ridicat la puterea 3)

lista = [11, 2, 5, 4]
cuburi = [i ** 3 for i in lista]
print(cuburi)
