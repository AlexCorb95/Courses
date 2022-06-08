# def fizzBuzz(n):
#     for i in range(1,n+1):
#         if i%3==0 and i%5==0:
#             print("FizzBuzz")
#         elif i%5==0:
#             print("Buzz")
#         elif i%3==0:
#             print("Fizz")
#         else:
#             print(i)
# fizzBuzz(15)

# def reverse_words_order_and_swap_cases(sentence):
#     list_sent=sentence.split()
#     list_sent.reverse()
#     str_rev=""
#     for word in list_sent:
#         for char in word:
#             if char.islower():
#                 str_rev+=char.upper()
#             else:
#                 str_rev+=char.lower()
#
#         str_rev+=" "
#
#     return str_rev
#
#
# sent="aWESOME is cODING"
# print(reverse_words_order_and_swap_cases(sent))

#
# class Car:
#     def __init__(self,speed,units):
#         self.speed=speed
#         self.units=units
#     def __str__(self):
#         return f"Car with the maximum speed of {self.speed} {self.units}"
#
# class Boat:
#     def __init__(self,knots):
#         self.knots=knots
#     def __str__(self):
#         return f"Boat with the maximum speed of {self.knots} knots"
#
#
# a=Boat(77)
# b=Car(151,"km/h")
# print(a,b)

# if __name__ == '__main__':
#     n = int(input().strip())
# if n % 2 != 0:
#     print("Weird")
# elif n % 2 == 0 and n in range(2, 5):
#     print("Not Weird")
# elif n % 2 == 0 and n in range(6, 20):
#     print("Weird")
# elif n % 2 == 0 and n > 20:
#     print("Not Weird")
# n=3
# string=""
# for item in range(1,n+1):
#     string+=str(item)
#
# print(string)
def find_ocur(string):
    for i in range(len(string)-1):
        s=string[i]
        if s.isalnum() and s==string[i+1]:
            print(s)
            break
    else:
        print(-1)


if __name__ == '__main__':
    string=input()
    find_ocur(string)
