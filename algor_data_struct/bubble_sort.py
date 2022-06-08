# def bubble_sort(array):
#     n = len(array)
#
#     for i in range(n):
#         # Create a flag that will allow the function to
#         # terminate early if there's nothing left to sort
#         already_sorted = True
#
#         # Start looking at each item of the list one by one,
#         # comparing it with its adjacent value. With each
#         # iteration, the portion of the array that you look at
#         # shrinks because the remaining items have already been
#         # sorted.
#         for j in range(n - i - 1):
#             if array[j] > array[j + 1]:
#                 # If the item you're looking at is greater than its
#                 # adjacent value, then swap them
#                 array[j], array[j + 1] = array[j + 1], array[j]
#
#                 # Since you had to swap two elements,
#                 # set the `already_sorted` flag to `False` so the
#                 # algorithm doesn't finish prematurely
#                 already_sorted = False
#
#         # If there were no swaps during the last iteration,
#         # the array is already sorted, and you can terminate
#         if already_sorted:
#             break
#
#     return array
#
#
# def reversed_bubble_sort(array):
#     n=len(array)
#     for i in range(n):
#         already_sorted=True
#         for j in range(n-1-i):
#             if array[j] < array[j+1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#                 already_sorted = False
#         if already_sorted:
#             break
#     return array
#
# a=[1,2,5,4,6,9,8,0,3]
# # print(bubble_sort(a))
# print(reversed_bubble_sort(a))
#
# def bubble_sort(array, ascending=True):
#     n = len(array)
#
#     for i in range(n):
#         # Create a flag that will allow the function to
#         # terminate early if there's nothing left to sort
#         already_sorted = True
#         for j in range(n - i - 1):
#             condition = array[j] > array[j + 1] if ascending else array[j] < array[j + 1]
#             if condition:
#                 # If the item you're looking at is greater than its
#                 # adjacent value, then swap them
#                 array[j], array[j + 1] = array[j + 1], array[j]
#
#                 # Since you had to swap two elements,
#                 # set the `already_sorted` flag to `False` so the
#                 # algorithm doesn't finish prematurely
#                 already_sorted = False
#
#         # If there were no swaps during the last iteration,
#         # the array is already sorted, and you can terminate
#         if already_sorted:
#             break
#
#     return array
#
