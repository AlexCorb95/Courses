# def rotate_char(character, times=1):
#     i=0
#     character_to_rep="\|/-"
#     rep_char="│╱─╲"
#     while i<=times:
#         new_char=character.maketrans(character_to_rep,rep_char)
#         character=character.translate(new_char)
#         i+=1
#     return character
# def rotate_characters(characters):
#     result=""
#     length=len(characters)
#     for character in characters:
#         new_char=rotate_char(character,length)
#         result += new_char
#     return result
#
# test= "╲││╱│─╱││─╱╲│─"
# par= rotate_characters(test)
# print(par)
# 4. b)  Fiind date cele de mai sus, faceti ca fiecare caracter sa se
# roteasca 45' * pozitia in string


# def rotate_character(character, times=0):
#     character_to_replace = "╲│╱─"
#     replaced_characters = "╲│╱─"
#     while times > 0:
#         replaced_characters = replaced_characters[1:] + replaced_characters[0]
#         times -= 1
#     new_characters = character.maketrans(character_to_replace, replaced_characters)
#     character = character.translate(new_characters)
#     return character
#
#
# def rotate_characters(characters):
#     result = ""
#     for index, character in enumerate(characters):
#         new_character = rotate_character(character, times=index)
#         result += new_character
#     return result
#
#
# test = "╲││╱│─╱││─╱╲│─│─╲╲╱╱││─╱│╲─╱─"
# parameter = rotate_characters(test)
# print(parameter)