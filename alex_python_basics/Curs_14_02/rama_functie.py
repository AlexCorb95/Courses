# print(f'{"*"*3}{" " * 20}{"*"*3}')
# print(f'{"*"*2}{" " * 22}{"*"*2}')
# print(f'{"*"*1}{" " * 24}{"*"*1}')

# i = 6
# prov = i
#
# for i in range(prov, -1, -1):
#     print(f'{"*" * i}{" " * (20 + (prov-i)*2)}{"*" * i}')
#
#
# print(f"{' ' * ((20+prov*2) // 2-2)}{'.' * 4}{' ' * ((20+prov*2) // 2-2)}")
#
# for i in range(0, prov + 1, 1):
#     print(f'{"*" * i}{" " * (20 + (prov-i)*2)}{"*" * i}')
#

def listat_de_rama(i):
    prov = i
    lista = []
    for i in range(prov, -1, -1):
        lista.append(f'{"*" * i}{" " * (20 + (prov - i) * 2)}{"*" * i}')

    lista.append(f"{' ' * ((20 + prov * 2) // 2 - 2)}{'.' * 4}{' ' * ((20 + prov * 2) // 2 - 2)}")

    for i in range(0, prov + 1, 1):
        lista.append(f'{"*" * i}{" " * (20 + (prov - i) * 2)}{"*" * i}')
    return lista


def afisare_lista(lista):
    for row in lista:
        print(row)


lista = listat_de_rama(7)
afisare_lista(lista)
