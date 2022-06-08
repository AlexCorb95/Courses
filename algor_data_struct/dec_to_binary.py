def dec_to_binary():  # while clasic
    decimal = int(input("Enter a decimal number greater then 0:"))
    string = ""

    while decimal != 0:
        rest = decimal % 2
        if rest == 1:
            string = "1" + string

        else:
            string = "0" + string

        decimal = decimal // 2
    return string


def dec_to_binary2():  # do while
    decimal = int(input("Enter a decimal number greater then 0:"))
    string = ""

    while True:
        rest = decimal % 2
        if decimal == 0:
            break
        elif rest == 1:
            string = "1" + string

        else:
            string = "0" + string
        decimal = decimal // 2

    return string


a = dec_to_binary()
print(a)
b = dec_to_binary2()
print(b)
