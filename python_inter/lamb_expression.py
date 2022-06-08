# adaugare = lambda x: x + 15
# print(adaugare(2))
# multiply = lambda x, y: x * y
#
# print(multiply(2, 3))
#
#
# def rsl(n):
#     return lambda x: x * n
#
#
# result = rsl(3)
# print(result(2))
# ============================================================================================

# find_str = lambda x, y: print(f"incepe cu {y}") if x[0] == y else print(f"nu incepe cu {y}")
#
# d=find_str("asdasda","a")
# x="asdasda"
# y="a"
# if x[0]== y:
#     print(f"incepe cu {y}")
# else:
#     print(f"nu incepe cu {y}")
#
# ============================================================================================

# import datetime
#
# now = datetime.datetime.now()
# print(now)
# year = lambda x: x.year
# month = lambda x: x.month
# day = lambda x: x.day
# time_now = lambda x: x.time()
# print("Year: ", year(now))
# print("Month: ", month(now))
# print("Day: ", day(now))
# print("Time: ", time_now(now))


# ===========================================map=================================================

# integars = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# patrat = map(lambda x: x ** 2, integars)
# cub = map(lambda x: x ** 3, integars)
# print(list(patrat))
# print(list(cub))


# ==========================================filter==================================================
# lst1 = [1, 2, 3, 4, 5, 6, 7]
# lst2 = [5, 6, 7, 8]
#
# common_elements = list(filter(lambda x: x in lst1, lst2))
# print(common_elements)
# # ======================================filter=====================================================


# lst3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 12, 13, 124, 523, 13]
# cnt_even = len(list(filter(lambda x: x % 2 == 0, lst3)))
# cnt_odd = len(list(filter(lambda x: x % 2 != 0, lst3)))
# print(cnt_odd)
# print(cnt_even)
# ====================================sorted========================================================

# lst1 = [
#         {"nume": "naa", "varsta": 22},
#         {"nume": "csdg", "varsta": 21},
#         {"nume": "badf", "varsta": 209},
#         {"nume": "gsa", "varsta": 212},
#         {"nume": "rasdfa", "varsta": 232}
# ]
# sortam_lst=sorted(lst1,key=lambda x : x["varsta"])
# print(sortam_lst)
# ===============================  Min == Max =======================================================

# lst1=[[1,2,3],[0,0],[3,3,3,4,5,4],[11,2],[0,0],[0,8,7,6,2]]
# lst_min=min(lst1,key= lambda k: len(k))
# lst_max=max(lst1,key= lambda k: len(k))
# print(len(lst_min),lst_min)
# print(len(lst_max),lst_max)

