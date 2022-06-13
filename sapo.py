# import requests
from time import time#, sleep
from urllib.request import urlopen
import json
# from pprint import pprint

i = 1
url_base = 'https://api.binance.com/api/v3/ticker/price'
symbol = 'BTCBUSD'
url_full = url_base + f'?symbol={symbol}'

while ++i:
     try:
          body = None
          hora1 = time()
          with urlopen(url_full) as response:
               hora2 = time()
               body = response.read()
     except KeyboardInterrupt:
          print('tirao abajo con c-c c:')
          break
     except:
          print('binance exploded...')
     else:
          btc = json.loads(body)

          simbolo = btc['symbol']
          precio = btc['price']
          hora = hora1 + (hora2 - hora1)/2
          cadena = f'{simbolo},{precio},{hora}\n'

          with open('coins.txt', 'a') as coins:
               coins.write(cadena)

# while True:
#      try:
#           response = requests.get(url_full)
#      except KeyboardInterrupt:
#           print('tirao abajo con c-c c:')
#           break
#      except:
#           print('binance exploded...')
#      else:
#           response_json = response.json()

#           simbolo = response_json['symbol']
#           precio = response_json['price']
#           hora = time()
#           cadena = f'{simbolo},{precio},{hora}\n'

#           with open('coins.txt', 'a') as coins:
#                coins.write(cadena)
          #i += 1

#ned

