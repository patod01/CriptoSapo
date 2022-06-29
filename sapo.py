from time import time
from urllib.request import urlopen
import json
# from pprint import pprint


i = 1
url_base = 'https://api.binance.com/api/v3/ticker/price'
symbol = 'BTCBUSD'
url_full = url_base + f'?symbol={symbol}'


def infoBTC(api: str) -> (float, dict):
     ("Retorna la hora promedio a la que se realizo una peticion al "
     "servidor.")
     hora_i_request: float = time()
     with urlopen(api) as response:
          hora_f_request: float = time()
          html_body: bytes = response.read()
     hora = hora_i_request + (hora_f_request - hora_i_request)/2
     
     return hora, json.loads(html_body)


def pAPP(): ...


while ++i:
     try:
          # hora1 = time()
          # with urlopen(url_full) as response:
          #      hora2 = time()
          #      body = response.read()
          hora: float
          btc_info: dict
          hora, btc_info = infoBTC(url_full)

     except KeyboardInterrupt:
          print('tirao abajo con c-c c:')
          break
     except:
          print('binance exploded...')
     else:
          # hora = hora1 + (hora2 - hora1)/2
          # btc_info = json.loads(body)

          simbolo: str = btc_info['symbol']
          precio: str = btc_info['price']
          cadena: str = f'{simbolo},{precio},{hora}\n'

          with open('coins.txt', 'a') as coins:
               coins.write(cadena)

#ned
