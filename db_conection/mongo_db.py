import pymongo
import datetime
from pymongo import MongoClient

client = MongoClient()
db = client.test_db
collection = db.test_collection
# dictionar = {
#     "name": "Alex",
#     "hobbies": ["Motociclete","Pictura", "VideoGames"],
#     "date": datetime.datetime.now(),
#     "income": 30.2,
#     "age": 27
# }
dictionar = {
    "name": "Alex",
    "hobbies": ["Motociclete", "Pictura", "VideoGames"],
    "date": datetime.datetime.now() - datetime.timedelta(days=1),
    "income": 30.2,
    "age": 27
}
# inserted=collection.insert_one(dictionar)
# print(inserted)
# v=db.list_collection_names()
# print(v)
# document=collection.find()
# print(document)
# document = collection.find_one({"name": "Ionel"})
# print(document)
# inserted_id=collection.insert_one(dictionar).inserted_id
# print(inserted_id)
# dictionar_document=collection.find_one({"_id":inserted_id})
# print(dictionar_document)
# documents=collection.find({"date":{"$gt":datetime.datetime.now()-datetime.timedelta(hours=3)}})
# print(collection.count_documents({}))
# print(len(list(documents)))
# ========UPDATE
# collection.update_many({"name":"Ion"},
#                        {"$set":{"hobbies":["Programeaza","Citeste","Bea Bere"]},
#                         "$currentDate":{"date":True}})
# documents=collection.find()
# for doc in documents:
#     print(doc)
# =============AGREGARE
result = collection.aggregate([{"$match": {"name": "Ion"}},
                               {"$group": {"_id": "$income", "total_income": {"$sum": "$income"}}}])
print(list(result))
