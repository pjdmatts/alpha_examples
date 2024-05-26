# Cash Flow

# Balance Sheet

import requests
import constants

key = constants.key

symbol = 'GE'

api_function = 'CASH_FLOW'

params = {'function': api_function, 'symbol': symbol, 'apikey': key}

response = requests.get('https://www.alphavantage.co/query', params=params)

try:
    response.raise_for_status()  # Raises an HTTPError if the status is 4xx, 5xx
    data = response.json()
    print(data)
except requests.exceptions.HTTPError as err:
    print(f'HTTP Error: {err}')