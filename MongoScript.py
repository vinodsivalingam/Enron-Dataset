import json
import pymongo

connection = pymongo.MongoClient("mongodb://localhost")
db=connection.user
record1 = db.user_collection
page = open("out.json", 'r')
parsed = json.loads(page.read())

for item in parsed["Records"]:
    record1.insert(item)
