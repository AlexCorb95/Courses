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
# def aparitie_dict_comprihansion(text="python the basics"):
#     result = {letter: text.count(letter) for letter in text}
#     return result
#
#
# print(aparitie_dict_comprihansion())
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
# letter ="\u0041"
# last_letter="\u0049"
# while letter <= last_letter:
#     letter += "\1"
#     print(letter)

l="asdafsdfgasgdasf"
last_char=l[-1]
if last_char == "f":
    l=l[:-2]
    # print ("DADADA")
for iterabil in l:
    print(iterabil)
print(last_char)
print(l)