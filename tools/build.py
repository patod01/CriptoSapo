import os
from sys import exit as build_notification, argv
import json
import time
from zipfile import ZipFile as zfile, ZIP_DEFLATED


def del_build_content() -> None:
     ("Recorre toda la carpeta 'build' para eliminar su contenido.")
     build_folder_tree = list(os.walk('.\\build'))[::-1]
     for path, folders, files in build_folder_tree:
          for file in files:
               print(path + '\\' + file)
               os.unlink(path + '\\' + file)
          for folder in folders:
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
               if not 'pydist' in os.listdir('tools'):
                    os.mkdir('tools\\pydist')
                    ITER_AGAIN = True
               if not 'bdmn.txt' in os.listdir('tools'):
                    legos = {
                         "app name": '',
                         "app version": '0',
                         "beta version": '1',
                         "build date": '0',
                         "build number": '0',
                         "build version": '0',
                         "changelog file": '',
                         "commit file": '',
                         "license": '',
                         "python version": '',
                    }
                    with open('tools\\bdmn.txt', 'x') as info_file:
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
     if os.path.isfile('tools\\bdmn.txt'):
          with open('tools\\bdmn.txt') as info_file:
               legos: dict = json.load(info_file)
     else:
          return False

     print()
     for info in legos:
          print(info + ': ' + legos[info])
          if legos[info] == '':
               print('No puede haber campos vacios.')
               return False
     print()

     if legos['app version'].isnumeric():
          if int(legos['build number']) < 0:
               print('Major version must be a possitive integer')
               return False
     else:
          print('Build number must be a possitive integer')
          return False

     if legos['beta version'].isnumeric():
          if not int(legos['beta version']) in (0, 1):
               print('Beta version must be a 0 or 1')
               return False               
     else:
          print('Beta version must be 0 or 1')
          return False

     if legos['build number'].isnumeric():
          if int(legos['build number']) < 0:
               print('Build number must be a possitive integer')
               return False
     else:
          print('Build number must be a possitive integer')
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


def klaus_fangs(x: str, base_a: int, base_b: int) -> str:
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


def version_it() -> str:
     ("Updates build number and its date inside app's information file.")
     legos: dict
     fecha: [str, str]
     build_number: str
     version_code: str
     with open('tools\\bdmn.txt') as info_file:
          legos = json.load(info_file)
          new_build_date: str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
          fecha = time.strftime('%y.%j', time.localtime()).split('.')
          build_number = str(int(legos['build number']) + 1)
          version_code = klaus_fangs(fecha[0], 10, 62) \
                       + klaus_fangs(fecha[1], 10, 62) \
                       + klaus_fangs(build_number, 10, 62)
     with open('tools\\bdmn.txt', 'w') as info_file:
          legos['build date'] = new_build_date
          legos['build number'] = build_number
          legos['build version'] = legos['app version'] + '.' + version_code
          print(json.dumps(legos, indent=2))
          json.dump(legos, info_file, indent=2)
     return legos['build version']


def update_changelog() -> None:
     ("Writes on a changelog file defined in the app information file"
     " the content of the commit file, adding the date and build numbers."
     " It only do the writing if the build is not a beta version.")
     with open('tools\\bdmn.txt') as info_file:
          legos: dict = json.load(info_file)
          if int(legos['beta version']): return None
          # retrieving information
          with open(legos['commit file']) as commit_file:
               commit_content = commit_file.readlines()
               commit_header = '# ' + commit_content.pop(0)
               commit_content = ''.join(commit_content)
          with open(legos['changelog file']) as changelog_file:
               changelog_content = changelog_file.read()
          # merging and updating information into changelog
          with open(legos['changelog file'], 'w') as changelog_file:
               new_changelog_content = commit_header          \
                                     + '\n`build date: '      \
                                     + legos['build date']    \
                                     + '`\n`build version: '  \
                                     + legos['build version'] \
                                     + '`\n'                  \
                                     + commit_content         \
                                     + '\n---\n\n'            \
                                     + changelog_content
               changelog_file.write(new_changelog_content)
     return None


def copy_sources() -> bool:
     ("Copy the specified source files in 'src.txt' to the build folder.")

     if not os.path.isfile('tools/src.txt'):
          print('Sin archivo \'src.txt\'')
          return False

     with open('tools/src.txt') as sources:
          source_files = sources.readlines()

     with open('tools/_src.txt', 'w') as xcopy:
          for file in source_files:
               if file == '\n': continue
               if file[0] == '#': continue
               file = file[:-1:]
               destination = file.split('\\')
               destination.pop()
               if destination and destination[0] == 'app':
                    destination.pop(0)
               if destination and destination[0] == 'tools':
                    destination.pop(0)
               command = 'xcopy ' + file + ' build\\' + '\\'.join(destination) + '\n'
               xcopy.write(command)

               # crea las carpetas paa que xcopy no se maree
               last_folder = 'build'
               for folder in destination:
                    if not os.path.isdir(last_folder + '/' + folder):
                         os.mkdir(last_folder + '/' + folder)
                    last_folder += '/' + folder

     return True


def compile_project() -> None:
     ("Compile .py files to .pyc files.")
     pass


def pack_it() -> None:
     ("Packs build folder into a zip file.")

     with open('tools\\bdmn.txt') as info_file:
          legos: dict = json.load(info_file)

     os.chdir('build')
     source_files = list(os.walk('.'))
     app_name: str = f"criptosapo-{'-'.join(legos['build version'].split('.'))}.zip"

     with zfile(
          app_name,
          mode = 'w',
          compression = ZIP_DEFLATED,
          compresslevel = 9
     ) as app:
          for path, folders, files in source_files:
               for folder in folders:
                    print(path + '\\' + folder)
                    app.write(path + '\\' + folder)
               for file in files:
                    print(path + '\\' + file)
                    app.write(path + '\\' + file)

     os.chdir('..')

     return None


def build() -> None:
     PROJECT_NAME = 'CriptoSapo'
     INSTRUCTION: str = argv[-1::][0] if len(argv) > 1 else ''
     NOT_READY, UPDATE, COPY, BUILD = 1, 4, 33, 69

     match INSTRUCTION:
          case 'setup':
               print('Checking files and setting up...')
               del_build_content()
               FOLDER_READY = check_build_folder(PROJECT_NAME)
               if not FOLDER_READY:
                    return print(
                         'Build folder initialized.'
                         ' Update your config file.'
                    )
               if not check_app_info():
                    build_notification(NOT_READY)
               build_notification(UPDATE)
          case 'update':
               BUILD_VERSION: str = version_it()
               print('VASDFasdfbaksfbkasef:', BUILD_VERSION)
               update_changelog()
               build_notification(COPY)
          case 'copy':
               if copy_sources(): # done in batch for now
                    build_notification(BUILD)
          case 'build':
               print('Building...')
               compile_project()
               pack_it()
     return None


build()

#ned
