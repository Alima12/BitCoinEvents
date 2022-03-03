import requests as rq
from db_connect import DbManager


manager = DbManager()

def get_price():
    url = "https://blockchain.info/ticker"
    response = rq.get(url)
    response = response.json()
    price = response["USD"]
    buy_price = price["buy"]
    return buy_price

# manager.set_price(get_price())
# res = manager.get_average_price(manager.get_price_today(), 10)
# print(res)

