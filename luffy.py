from nami import nami
import sapo, franky
from sys import argv


match haz_esto := argv[1]:
     case "buy" | "sell":
          nami(haz_esto)
     case "spy":
          sapo.pAPP()
     case "ship":
          franky.franky()
     case _:
          print(f'WTF are you saying... {haz_esto}??')

print(f'Instruccion \'{haz_esto}\' finalizada.')

#ned
