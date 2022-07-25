import json
import os
from pymongo import MongoClient
import urllib

username = urllib.parse.quote_plus('ncc')

password = urllib.parse.quote_plus('***REMOVED***')

client = MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password))

print(client.list_database_names())

db = client["app"]

data = db["data"]

file = open(os.path.join(os.getcwd(), "data/data.json"), "r", encoding="utf8")

object = json.load(file)
data.insert_one(object)
print(data.find_one())
