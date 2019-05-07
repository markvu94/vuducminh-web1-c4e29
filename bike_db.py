from pymongo import MongoClient

uri = "mongodb+srv://admin:admin@c4e29-cluster-06kp9.mongodb.net/test" 

client = MongoClient(uri)
bike_db = client.bike_db
bike_collection = bike_db["bike_collection"]

list1 = {
    "name": 1,
    "goood": 2,
}

bike_collection.insert_one(list1)