# import timeit
#
# def recur_suma(a):
#     if len(a) == 0:
#         return 0
#     return a[0] + recur_suma(a[1:])
#
#
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a = recur_suma(l)
# print(a)
## =================================================================================

#
# def recur_fib(x):
#     if x == 0:
#         return 0
#     elif x==1:
#         return 1
#     else:
#         return recur_fib(x - 1) + recur_fib(x - 2)
#
#
# # da = recur_fib(5)
# # print(da)
## =================================================================================

# def fib(n):
#     a, b = 0, 1
#     for number in range(0, n - 1):
#         a, b = b, a + b
#     return b
#
# # c=fibonacci(5)
# # print(c)
# n = 20
# print(timeit.timeit('recur_fib(n)', 'from __main__ import recur_fib, n', number=10))
# print(timeit.timeit('fib(n)', 'from __main__ import fib, n', number=10))
# =================================================================================

# def recur_lst(lst):
#     total=0
#     if len(lst) == 0:
#         return 0
#     for elem in lst:
#         if type(elem) == list:
#            total =total + elem[0] + recur_lst(elem[1:])
#         else:
#             total=total+elem
#     return total
#
# ava = [1, 2, [3, 4], [5, [1,2,3],6]]
# aba = recur_lst(ava)
# print(aba)

# =================================================================================

# def recur_sum(st):
#     if st == 0:
#         return 0
#     else:
#         return st % 10 + recur_sum(st // 10)
#
#
# print(recur_sum(345))
# print(recur_sum(45))
# print(recur_sum(33245))
# print(recur_sum(3454565))
# print(recur_sum(345452))
#
#
# def itera_sum(digits):
#     total = 0
#     digits = str(digits)
#     for elem in digits:
#         total = int(elem)+total
#
#     return total
#
#
# print(itera_sum(12333))
# ========================================Recur=========================================

def recurs_sigma(n):
    total=n-2
    if total <=0:
        return total+2
    else:
        return n+recurs_sigma(total)
print(recurs_sigma(10))
# =================================Iter================================================
def iterativ_sigma(n):
    total=n
    while n>0:
        n=n-2
        total+=n
    return total

print(iterativ_sigma(10))

import bisect
my_list=[1,2,3,4,4,6,7,8,9]
bisect.bisect(my_list,5)

def find(nums,num):
    i=bisect.bisect_left(nums,num)
    if i != len(nums) and nums[i] == num:
        return i
print(find(my_list,4))


