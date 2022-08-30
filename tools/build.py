import os
from sys import exit as build_notification, argv
import json
import time
# from os import getcwd, listdir, chdir, walk
# from os import mkdir, rename, unlink, rmdir
# from os.path import exists


def del_build_content() -> None:
     # def content_of(folder: str) -> bool:
     #      ("Verifica si la ruta se encuentra listada en la definicion de"
     #      " esta funcion")
     #      forbiden_list = [     
     #           '.\\tools\\conf',
     #           '.\\tools\\conf\\pydist',
     #      ]
     #      for forbiden_folder in forbiden_list:
     #           if (folder + '\\').startswith(forbiden_folder + '\\'):
     #                return False
     #      return True

     build_folder_tree = list(os.walk('.\\build'))[::-1]
     for path, folders, files in build_folder_tree:
          for file in files:
               # is_removable = content_of(path)
               # if not is_removable: continue
               print(path + '\\' + file)
               os.unlink(path + '\\' + file)
          for folder in folders:
               # is_removable = content_of(path + '\\' + folder)
               # if not is_removable: continue
               print(path + '\\' + folder)
               os.rmdir(path + '\\' + folder)
     return None


def check_build_folder(project_name: str) -> bool:
     ("Verifica si existe la carpeta 'build'. Si no existe, intenta"
     " crearla. Solo retorna True si, al verificar, no encuentra"
     " errores ni necesita crear carpetas o archivos")
     if os.getcwd().endswith(project_name):
          try:
               ITER_AGAIN = False
               if not 'build' in os.listdir():
                    os.mkdir('build')
                    ITER_AGAIN = True
               # if not 'conf' in os.listdir('tools'):
               #      os.mkdir('tools\\conf')
                    ITER_AGAIN = True
               if not 'pydist' in os.listdir('tools'):
                    os.mkdir('tools\\pydist')
                    ITER_AGAIN = True
               if not 'legos.txt' in os.listdir('tools'):
                    legos = {
                         "app name": '',
                         "app version": '0',
                         "changelog file": '',
                         "commit file": '',
                         "python version": '',
                    }
                    with open('tools\\legos.txt', 'x') as info_file:
                         json.dump(legos, info_file, indent=2)
                    ITER_AGAIN = True
          except Exception as e:
               print('A')
               print(e)
               return False
          if ITER_AGAIN: return False
     else:
          print(f'No estas en la carpeta correcta del proyecto {project_name}')
          return False
     return True


def check_app_info() -> bool:
     if os.path.isfile('tools\\legos.txt'):
          with open('tools\\legos.txt') as info_file:
               legos: dict = json.load(info_file)

     for info in legos:
          print(info + ': ' + legos[info])
          if legos[info] == '':
               print('No puede haber campos vacios.')
               return False

     if not os.path.isfile(legos['changelog file']):
          print('No se puede encontrar changelog file.')
          return False
     if not os.path.isfile(legos['commit file']):
          print('No se puede encontrar commit file.')
          return False

     python_version = legos['python version'].split('.')

     if len(python_version) != 2:
          print('Version de python mal indicada.')
          return False
     elif not python_version[0].isnumeric():
          print('Version de python mal indicada.')
          return False
     elif not python_version[1].isnumeric():
          print('Version de python mal indicada.')
          return False

     return True


def can_copy() -> bool: return True


def version() -> str:
     build_number: str
     if os.path.isfile('tools\\legos.txt'):
          with open('tools\\legos.txt') as info_file:
               legos: dict = json.load(info_file)
               if legos['app version'].isnumeric():
                    if int(legos['app version']) == 0:
                         print('yes')
                         print(time.strftime('%Y-%m-%d %H:%M', time.localtime()))
               else: # parser
                    print(time.strftime('%Y-%m-%d %H:%M', time.localtime()))

     return None


def numbers_eater(x: str, base_a: int, base_b: int) -> str:
     ("Convierte un numero 'x' en base 'a' al equivalente en base"
     " 'b'. 'x' debe ser un entero positivo y las bases van desde"
     " base 2 hasta base 62 inclusive.")
     if isinstance(x, int): x = str(x)
     if not isinstance(x, str): raise TypeError
     if not isinstance(base_a, int): raise TypeError
     if not isinstance(base_b, int): raise TypeError
     if not 1 < base_a < 63: raise ValueError
     if not 1 < base_b < 63: raise ValueError
     decimal_of = {
          '0': 0,  '1': 1,  '2': 2,  '3': 3,  '4': 4,  '5': 5,  '6': 6,  '7': 7,  '8': 8,  '9': 9,  'a': 10,
          'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17, 'i': 18, 'j': 19, 'k': 20, 'l': 21,
          'm': 22, 'n': 23, 'o': 24, 'p': 25, 'q': 26, 'r': 27, 's': 28, 't': 29, 'u': 30, 'v': 31, 'w': 32,
          'x': 33, 'y': 34, 'z': 35, 'A': 36, 'B': 37, 'C': 38, 'D': 39, 'E': 40, 'F': 41, 'G': 42, 'H': 43,
          'I': 44, 'J': 45, 'K': 46, 'L': 47, 'M': 48, 'N': 49, 'O': 50, 'P': 51, 'Q': 52, 'R': 53, 'S': 54,
          'T': 55, 'U': 56, 'V': 57, 'W': 58, 'X': 59, 'Y': 60, 'Z': 61,
     }
     for letra in x:
          if not letra in decimal_of.keys():
               raise ValueError
     # from base a to decimal
     y = 0
     posicion = len(x) - 1
     for x0 in x:
          if base_a < decimal_of[x0] + 1: raise TypeError
          y += decimal_of[x0]*base_a**posicion
          posicion -= 1
     # from decimal to base b
     X = ''
     while ++y:
          if y < base_b:
               X += list(decimal_of.items())[y][0]
               break
          X += list(decimal_of.items())[y % base_b][0]
          y = y//base_b
     if X == '': X = '0'
     return X[::-1]


def update_change_log(): ...
def compile_project(): ...
def pack_it(): ...


def build() -> None:
     PROJECT_NAME = 'CriptoSapo'
     INSTRUCTION = argv[-1::][0] if len(argv) > 1 else None
     NOT_READY = 0
     COPY = 69

     match INSTRUCTION:
          case 'setup':
               print('Setting up...') # checking files
               del_build_content()
               FOLDER_READY = check_build_folder(PROJECT_NAME)
               if not FOLDER_READY:
                    return print(
                         'Build folder initialized.'
                         ' Update your config file.'
                    )
               if not check_app_info(): build_notification(NOT_READY)
               if can_copy(): build_notification(COPY)
          case 'build':
               print('Building...') # after copy
               BUILD_NUMBER: str = version()
               update_change_log()
               compile_project()
               pack_it()
     return None


build()

#ned
