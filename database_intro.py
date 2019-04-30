from pymongo import MongoClient
from bson.objectid import ObjectId 

uri ="mongodb+srv://admin:admin@c4e29-cluster-06kp9.mongodb.net/test?retryWrites=true"

#1 create a connection
client = MongoClient(uri)

#2 get/ create a database
first_db = client.first_database
#3 get/ create a collection
first_coll = first_db["first_collection"]

#4 create a document
first_document = {
    "game": "Dota",
    "description": "Moba",
}

game_list = [
    {
        "game": "pikachu",
        "description": "lost money",
    },
    {
        "game": "pubg",
        "description": "sung",
    },
]
#5 CREATE
#5.1 create one
# first_coll.insert_one(first_document)
#5.2 create many
# first_coll.insert_many(game_list)

#6 READ
#6.1 Read all
all_games = first_coll.find()
# Lazy loading
# for game in all_games:
#     print (game)

#6.2 Read one
# pikachu_game = first_coll.find_one({"_id": ObjectId("5cc064bf8874be21939c99ff")})
# print(pikachu_game)

#7 UPDATE
# pikachu_game = first_coll.find_one({"_id": ObjectId("5cc064bf8874be21939c99fe")})
# new_value = { "$set": { "game": "PIKACHU" } }
# first_coll.update_one(pikachu_game, new_value)

#8 DELETE
# pikachu_game = first_coll.find_one({"_id": ObjectId("5cc064bf8874be21939c99fe")})
# if pikachu_game is not None:
#     first_coll.delete_one(pikachu_game)
# else:
#     print("not found")



