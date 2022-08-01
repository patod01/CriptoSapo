import csv
from time import localtime, strftime
from pprint import pprint


def franky() -> None:
     ("Utilidad para transformar csv obtenido de binance a un CSV "
     "que pueda leerse.")
     
     def registrar() -> None:
          ("Ingresa un nuevo registro en un CSV.")
          registro = [
               coins_book[linea[0]], # line's coin
               minuto_anterior,
               precio['open'],
               precio['high'],
               precio['low'],
               precio['close'],
          ]
          pluma.writerow(registro)
          return

     coins_book = {
          'BTCBUSD':   1,
          'XRP':       2,
          'GRT':       3,
          'BNB':       4,
          'BAKE':      5,
          'ETH':       6,
          'TLM':       7,
          'CAKE':      8,
          'MATIC':     9,
          'DOT':      10,
          'SOL':      11,
          'NEAR':     12,
          'BUSDUSDT': 13,
          'LUNC':     14,
          ...: 'lel',
     }

     precio = {
          'open': None,
          'high': None,
          'low': None,
          'close': None
     }
     precio_actual = None
     minuto_anterior = ''
     minuto_actual = ''

     # Data base transformation
     db_coins = open('db/coins.csv')
     db_gold = open('db/gold.csv', 'w', newline='')

     lente = csv.reader(db_coins)
     pluma = csv.writer(db_gold)
     # CSV's Titles
     pluma.writerow([
          'Coin ID', 'Fecha', 'Open', 'High', 'Low', 'Close'
     ])

     while ...:
          try:
               linea = next(lente)
               if len(linea) < 3: continue
          except StopIteration:
               print('oef reached')
               break
          else:
               minuto_actual = strftime( '%F %R', localtime(float(linea[2])) ) # line's time
               precio_actual = linea[1] # line's price

               if minuto_actual[-2::] != minuto_anterior[-2::]:
                    # Actualizacion de registro de la hora anterior
                    if minuto_anterior != '': registrar()
                    # Ajuste de precio inicial de nuevo registro
                    precio['open'] = precio_actual
                    precio['high'] = precio_actual
                    precio['low'] = precio_actual
                    # Nueva hora de seguimiento
                    minuto_anterior = minuto_actual
               # Seguimiento del precio
               if precio['high'] < precio_actual: precio['high'] = precio_actual
               if precio['low'] > precio_actual: precio['low'] = precio_actual
               precio['close'] = precio_actual
          ...==...

     # estoy pensando para agregar ultima hora de egisro
     if minuto_anterior != '': registrar()
     db_coins.close()
     db_gold.close()

     print('files closed and convertion finished')

     return


if __name__ == '__main__':
     franky()

#ned
