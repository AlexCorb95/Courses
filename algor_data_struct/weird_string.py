def to_weird_case(string: str) -> str:
    index = 0
    string_list = list(string)
    while index in range(len(string_list)):
        if index % 2 == 0:
            x = string_list[index]
            y= x.upper()
            string_list[index] = y
            # print(f"x={x}")

        else:
            x = string_list[index]
            y=x.lower()
            string_list[index] = y
            # print(f"x={x}")
        index += 1
    converted_string="".join(string_list)
    return converted_string


print(to_weird_case('String'))
print(to_weird_case('Algorithms and data structures'))