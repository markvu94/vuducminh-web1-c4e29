from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)

database = client.c4e
collection1 = database["posts"]
collection2 = database["customers"]
collection3 = database["river"]

# all_post = collection1.find()
# new_post = {
#     "title": "Choi Fifa Online 4",
#     "author": "Minh Vu C4E29",
#     "content": "Game dễ vl\n Đã lên được rank siêu sao",
# }
# f04 = collection1.find_one({"title": "Choi Fifa Online 4"})
# collection1.delete_one(f04)

# collection1.insert_one(new_post)

all_customer_events = collection2.find({ "ref": "events" })
count_events = 0
for customer_events in all_customer_events:
    count_events += 1
print("number of customers from events is {}".format(count_events))

all_customer_wom = collection2.find({ "ref": "wom" })
count_wom = 0
for customer_wom in all_customer_wom:
    count_wom += 1
print("number of customers from wom is {}".format(count_wom))

all_customer_ads = collection2.find({ "ref": "ads" })
count_ads = 0
for customer_ads in all_customer_ads:
    count_ads += 1
print("number of customers from ads is {}".format(count_ads))

all_river_africa = collection3.find({ "continent": "Africa" })
list_river_africa = []
for river_africa in all_river_africa:
    list_river_africa.append (river_africa["name"])
print (*list_river_africa, sep = ", ")

all_river_america = collection3.find ({ "continent": "S. America" })
# list_river_america_under1000 = []
string2 = "American rivers whose length under 1000 are"
for river_america in all_river_america:
    if river_america["length"] < 1000:
        string2 += " {},".format(river_america["name"])
print (string2[:-1])    
#         list_river_america_under1000.append(river_america["name"])
# print (list_river_america_under1000)







