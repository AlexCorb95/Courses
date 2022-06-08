# Example 1 using = operator

# old_list = [[1, 2, 3], [4, 5, 6], [7, 8, "T"]]
#
# new_list = old_list
# new_list[2][2] = 9
#
# print("old list:", old_list)
# print("id of old list: ", id(old_list))
#
# print("new list:", new_list)
# print("id of new list: ", id(new_list))

# Example 2: Create a copy using shallow copy

# import copy
#
# old_list = [[1, 2, 3], [4, 5, 6], [7, 8, "T"]]
# new_list = copy.copy(old_list)
#
# print("old list:", old_list)
# print("new list:", new_list)
#
# print("id of old list: ", id(old_list))
# print("id of new list: ", id(new_list))

# Example 3:
# import copy
#
# old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# new_list = copy.copy(old_list)
#
# old_list.append([4, 4, 4])
# print("old list:", old_list)
# print("new list:", new_list)
# print("\r")
# print("\r")
# old_list[0][0] = 0
# print("old list:", old_list)
# print("new list:", new_list)

# Example 4
#
# import copy
#
# old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# new_list = copy.copy(old_list)
#
# old_list[1][1] = "AA"
# print("old list:", old_list)
# print("new list:", new_list)

# Example 5: Copying a list using deepcopy()
# import copy
#
# old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# new_list = copy.deepcopy(old_list)
#
# print("old list:", old_list)
# print("new list:", new_list)

# Example 6: Adding a new nested object in the list using deepcopy()
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

old_list[1][0] = "BB"

print("old list:", old_list)
print("new list:", new_list)
























































