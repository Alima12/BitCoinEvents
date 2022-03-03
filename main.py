import requests as rq
from db_connect import DbManager as manager


def get_price():
    url = "https://blockchain.info/ticker"
    response = rq.get(url)
    response = response.json()
    #جدا کردن قیمت دلاری
    price = response["USD"]
    #گرفتن قیمت خرید بیت کوین
    buy_price = price["buy"]

    return buy_price


price = get_price()
print(price)