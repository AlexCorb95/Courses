# def caesarCipher(s, k):
#     result=""
#     for char in s:
#         int_char = ord(char)
#
#         if int_char + k <= 122 and int_char >= 97 or int_char + k <= 90 and int_char >= 65:
#             int_char += k
#             new_char = chr(int_char)
#             result+=new_char
#         elif int_char <= 48 and int_char >= 57:
#             int_char += k
#             new_char = chr(int_char)
#             result+=new_char
#         elif int_char < 97:
#             result += char
#         elif int_char + k > 122:
#             int_char = int_char - 26 + k
#             new_char = chr(int_char)
#             result+=new_char
#
#         elif int_char + k > 90:
#             int_char = 90 - 25 + k
#             new_char = chr(int_char)
#             result+=new_char
#
#     return result
#
#
# c = caesarCipher("Hello_World!", 4)
# print(c)
import string
symbols_low = string.ascii_lowercase
symbols_up = string.ascii_uppercase


def caesarCipher(s, k):
    results=""
    for char in s:
        # char=s[index]
        if char in symbols_low:
            new_index=symbols_low.index(char)
            new_char=symbols_low[new_index+k if new_index+k<=25 else (new_index+k)%26 ]
            results+= new_char
        elif char in symbols_up:
            new_index=symbols_up.index(char)
            new_char=symbols_up[new_index+k if new_index+k<=25 else (new_index+k)%26 ]
            results+= new_char
        else:
            results+=char
    return results

c = caesarCipher("Hello_World!", 4)
print(c)
