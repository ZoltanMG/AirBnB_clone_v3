#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.city import City

"""

Creamos la vista para el modelo cities con ayuda de flask !

"""


@app_views.route("/cities/<id>", methods=["GET"])
def get_cities(id):
    """
    id : será el id correspondiente a cada ciudad
    """
    objeto = storage.get(City, id)
    print(objeto.to_dict())
    return "<h1>SOY CITIES UWU</h1>"
