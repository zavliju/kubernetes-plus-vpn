import logging
import json
from api.filter import Filter
from api import config

from flask import Flask, Response, jsonify, request, send_file
from flask_restful import Api

import traceback
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

app.logger.addHandler(logging.StreamHandler())
app.logger.setLevel(logging.INFO)
app.config['DEBUG'] = True


@app.route('/')
def check():
    metadata = {'status': '200', 'message': 'cari apa?'}
    return Response(json.dumps(metadata), status=200, mimetype='application/json')

@app.route('/ovpn)
def info():
    metadata = {'name': 'ubernetes-plus-vpn', 'version': '0.1.0', 'api': ['/ovpn']}
    return Response(json.dumps(metadata), status=200, mimetype='application/json')

@app.errorhandler(404)
def page_not_found(e):
    metadata = {'status': '404', 'message': 'mau cari apa?'}
    return Response(json.dumps(metadata), status=404, mimetype='application/json')

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0')

