from typing import List
# Anagrams
# Write a function that finds all the Anagrams of a given word from the given list. Words found should be return as a list.

def anagrams(word, lst_of_words):
    for item in lst_of_words:
        if len(word) == len(item):
            v = search_word(word, item)
        if v == True:
            print(f"Anagrama cuvantului {word} este {item}")
        else:
            print('None')
    return


def search_word(word, item):
    lst1 = []
    lst2 = []
    for char in word:
        lst1.append(char)
    for char in item:
        lst2.append(char)
    lst1.sort()
    lst2.sort()

    if lst1 == lst2:
        return True
    else:
        return False


n = ["cat", "mat", "pat", "dulap"]
wo = "tac"

aa = anagrams(wo, n)


# =================================================================================
# Phone number
# Write a function that takes a list of 11 integers and returns a string in phone number format.

def create_phone_number(n: List[int]) -> str:
    number = "(+"
    for item in n[0:2]:
        number = number + str(item)
    number = number + ") "
    for item in n[2:5]:
        number = number + str(item)
    number=number+"-"
    for item in n[5:8]:
        number = number + str(item)
    number=number+"-"
    for item in n[8:]:
        number = number + str(item)
    return number

lst_numb= [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]
ph_numb=create_phone_number(lst_numb)
print(ph_numb)
