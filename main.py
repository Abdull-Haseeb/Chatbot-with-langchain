import pymongo  
client = pymongo.MongoClient("mongodb://localhost:27017")

db = client['mydatabase']

collection = db['db_collection']

# data={
#     "name":"abdul",
#     "father_name":"akram",
#     "nationalality":"Pakistani"
    
# }

# information = collection.insert_one(data)
information = collection.update_one({"name":"abdul"},{"$set":{"nationalality":"live on earth"}})
info=collection.find_one({"name":"abdul"})
print("Inserted document ID",information,info)