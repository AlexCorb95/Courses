# def simple_generator():
#     n = 1
#     print("This is printed first")
#     yield n
#
#     n += 1
#     print("This is printed second")
#     yield n
#
#     n += 1
#     print("This is printed third")
#     yield n
#
# # a = simple_generator()
# #
# # next(a)
# # next(a)
# # next(a)
# # # next(a)
# # a = simple_generator()
# # next(a)
#
#
# for item in simple_generator():
#     print(item)

# =================================================================================

# def reverse_string(my_string):
#     length = len(my_string)
#     for i in range(length - 1, -1, -1):
#         yield my_string[i]
#
#
# for char in reverse_string("Python Programming"):
#     print(char)

# =================================================================================

# random_list = [1, 3, 4, 6, 10, 15]
#
# # square reach item using list comprehension
# list1 = [x**2 for x in random_list]
# print(list1)
#
# generator = (x**2 for x in random_list)
# print(generator)
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))

# =================================================================================
# random_list = [1, 3, 4, 6, 10, 15]
# print(sum(x for x in random_list))
# print(sum(x**2 for x in random_list))
#
#
# print(min(x**2 for x in random_list))
# print(max(x**2 for x in random_list))

# =================================================================================

# class PowerTwo:
#     def __init__(self, max=0):
#         self.n = 0
#         self.max = max
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.n > self.max:
#             raise StopIteration
#
#         result = 2 ** self.n
#         self.n += 1
#
#         return result
#
#
# def PowerTwoGenerator(max=0):
#     n = 0
#     while n < max:
#         yield 2 ** n
#         n += 1
#
#
# a = PowerTwo()
# print(a)
# print(a.__next__())
#
# b = PowerTwoGenerator(2)
# print(next(b))
# print(next(b))


# print(next(b))

# =================================================================================

# def all_even():
#     n = 0
#     while True:
#         yield n
#         n += 2
#
#
# a = all_even()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# ============================== EXERCITII  ===================================================
# ============================== Loto Generator ===================================================
# import random
#
#
# def generator_loto():
#     lst = []
#     while len(lst) < 6:
#         c = random.randint(1, 49)
#         lst.append(c)
#     yield f"Numerele castigatoare sunt {lst}"
#     joker = random.randint(1000, 1100)
#     yield f"And the joker is {joker}"
#
#
# a = generator_loto()
# print(next(a))
# print(next(a))
# ============================== ChatBot ===================================================

def chat_bot():
    yield "First message"
    yield "Second message"
    yield "Third message"
    yield "Forth message"
    yield "Fifth message"


test_bot = chat_bot()
print(next(test_bot))
print(next(test_bot))
print(next(test_bot))
print(next(test_bot))
print(next(test_bot))


# ============================== Fibonacci ===================================================

def fibonacci():
    lst=[1]
    a=1
    while True :
        lst.append(a)
        a=lst[-2]+lst[-1]
        yield lst

def fibonacci():
    b = 0
    a = 1
    c = 1
    while True:
        yield c
        c = a + b
        b = a
        a = c


c = fibonacci()
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))


def fibonacci(n):
    b = 0
    a = 1
    c = 1
    x=0
    while x < n:
        yield c
        c = a + b
        b = a
        a = c
        x = x+1


c=fibonacci(25)
while True:
    print(next(c))

def fibonacci(n):
    b = 0
    a = 1
    c = 1
    x=0
    while x < n:
        c = a + b
        b = a
        a = c
        x = x+1
    return c

