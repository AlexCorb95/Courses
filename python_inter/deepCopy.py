import copy

# initialize list1
list1 = [1, 2, [3, 5], 4]

# using deepcopy to create a deep copy
list2 = copy.deepcopy(list1)

# original elements of list 1
print("The orignal list:")
for i in range(0, len(list1)):
    print(list1[i], end=" ")

print("\r")

# adding and element to new list
list2[2][0] = 7

print("The new list of elements after deep copying:")
for i in range(0, len(list1)):
    print(list2[i], end=" ")

print("\r")

# Change is NOT reflected in original list
print("The original elements after deep copying:")
for i in range(0, len(list1)):
    print(list1[i], end=" ")


