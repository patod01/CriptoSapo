import os.path as ruta
import csv
from time import localtime, strftime


def make_format_time(unformated_time: str, seconds=None) -> str:
     ("Recibe una cadena de un numero decimal que represente una"
     " fecha segun la libreria estandar de C y le da un formato"
     " legible.")
     formated_time = strftime(
          '%F %R',
          localtime(float(unformated_time))
     )
     return formated_time


def database_verification(database_url: str) -> bool:
     ("Confirma si existe una base de datos.")
     if ruta.isfile(database_url):
          print('Materials!!')
          return True
     else:
          print(f'Materials not found in {database_url} D\':')
     return False


def franky() -> None:
     ("Utilidad para transformar csv obtenido de binance a un CSV"
     " ordenado que pueda leerse.")


     def registrar() -> None:
          ("Ingresa un nuevo registro en un CSV.")
          registro = [
               linea[0], # index of logged coin
               minuto_anterior,
               precio['open'],
               precio['high'],
               precio['low'],
               precio['close'],
          ]
          pluma.writerow(registro)
          return


     # Price attributes
     precio = {
          'open':  None,
          'high':  None,
          'low':   None,
          'close': None,
     }
     precio_actual = None
     minuto_anterior = ''
     minuto_actual = ''

     # Databases: coins -> gold
     coinsCSV = '../db/coins.csv'
     goldCSV = '../db/gold.csv'

     if database_verification(coinsCSV):
          db_coins = open(coinsCSV)
     else:
          return None
     db_gold = open(goldCSV, 'w', newline='')

     lente = csv.reader(db_coins)
     pluma = csv.writer(db_gold)
     # CSV's Titles
     pluma.writerow([
          'Coin ID', 'Fecha', 'Open', 'High', 'Low', 'Close'
     ])

     # Database transformation
     while ...:
          try:
               linea = next(lente)
               if len(linea) < 3: continue # jumps empty lines
          except StopIteration:
               print('End of file reached')
               break
          else:
               minuto_actual = make_format_time(linea[2]) # log time
               precio_actual = linea[1] # log price

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

     # ultima hora de regisro
     if minuto_anterior != '': registrar()
     db_coins.close()
     db_gold.close()

     print('Files closed and convertion finished')

     return

#ned
