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

price = get_price()
res = manager.is_biggest_price(price)
low = manager.is_biggest_price(price)
print(res)
print(low)
manager.set_price(price)
