import datetime
import time

import requests as requests


# functional for requests
def get(site, url):
    req = requests.get(url).json()["page"]
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'), site, req)


sites = {"maria.ru": "http://maria.ru/api/count",
         "rose.ru": "http://rose.ru/api/count",
         "sina.ru": "http://sina.ru/api/count"}

# cycle for request once in minute
while True:
    for key, value in sites.items():
        get(site=key, url=value)
    time.sleep(60)
