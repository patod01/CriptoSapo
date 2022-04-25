import requests
from time import sleep, time

i = 1
url_base = 'https://api.binance.com/api/v3/ticker/price'
symbol = 'BTCBUSD'
url_full = url_base + f'?symbol={symbol}'

while True:
     response = requests.get(url_full)
     response_json = response.json()

     simbolo = response_json['symbol']
     precio = response_json['price']
     hora = time()
     cadena = f'{simbolo},{precio},{hora}\n'

     with open('coins.txt', 'a') as coins:
          coins.write(cadena)
     #i += 1

#ned
