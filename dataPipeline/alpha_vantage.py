# This module manages all the requests to the alpha vantage api to retrieve the time series data
import requests

API_KEY = 'DEJURKAO1Y269SIZ'


def download_data(symbol: str, function='TIME_SERIES_WEEKLY', api_key=API_KEY):
    url = 'https://www.alphavantage.co/query?function={}&symbol={}&interval=5min&'\
          'apikey={}'.format(function, symbol, api_key)
    r = requests.get(url)
    return r.json()
