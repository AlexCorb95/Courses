from collections import Counter

number_of_shoes = int(input())
sizes = map(int, input().split())
number_of_customers = int(input())
size_and_price = map(tuple, (map(int, input().split()) for _ in range(number_of_customers)))
size_counter = Counter(sizes)


def shoe_shop():
    result = 0
    for element in size_and_price:
        if element[0] in size_counter and size_counter[element[0]]:
            result += element[1]
            size_counter[element[0]] -= 1
        else:
            print(f"Size {element[0]} not available")
    return result

print(shoe_shop())