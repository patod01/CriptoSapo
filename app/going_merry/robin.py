import os, json
from flask import (
     Flask, request, render_template,
     url_for, redirect, jsonify
)

app = Flask(__name__, template_folder='treasures')

@app.errorhandler(404)
def go_default(error):
     return 'notmyproblem', 404

@app.route('/')
def home():
     return render_template('bird.html')

@app.route('/wallet/', methods=['POST', 'GET', 'PUT', 'DELETE'])
def api():
     print(os.getcwd())
     if request.method == 'POST':
          ...
     elif request.method == 'GET':
          if os.path.isdir('action'):
               os.chdir('action')
               print('Focus changed to actions folder.')
               print(os.getcwd())
          if os.path.isfile('../db/chauchero'):
               wallet = open('../db/chauchero', 'r')
               respuesta = json.load(wallet)
          else:
               respuesta = 'no existe la chauchera!!'
     elif request.method == 'PUT':
          ...
     elif request.method == 'DELETE':
          ...
     return jsonify(respuesta)

if __name__ == '__main__':
     app.run(debug=True, port=7777, host='0.0.0.0')

#ned
