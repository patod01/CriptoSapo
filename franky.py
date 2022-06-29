import csv
from time import localtime, strftime


def franky() -> None:
     ("Utilidad para transformar csv obtenido de binance a un csv "
     "que puede leerse.")
     coins_book = {
          'BTCBUSD': 1,
          'luna': 2,
          'grt': 2,
          'cake': 2,
          'xrp': 2,
          ...: 'lel',
     }

     db_coins = open('inch.csv')
     db_gold = open('gold.csv', 'w', newline='')

     lente = csv.reader(db_coins)
     pluma = csv.writer(db_gold)

     while ...:
          try:
               linea = next(lente)
          except StopIteration:
               break
          else:
               registro = [
                    coins_book[linea[0]], # line's coin
                    strftime( '%F %R', localtime(float(linea[2])) ), # line's time
                    linea[1] # line's price
               ]
               pluma.writerow(registro)
          ...

     db_coins.close()
     db_gold.close()

     print('files closed and convertion finished')

     return


if __name__ == '__main__':
     franky()

#ned
