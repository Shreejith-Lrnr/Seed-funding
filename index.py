from pymongo import MongoClient

uri = "mongodb+srv://vsrcode21:Vishnusiva21@cluster1.eqqxd4r.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client.databse_hem
Coll_hem = db.Coll_hem

Coll_hem.insert_one({"name":"Hem", "age":19})
print(Coll_hem.find())