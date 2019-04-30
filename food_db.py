from pymongo import MongoClient

uri ="mongodb+srv://admin:admin@c4e29-cluster-06kp9.mongodb.net/test?retryWrites=true"

client = MongoClient(uri)

foods_db = client.foods_app
Foods = foods_db["foods"]


# for item in food_list:        cach 1
#     foods.insert_one(item)     

# foods_coll.insert_many(food_list)   #cach 2