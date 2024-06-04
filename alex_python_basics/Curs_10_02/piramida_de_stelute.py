# Sa se scrie o functie care deseneaza o piramida ca mai jos.
# Latimea bazei se primeste ca parametru in functie.
# a)
#    *
#   ***
#  *****
# *******

def draw_pyramid(width):
    for index in range(1, width + 1, 2):
        print(" " * ((width - index) // 2) + "*" * index + " " * ((width - index) // 2))


# draw_pyramid(99)

# b)
# ^^^^^^^
# ^^^ ^^^
# ^^ * ^^
# ^ *** ^
#  *****
# *******
def draw_pyramid2(width):
    print("^" * width)
    print("^" * ((width - 1) // 2) + " " + "^" * ((width - 1) // 2))
    for index in range(1, width + 1, 2):
        if index == width:
            space = ""
        else:
            space = " "
        print(f'{"^" * ((width - index) // 2 - 1)}{space}{"*" * index}{space}{"^" * ((width - index) // 2 - 1)}')

draw_pyramid2(21)