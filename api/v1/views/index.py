#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify

"""
creamos nuestra primera vista con el blueprint
que ya creamos
"""


@app_views.route("/status", methods=["GET"])
def index():
    """
    esta vista retorna el estado de la api
    """
    return jsonify({'status': 'OK'})