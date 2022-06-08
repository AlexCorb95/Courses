# # Sa se verifice daca un numar este divizibil cu 77
#
#
# div = int(input())
# div_rez = div % 77
# div_int = div // 77
# if div_rez == 0:
#     print(f"""{div} este divizibil cu 77
# si este {div_int}""")
# else:
#     print(f"{div}nu este divizibil cu 77")
#
#
#
#
# # Fiind date 3 numere a, b, c, sa se verifice daca sunt pitagoreice
#
#
# aa = int(input())
# bb = int(input())
# cc = int(input())
# suma_ab = (aa ** 2) + (bb ** 2)
# cc2 = cc ** 2
# if suma_ab == cc2:
#     print("Intre a si b este unghi de 90 de grade si sunt pitagoreice")
# else:
#     print("Nu sunt pitagoreice")
#
#
#
#
# # Sa se calculeze volumul trunchiului de con cu inaltimea h, si razele de cerc r1, r2
#
#
# print("Introduceti prima raza")
# r1=int(input())
# print("Introduceti a doua raza")
# r2=int(input())
# print("Introduceti inaltimea")
# h=int(input())
# volum_tru = (h / 3) * (r1 ** 2 + r2 ** 2 + r1 * r2)
# print(f"Volumul este {volum_tru}")
# # Sa se calculeze cel mai mare divizor comun a 2 numere
# # la cate numere sa se afle c.m.m.d.c
# print("Cate numere doriti sa comparati?")
# numar_nr = input()
# while not numar_nr.isnumeric():
#     print("Numerele trebuie sa fie intregi")
#     numar_nr = input()
# numar_nr = int(numar_nr)
#
#


# se face o lista cu numerele introduse, se gaseste cel mai mare nr

print("Introduceti cate numere vreti sa comparati pentru a afla c.m.m.d.c.")
numar_nr = input()
while not numar_nr.isnumeric():
    print("Numerele trebuie sa fie intregi")
    numar_nr = input()
numar_nr = int(numar_nr)
numere = []
for numar in range(0, numar_nr):
    print(f"introduceti nuamrul {str(numar + 1)} pe care doriti sa-l calculati ")
    numere_intr = input()
    while not numere_intr.isnumeric():
        print("Numerele trebuie sa fie intregi")
        print(f"introduceti nuamrul {str(numar + 1)} pe care doriti sa-l calculati ")
        numere_intr = input()
    numere_intr = int(numere_intr)
    if not numere:
        cmmnr = numere_intr
    for numar in numere:
        if numere_intr > numar:
            cmmnr = numere_intr
    numere.append(numere_intr)
# se face o lista cu divizori celui mai mare numar
print(numere)
divizori = []
for divizibil in range(cmmnr, 0, -1):
    if (cmmnr % divizibil) == 0:
        divizori.append(divizibil)
print(divizori)
for div in divizori:
    este_div = True
    toti_div = []
    for numar in numere:
        if (numar % div) == 0:
            toti_div.append(True)
        else:
            toti_div.append(False)
    for nr in toti_div:
        if nr == False:
            este_div = False
    if este_div == True:
        cmmnr = div
        break
print(f"C.m.m.d.c al numerelor {numere} este {cmmnr}")




# Sa se calculeze cel mai mic multiplu comun a 2 numere

