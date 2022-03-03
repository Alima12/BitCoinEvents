import pymongo as mongo


class DB:
    def __init__(self):
        client = mongo.MongoClient("mongodb://localhost:27017/")
        db = client["bit_prices"]
        table = db["prices"]
        self.table = table

    def insert(self, data):
        self.table.insert_one(data)

    def get(self, query):
        data = self.table.find_all(query)
        return data

    def sort(self, data, pattern):
        return data.sort(pattern)

    def update(self, query, value):
        result = self.table.update_one(query, value)
        return result
 


class DbManager:
    def __init__(self):
        self.db = DB()
    