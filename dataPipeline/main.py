import json
from alpha_vantage import download_data


if __name__ == '__main__':
    data = download_data('Googl')
    with open('api_data.txt', 'w') as out:
        json.dump(data, out, sort_keys=True, indent=4)
