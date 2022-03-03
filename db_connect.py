import pymongo as mongo
from datetime import datetime, timedelta
from usd_to_rial import exchange


class DB:
    def __init__(self):
        client = mongo.MongoClient("mongodb://localhost:27017/")
        db = client["bit_prices"]
        table = db["prices"]
        self.table = table

    def insert(self, data):
        self.table.insert_one(data)

    def get(self, query):
        data = self.table.find(query)
        return data

    def sort(self, data, pattern):
        return data.sort(pattern, -1)

    def update(self, query, value):
        result = self.table.update_one(query, value)
        return result
 


class DbManager:
    def __init__(self):
        self.db = DB()

    def set_price(self, price):
        now = datetime.now()
        rial = exchange(price)
        self.db.insert({
            "price": price,
            "rial":rial,
            "created_time": now
        })

    def get_price_today(self):
        now = datetime.now()
        dif = timedelta(hours=now.hour, minutes=now.minute, seconds=now.second)
        time_difference = now - dif
        results = self.db.get({
            "created_time": {
                "$gt": time_difference
            }
        })
        resutls = self.db.sort(results, "created_time")
        return [record for record in results]

    def get_price_yesterday(self):
        now = datetime.now()
        dif = timedelta(hours=now.hour, minutes=now.minute, seconds=now.second, days=1)
        time_difference = now - dif
        until_today = now - timedelta(hours=now.hour, minutes=now.minute, seconds=now.second)
        results = self.db.get({
            "created_time": {
                "$gt": time_difference,
                "$lt": until_today
            }
        })
        resutls = self.db.sort(results, "created_time")
        return [record for record in results]

    def get_average_price(self, data, limit=0):
        if limit==0:
            limit = len(data)
        data = data[:limit]
        sum_prices = sum([x["price"] for x in data])
        average = sum_prices / limit
        return round(average, 2)




    