# iterable_value = "Python Programming"
# iterable_obj = iter(iterable_value)
#
# while True:
#     try:
#         item = next(iterable_obj)
#         print(item)
#     except StopIteration:
#         break


# =================================================================================

# class TestIterator:
#     def __init__(self, limit):
#         self.limit = limit
#
#     def __iter__(self):
#         self.x = 10
#         return self
#
#     def __next__(self):
#         x = self.x
#         if x > self.limit:
#             raise StopIteration
#         self.x = x + 1
#         return x
#
#
# for i in TestIterator(20):
#     print(i)
#
# for i in TestIterator(9):
#     print(i)

# =================================================================================

# programming_languages = ["Python", "C Programming", "Java", "Javascript", "Go"]
# for i in programming_languages:
#     print(i)
#
# programming_languages = ("Python", "C Programming", "Java", "Javascript", "Go")
# for i in programming_languages:
#     print(i)

programming_language = "Python"
for i in programming_language:
    print(i)

squares = {
    2: 4,
    3: 9,
    5: 25,
    6: 36,
    7: 49
}
for i in squares:
    print(i, squares[i])
