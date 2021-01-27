#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify
from models import storage

"""

Creamos la vista para el modelo cities con ayuda de flask !

"""


@app_views("/cities/<city_id>", methods=["GET"])
def get_cities(id):
    """
    id : será el id correspondiente a cada ciudad
    """
    print("HOLA SOY EL ID:" + id)
    print(dir(storage))
    return "<h1>SOY CITIES UWU</h1>"
