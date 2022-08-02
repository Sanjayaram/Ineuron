import pymongo
client = pymongo.MongoClient("mongodb+srv://santosh:mongodb@cluster.awz3j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
d={
    "name":"sant"
}
db1=client["mongo1"]
coll=db1["test"]
coll.insert_one(d)