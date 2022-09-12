from time import time
from urllib.request import urlopen
import json


coin_index = {
     "BTC":      1,
     "BNB":      2,
     "CAKE":     3,
     "ETH":      4,
     "MATIC":    5,
     "TLM":      6,
     "GRT":      7,
     "BAKE":     8,
     "NEAR":     9,
     "SOL":     10,
     "XRP":     11,
     "DOT":     12,
     "TRX":     13,
     "XLM":     14,
     "SHIB":    15,
     "DOGE":    16,
     "LUNA":    17,
     ...:    'lel',
}


def API_string_builder():
     url_base = 'https://api.binance.com/api/v3/ticker/price'
     symbol = 'BTC'
     USD = 'USDT'
     url_full = url_base + f'?symbol={symbol}' + USD
     return url_full


def coin_info() -> (float, dict):
     ("Retorna el precio de un par y la hora promedio a la que se"
     " realizo la peticion al servidor.")

     api: str = API_string_builder()
     hora_i_request: float = time()
     with urlopen(api) as response:
          hora_f_request: float = time()
          html_body: bytes = response.read()
     hora = hora_i_request + (hora_f_request - hora_i_request)/2

     return json.loads(html_body), hora


def spy() -> None:
     ("Llama a la api de binance y registra el simbolo, precio y hora"
     " de la llamada en un csv.")

     i = 1
     hora: float
     coin_price: dict
     indice: int
     precio: str
     cadena: str
     coinsCSV = '../db/coins.csv'

     print('Proceso iniciado. Para salir, presionar ctrl+c...')

     while ++i:
          try:
               coin_price, hora = coin_info()
          except KeyboardInterrupt:
               print('Tirao abajo con c-c c:')
               break
          except:
               print('Binance exploded...')
               break
          else:
               indice = coin_index[coin_price['symbol'].removesuffix('USDT')]
               precio = coin_price['price']
               cadena = f'{indice},{precio},{hora}\n'

               # tratar de llevar este bloque justo despues del while
               with open(coinsCSV, 'a') as coins:
                    coins.write(cadena)
     return None

#ned
