import copy

# initialize list1
list1 = [1, 2, [3, 5], 4]

# using copy to create a shallow copy
list2 = copy.copy(list1)

# using deepcopy to create a deep copy
list3 = copy.deepcopy(list1)

print(list1)
print(list2)
print(list3)
