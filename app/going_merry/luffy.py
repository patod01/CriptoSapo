from nami import nami
import usopp, franky
from sys import argv


match haz_esto := argv[1]:
     case "buy" | "sell":
          nami(haz_esto)
     case "spy":
          usopp.spy()
     case "ship":
          franky.build_blueprint()
     case _:
          print(f'WTF are you saying... {haz_esto}??')

print(f'Instruccion \'{haz_esto}\' finalizada.')

#ned
