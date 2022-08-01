from time import time
from urllib.request import urlopen
import json
from sys import argv
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


def pAPP(mode: list) -> None:
     ("Inicia la aplicacion segun el modo especificado."
     " Para que registre la base de datos, el modo debe ser 'do it',"
     " caso contrario, solo sapea.")

     modo = " ".join(mode[1::])

     hora: float
     btc_info: dict
     simbolo: str
     precio: str
     cadena: str

     if modo == 'do it':
          while ++i:
               try:
                    hora, btc_info = infoBTC(url_full)
               except KeyboardInterrupt:
                    print('tirao abajo con c-c c:')
                    break
               except:
                    print('binance exploded...')
                    break
               else:
                    simbolo = btc_info['symbol']
                    precio = btc_info['price']
                    cadena = f'{simbolo},{precio},{hora}\n'

                    with open('db/coins.csv', 'a') as coins:
                         coins.write(cadena)
     elif modo == 'just the price':
          try:
               btc_price: str = infoBTC(url_full)[1]['price']
               print(btc_price)
          except:
               print('binance exploded...')
          ...
     else:
          ...
          print('lel')
     return None


if __name__ == '__main__':
     pAPP(argv)

#ned
