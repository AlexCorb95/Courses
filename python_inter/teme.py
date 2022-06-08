# 1. Write a generator that generates prime numbers in a specified range.
# ( create a function that verifies if a number is prime and use it in the generator
prime_terms = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
    107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
    227, 229, 233, 239, 241, 251, 257, 263, 269, 271
]


def prime_verification(n):
    for unit in prime_terms:
        cat = n // unit
        rest = n % unit
        if unit > cat:
            return True
        else:
            continue


#
# def prime_generator(length):
#     n = 1
#     while n in range(length):
#         prime_verification(n)
#         if prime_verification(n) == True:
#             yield n
#         n = n + 1
#
#
# ver = prime_generator(11)
# print(next(ver))
# print(next(ver))
# print(next(ver))
# print(next(ver))
# print(next(ver))
# print(next(ver))
# print(next(ver))
# print(next(ver))
# print(next(ver))
var = prime_verification(15)
print(var)
# =================================================================================
# 2. Write a generator that generates all posible pairs of 2 cards from a deck.
# (practic trebuie generate toate posibilele 2 perechi de carti dintr-un pachet de carti)
# Rank the cars by their rank: 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"
# and
# by their suit: "clubs", "diamonds", "hearts", "spades"
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
shapes = ["clubs", "diamonds", "hearts", "spades"]


def posible_pairs(length=4, initial=None, result=None):
    if result is None:
        result = []
    if initial is None:
        initial = []
    if len(initial) == length:
        str_value = ""
        for c in initial:
            str_value += c
        result.append(str_value)
        return result
    for number in numbers:
        initial.append(number)
        for shape in shapes:
            initial.append(shape)
            index = len(initial) - 1
            result = posible_pairs(initial=initial, result=result)
            initial.pop(index)
    return result
amama = posible_pairs()

