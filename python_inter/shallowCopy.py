import copy

# initialize list1
list1 = [1, 2, [3, 5], 4]

# using copy to create a shallow copy
list2 = copy.copy(list1)

# original elements of list 1
print("The orignal list:")
for i in range(0, len(list1)):
    print(list1[i], end=" ")

print("\r")

list2[1] = 10
list2[2][0] = 7

print("The new list of elements after shallow copying:")
for i in range(0, len(list1)):
    print(list2[i], end=" ")

print("\r")

print("The original list of elements after it was copied using shallow copy and the copy suffered changes:")
for i in range(0, len(list1)):
    print(list1[i], end=" ")
