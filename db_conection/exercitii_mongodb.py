import json
import pymongo
import datetime
from pymongo import MongoClient
client=MongoClient()
db=client.medical_db
o=open("medical-data.json","r")
medical=json.loads(o.read())
medicaldata=db.medical_data
# insert=medicaldata.insert_many(medical)
# print(insert)
# s=db.medical_data.delete_many()
search=medicaldata.find({"procedure_code":"0F1F4ZC"})
for item in search:
    print(item)
search=medicaldata.find({"patient_id":74},{"first_name":1,"last_name":1})
print(list(search))
search=medicaldata.update_one({"visit_date.$date":"2019-05-24T01:52:37.000Z"},{"$set":{"procedure_code":"1"}})
search=medicaldata.find_one({"procedure_code":"1"})
print(search)
