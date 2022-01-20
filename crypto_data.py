"""
    Crypto Data
    
    -Extract Crypto Data for analysis using COINMARKETCAP API -  !!! limit 300 calls / day !!!
        1. Price
        2. Percent change
        3. Overall Volume Change
        4. Volume 24h

"""


"""     All the modules used     """

import json

from main1 import *


"""     Main Functions       """

def crypto(coin_name) :
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

    parameters = {
        'symbol' : coin_name,
        'convert' : 'USD'
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'db843e5d-7d82-4e93-8f59-402955688290'
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)

    curr_price = round(json.loads(response.text)['data'][parameters['symbol']]['quote']['USD']['price'], 2)
    percent_change_24h = round(json.loads(response.text)['data'][parameters['symbol']]['quote']['USD']['percent_change_24h'], 2)
    overall_volume_change_24h = round(json.loads(response.text)['data'][parameters['symbol']]['quote']['USD']['volume_change_24h'], 2)
    volume_24h = round(json.loads(response.text)['data'][parameters['symbol']]['quote']['USD']['volume_24h'], 2)

    #pprint.pprint(json.loads(response.text))

    return  curr_price, percent_change_24h, overall_volume_change_24h, volume_24h
