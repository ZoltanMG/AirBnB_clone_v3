#!/usr/bin/python3
""" creamos nuestra primera ruta """
from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status", methods=["GET"])
def index():
    """
    esta vista retorna el estado de la api
    """
    return jsonify({'status': 'OK'})
