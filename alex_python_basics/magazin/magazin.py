# proof of concept command line application
from pprint import pprint

import pickle_library

from produse import Produs


# produse = []
# pickle_library.save_object_to_filename(produse, "produse.pickle")


def save_products(produse):
    pickle_library.save_object_to_filename(produse, "produse.pickle")


def load_products():
    return pickle_library.read_object_from_filename("produse.pickle")


def user_input(user_indication, default_value, numeric=False):
    result = input(user_indication)
    while not result.isnumeric() and numeric:
        result = input(user_indication)
    if result != "":
        return result
    else:
        return default_value


def interpret_command(command, produse):
    if command == "1":
        citeste_produs(produse)

    elif command == "2":
        afisare_produse(produse)
    elif command == "4":
        stergere_produs(produse)
    elif command == "5":
        modificare_podus(produse)
    elif command == "6":
        vanzare_produs(produse)


def afisare_meniu():
    print("0. Iesire...")
    print("1. Adaugare...")
    print("2. Afisare...")
    print("3. Testare...")
    print("4. Stergere...")
    print("5. Modificare...")
    print("6 Vanzare ...")


def citeste_produs(produse):
    nume = user_input("nume: ", "")
    cantitate = user_input("cantitate: ", "", numeric=True)
    descriere = user_input("descriere: ", "")
    categorie = user_input("categorie: ", "")
    pret = user_input("pret: ", "", numeric=True)

    produs = Produs(nume, float(pret), categorie, int(cantitate), descriere)
    produse.append(produs)
    save_products(produse)

    # return {"nume": nume, "cantitate": int(cantitate), "descriere": descriere, "pret": float(pret),
    #         "categorie": categorie}


def afisare_produse(produse):
    pprint(produse)


def alege_produs(produse):
    for index, produs in enumerate(produse):
        print(index, produs)
    prod_index = int(input('Introduceti un index: '))
    return produse[prod_index]


def stergere_produs(produse: list):
    produs = alege_produs(produse)
    produse.remove(produs)
    save_products(produse)


def modificare_podus(produse: list):
    produs = alege_produs(produse)
    modificare_proprietate_produs(produs)
    # prod_index = produse.index(produs)
    # produs = modifica_camp_prod(produs, 'nume', 'cantitate', 'descriere', 'categorie', 'pret')
    # produse[prod_index] = produs
    # for index, produs in enumerate(produse):
    save_products(produse)


def modificare_proprietate_produs(produs):
    nume = user_input("nume: ", "")
    cantitate = user_input("cantitate: ", "", numeric=True)
    descriere = user_input("descriere: ", "")
    categorie = user_input("categorie: ", "")
    pret = user_input("pret: ", "", numeric=True)
    produs.update(nume=nume)
    produs.update(cantitate=cantitate)
    produs.update(descriere=descriere)
    produs.update(pret=pret)
    produs.update(categorie=categorie)


# def modifica_camp_prod(produs, *campuri):
#     for camp in campuri:
#         valoare_noua = input(f"{camp}(Enter pentru a lasa {produs[camp]}): ")
#         if valoare_noua != "":
#             if camp == "cantitate":
#                 produs[camp] = int(valoare_noua)
#             elif camp == "pret":
#                 produs[camp] = float(valoare_noua)
#             else:
#                 produs[camp] = valoare_noua
#     return produs


def vanzare_produs(produse):
    produs: Produs = alege_produs(produse)
    cantitate = user_input("cantitate:", "", numeric=True)
    cantitate_produs = int(cantitate)
    produs.update(cantitate=produs.quantity - cantitate_produs)
    # produs.quantity = produs.quantity - cantitate_produs
    save_products(produse)


if __name__ == '__main__':
    produse = pickle_library.read_object_from_filename("produse.pickle")
    afisare_meniu()
    command = input("Intorduceti o comanda: ")
    while command != '0':
        interpret_command(command, produse)
        afisare_meniu()
        command = input("Intorduceti o comanda: ")
