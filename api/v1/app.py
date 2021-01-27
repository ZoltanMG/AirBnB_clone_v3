#!/usr/bin/python3

"""
importamos los modulos necesarios
"""

from flask import Flask, jsonify, make_response
from models import storage
from api.v1.views import app_views
import os

"""
creamos la instancia app de la clase Flask
"""

app = Flask(__name__)
"""
Con esto tenemos el blueprint, que va a haber que registrar en nuestra
aplicación para que esta añada sus rutas a una ruta base,
que en este caso, no está declarada. Esto hará que se registren en "/"
"""
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


if __name__ == "__main__":
    # obtenemos la variable de entorno
    host = os.environ.get('HBNB_API_HOST')
    if host is None:
        host = "0.0.0.0"
    port = os.environ.get('HBNB_API_PORT')
    if port is None:
        port = 5000
    """
    agregamos este ultimo parametro para que flask
    pueda manejar multiples solicitudes al tiempo
    y no en paralelo!
    """
    app.run(host=host, port=port, threaded=True)
