# class SingletonType(type):
#     _instances = {}
#
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
#         return cls._instances[cls]
#
#
# class SingletonClass(metaclass=SingletonType):
#     pass
#
#
# x = SingletonClass()
# y = SingletonClass()
#
# print(x == y)

# def findLucky(arr):
#     counter = {}
#
#     for num in arr:
#         counter[num] = counter.get(num, 0) + 1
#
#     lucky = -1
#     for key, value in counter.items():
#         if key == value and key > lucky:
#             lucky = value
#
#     return lucky
# ar=[2,2,3,4]
# print(findLucky(ar))

#
# def generateParenthesis(n):
#     def generate(A=[]):
#         if len(A) == 2 * n:
#             if valid(A):
#                 ans.append("".join(A))
#         else:
#             A.append('(')
#             generate(A)
#             A.pop()
#             A.append(')')
#             generate(A)
#             A.pop()
#
#     def valid(A):
#         bal = 0
#         for c in A:
#             if c == '(':
#                 bal += 1
#             else:
#                 bal -= 1
#             if bal < 0: return False
#         return bal == 0
#
#     ans = []
#     generate()
#     return ans
#
# print(generateParenthesis(3))
#
# # if __name__ == '__main__':
# n=int(input())
# output=generateParenthesis(n)
# print(output)


# def generateParenthesis(n):
#     ans = []
#
#     def backtrack(S=[], left=0, right=0):
#         if len(S) == 2 * n:
#             ans.append("".join(S))
#             return
#         if left < n:
#             S.append("(")
#             backtrack(S, left + 1, right)
#             S.pop()
#         if right < left:
#             S.append(")")
#             backtrack(S, left, right + 1)
#             S.pop()
#
#     backtrack()
#     return ans
#
# n=14
# x=generateParenthesis(n)
# print(x)