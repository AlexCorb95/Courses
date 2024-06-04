conv_trans = {
    'acedgfb': 8,
    'cdfbe': 5,
    'gcdfa': 2,
    'fbcad': 3,
    'dab': 7,
    'cefabd': 9,
    'cdfgeb': 6,
    'eafb': 4,
    'cagedb': 0,
    'ab': 1
}


def convert_string_to_numb(lst):
    for item in lst:
        pass

    # number= "".join(item)


def convert_string(lst):
    suma = 0
    allowed_len = [2, 3, 4, 7]
    for item in lst:
        while len(item) in allowed_len:
            suma += 1
            break
    return suma


def find_the_nubmer(fu_text):
    apperence = 0
    fu_list = fu_text.split('\n')
    print(fu_list)
    fuu_list = [linie.split("|") for linie in fu_list]
    print(fuu_list)
    new_item = [item.split() for item in fuu_list]
    print(new_item)

    for big_item in new_item:
        apperence += convert_string(big_item)
    #     for item in big_item:
    #         if len(item) == 2:
    #             unf_list.append(1)
    #         elif len(item) == 3:
    #             unf_list.append(7)
    #         elif len(item) == 4:
    #             unf_list.append(4)
    #         elif len(item) == 7:
    #             unf_list.append(8)
    #         else:
    #             unf_list.append(0)
    # apperence=unf_list.count(1)+unf_list.count(7)+unf_list.count(4)+unf_list.count(8)
    return apperence


# print(find_the_nubmer(a))


datele = """defabc gcb dbafcg gc gcbed fbecgd begfdac fcbde cfge debag | gfce fgce bdefgca aebgd
eabdc egbda bagcef eg fdageb beg bcfdag egdf agbfd cbgdafe | fdbga bge ebg eg
"""

# data_procesata=datele.strip("|")
print(find_the_nubmer(datele))
