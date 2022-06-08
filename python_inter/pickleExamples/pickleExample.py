# import pickle
#
# grades = {
#     "Alice": 89,
#     "Bob": 72,
#     "Charles": 87
# }
#
# serial_grades = pickle.dumps(grades)
# print(serial_grades)
#
# received_grades = pickle.loads(serial_grades)
# print(received_grades)

# ==============================================================================================
# import pickle

# data = {
#     "a": [1, 2.0, 3, 5],
#     "b": ["Alice has a dog", "Python is a programming language"],
#     "c": [False, True, False]
# }
#
# with open("data.pickle", 'wb') as f:
#     pickle.dump(data, f)

# ==============================================================================================

# import pickle
#
# with open("data.pickle", "rb") as f:
#     data2 = pickle.load(f)
#
# print(data2)

# ==============================================================================================

# import pickle
#
#
# def storeData():
#     john = {"key": "John", "name": "John Smith",
#             "age": 21, "pay": 4000
#             }
#     jack = {
#         "key": "Jack", "name": "Jack Wilson",
#         "age": 34, "pay": 5000
#     }
#
#     db = {}
#     db['john'] = john
#     db['jack'] = jack
#
#     dbfile = open('examplePickle', "ab")
#
#     # source, destination
#     pickle.dump(db, dbfile)
#     dbfile.close()
#
#
# def loadData():
#     dbfile = open('examplePickle', "rb")
#     db = pickle.load(dbfile)
#     for keys in db:
#         print(keys, "=>", db[keys])
#     dbfile.close()
#
#
# storeData()
# loadData()

# ==============================================================================================

import pickle

john = {"key": "John", "name": "John Smith",
            "age": 21, "pay": 4000
            }
jack = {
    "key": "Jack", "name": "Jack Wilson",
    "age": 34, "pay": 5000
            }

# database
db = {}
db['john'] = john
db['jack'] = jack
print(f"Acesta este db ul inainte de serializare: {db}")
# for storing
b = pickle.dumps(db)

# for loading
a = pickle.loads(b)
print(f"Acesta este db ul dupa deserializare: {a}")




