# 2. Sa se scrie o functie care genereaza toate combinatiile posibile a-z 0-9 de cate 3 caractere.
# pt 3:
# 'aaa', 'aab', 'aac', ..., 'aaz', 'aa0', 'aa1', ..., 'aa9',
# 'aba', 'abb', 'abc', ..., 'abz', 'ab0', 'ab1', ..., 'ab9',
# ...
# '99a', '99b', '99c', ..., '
# ...
# 3. Sa se dinamizeze functia de mai sus pentru orice numar de caractere.


# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
#            'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def increment(sir, lungime):
    # if sir[-1] == '8':
    #     sir=sir[:-lungime]
    sir = sir[:-1]
    return sir


def factorial(x):
    result = 1
    while x > 0:
        result = x * result
        x = x - 1
    return result


def comb(n, k):
    results = n ** k
    print(results)
    return results


def posible_comb(lista, numar_combinatii):
    lista_comb = []
    sir = ""
    i = 1
    combinari = comb(len(lista), numar_combinatii)
    # fact = factorial(len(lista))
    if len(lista) < numar_combinatii:
        return ("No se puedo!!")
    while len(lista_comb) < combinari:
        for character in lista:
            while len(sir) < numar_combinatii:
                sir += character

            lista_comb.append(sir)
            sir = increment(sir, len(sir))
        continue
    return lista_comb


l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
v = posible_comb(l, 3)
print(v)

# lista_comb.append(char)
# luam pprimu index de numar_comb-1 ori si ultimul il schimbam pana ajungem la capat(1,2,3,4...len(lista))
# luam primu index de numar_comb-2.....
# luam len(lista)-1 index de numar comb
print(factorial(35))
print(comb(35, 3))

# print(ala)
