# This module manages all the requeadd sts to the alpha vantage api to retrieve the time series data
import requests
import json

API_KEY = 'DEJURKAO1Y269SIZ'


def download_data(symbol: str, function='TIME_SERIES_WEEKLY', dump=False) -> dict:
    valid, best_match = validate_symbol(symbol)
    if not valid:
        return _not_valid(dump)
    url = 'https://www.alphavantage.co/query?function={}&symbol={}&interval=5min&' \
          'apikey={}'.format(function, best_match, API_KEY)
    r = requests.get(url)
    if dump:
        _dump_data(r.json(), 'api_data.txt')
    return r.json()


def validate_symbol(symbol: str) -> (bool, str):
    url = 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={}&apikey={}'.format(symbol, API_KEY)
    r = requests.get(url)
    matches = r.json()['bestMatches']
    if not matches:
        return False, symbol
    return True, matches[0]['1. symbol']


def _not_valid(dump: bool) -> dict:
    data = {"Error": "No se ha encontrado ninguna coincidencia para el simbolo solicitado"}
    if dump:
        _dump_data(data, 'api_data.txt')
    return data


def _dump_data(data: dict, file: str):
    with open(file, 'w') as out:
        json.dump(data, out, sort_keys=True, indent=4)


if __name__ == '__main__':
    company = validate_symbol('cf')
    print(company)
