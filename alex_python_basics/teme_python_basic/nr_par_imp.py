# se inializeaza un nr x daca nr este par sa se afiseze un text
numar = int(input())
calcul = (numar) % 2

if calcul == 0:

    print(f"{numar}", "Numar este par")

else:
    print(f"{numar}","Numar impar",)
