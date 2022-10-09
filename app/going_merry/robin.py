import os, json
from flask import (
     Flask, request, render_template,
     url_for, redirect, jsonify
)

app = Flask(__name__, template_folder='treasures')


@app.errorhandler(404)
def go_default(error):
     return 'notmyproblem .!.', 404


@app.route('/')
def home(): return render_template('bird.html')


def sanji(kick_in_the_face: str|None = None) -> dict|None:
     ("Robin's dog.")
     if kick_in_the_face == 'Robin: Find my wallet!':
          if os.path.isdir('action'):
               os.chdir('action')
               print('Focus changed to actions folder.')
               print(os.getcwd())
     else:
          if os.path.isfile('../db/chauchero'):
               wallet = open('../db/chauchero', 'r')
               pocket = json.load(wallet)
          else:
               pocket = {}
          return pocket
     return None


@app.route('/wallet/', methods=['POST', 'GET'])#, 'PUT', 'DELETE'])
def api():
     sanji('Robin: Find my wallet!')
     my_pocket: dict
     if request.method == 'POST':
          if request.is_json:
               if request.json['action'] == 'buy':
                    os.system('start buy')
               elif request.json['action'] == 'sell':
                    os.system('start sell')
               # elif request.json['action'] == 'ship':
               #      os.system('start ship')
               # elif request.json['action'] == 'spy':
               #      os.system('start spy')
               my_pocket = sanji().get('coin', 'No existe la chauchera!!')
     elif request.method == 'GET':
          my_pocket = sanji()
     elif request.method == 'PUT':
          ...
     elif request.method == 'DELETE':
          ...
     return jsonify(my_pocket)


if __name__ == '__main__':
     app.run(debug=True, port=7777, host='0.0.0.0')

#ned
