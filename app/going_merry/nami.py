import os.path as ruta
import json
from time import time
import usopp, franky


def stealable(wallet_url: str) -> bool:
     ("Confirma si existe una billetera. Si no se encuentra, pregunta"
     " si se desea crear una nueva.")

     if ruta.isfile(wallet_url):
          print('berries!!')
          return True
     else:
          if input('Wallet not found. Wanna create ona? (y/n) ').lower() == 'y':
               try:
                    wallet = open(wallet_url, 'w')
               except Exception as e:
                    print('Cannot create file')
                    raise e
               else:
                    input_saldo = input('Cuanto dinero en USD deseas colocar? (default: 1000)>')
                    try:
                         input_saldo = int(input_saldo)
                         if input_saldo <= 0: raise ValueError
                    except ValueError:
                         print('Bad input, added 1000 USDT')
                         input_saldo = 1000
                    pocket_template = {
                         "coin": {'USDT': input_saldo},
                         "historial": [{
                              "date": franky.make_format_time(time(), seconds=True),
                              "type": 'deposit',
                              "amount": input_saldo,
                              "unit price": 1,
                              "unit": 'USDT/USD',
                         }]
                    }
                    json.dump(pocket_template, wallet)
                    wallet.close()
                    del pocket_template, wallet
          else:
               print('Nothing done')
     return False


def sacar_berrys(wallet_url: str) -> dict:
     ("Carga los TODOS datos de la billetara en memoria.")
     wallet = open(wallet_url, 'r')
     pocket = json.load(wallet)
     wallet.close()
     return pocket


def guardar_berrys(pocket: str, wallet_url: str) -> None:
     ("Guarda los datos en la billetera.")
     with open(wallet_url, 'w') as wallet:
          json.dump(pocket, wallet)
     del pocket, wallet
     return None


def update_coins(log: dict, pocket: dict):
     ...


def nami(modo: str) -> None:
     WALLLET = '../db/chauchero'

     # verifica si existe la billetera
     if not stealable(WALLLET): return None

     # carga el contenido en el bolsillo
     bolsillo: dict = sacar_berrys(WALLLET)

     # compra o venta referenciado al usdt
     coin_price, hora = usopp.coin_info()
     coin_price = float(coin_price['price'])
     hora: str = franky.make_format_time(hora, seconds=True)

     # mover algun dia a su propia funcion
     if modo == 'buy':
          coin_b, coin_s = 'BTC', 'USDT'
          if bolsillo['coin'][coin_s] == 0:
               print(f"Tienes {bolsillo['coin'][coin_s]} {coin_s}, no puedes comprar!")
               return None
          amount_of_coins_traded: float = bolsillo['coin'][coin_s]/coin_price
     elif modo == 'sell':
          coin_b, coin_s = 'USDT', 'BTC'
          if bolsillo['coin'].get(coin_s, 'no coins') == 'no coins':
               print(f'No tienes esta moneda registrada ({coin_s})')
               return None
          else:
               if bolsillo['coin'][coin_s] == 0:
                    print(f"Tienes {bolsillo['coin'][coin_s]} {coin_s}, no puedes vender!")
                    return None
          amount_of_coins_traded: float = bolsillo['coin'][coin_s]*coin_price
     elif modo == 'deposit':
          NotImplemented
          raise
     elif modo == 'withdraw':
          NotImplemented
          raise

     new_trade = {
          "date": hora,
          "type": modo,
          "amount": amount_of_coins_traded,
          "unit price": coin_price,
          "unit": 'USDT/BTC',
     }

     bolsillo['coin'][coin_b] = amount_of_coins_traded
     bolsillo['coin'][coin_s] = 0
     bolsillo['historial'].append(new_trade)

     # salva el nuevo contenido en la cartera
     guardar_berrys(bolsillo, WALLLET)

     del bolsillo, new_trade

     return None

#ned
