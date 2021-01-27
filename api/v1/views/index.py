#!/usr/bin/python3
""" creamos nuestra primera ruta """
from api.v1.views import app_views
from flask import jsonify
from models import storage

classes = {
    "amenities": "Amenity",
    "cities": "City",
    "places": "Place",
    "reviews": "Review",
    "states": "State",
    "users": "User"
}

@app_views.route("/status", methods=["GET"])
def index():
    """
    esta vista retorna el estado de la api
    """
    return jsonify({'status': 'OK'})

@app_views.route('/stats', strict_slashes=False)
def stats():
    """
    esta vista retorna la cantidad de registros segunla clase
    """
    new_dict = {}
    for key, value in classes.items():
        new_dict[key] = storage.count(value)
    return jsonify(new_dict)
