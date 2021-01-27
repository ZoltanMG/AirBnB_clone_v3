#!/usr/bin/python3

"""
importamos los modulos necesarios
"""

from flask import Flask, jsonify, make_response
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(404)
def error_handler(e):
    """
    Manejamos el error 404
    de pagina no encontrada
    con make response para asiganar el
    http header error 404
    """
    return make_response(jsonify({"error": "Not found"}), 404)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    ''' main funciton to run flask '''
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
