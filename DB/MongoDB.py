# pip3 install pymongo

import pymongo

client = pymongo.MongoClient("mongodb://localhost:3000/")
# creating database
database = client["mongodatabase"]
# creating collection
collection = database["mongocollection"]
