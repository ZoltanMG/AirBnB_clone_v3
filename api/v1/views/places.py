#!/usr/bin/python3
"""
route and views of website
"""

from api.v1.views import app_views
from flask import abort, jsonify, request, make_response
from models import storage
from models.place import Place
from models.city import City
from models.user import User


@app_views.route("/cities/<city_id>/places", methods=["GET"],
                 strict_slashes=False)
def get_places(city_id):
    """
    busca todos los lugares a partir de una ciudad
    """
    objeto = storage.get(City, city_id)
    if objeto is None:
        abort(404)
    all_places = [place.to_dict() for place in objeto.places]
    return jsonify(all_places)


@app_views.route("/places/<place_id>", methods=["GET"], strict_slashes=False)
def get_place(place_id):
    """
    busca un lugar a partir del id
    """
    places = storage.get(Place, place_id)
    if places is None:
        abort(404)
    return jsonify(places.to_dict())


@app_views.route("/places/<place_id>", methods=["DELETE"],
                 strict_slashes=False)
def delete_place(place_id):
    """
    elimina una lugar
    """
    objeto = storage.get(Place, place_id)
    if objeto is None:
        abort(404)
    objeto.delete()
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route("/cities/<city_id>/places", methods=["POST"],
                 strict_slashes=False)
def create_place(city_id):
    """
    crea y devuelve un lugar
    """
    objeto_city = storage.get(City, city_id)
    if objeto_city is None:
        abort(404)
    dic = request.get_json()
    if not dic:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if "user_id" not in dic:
        return make_response(jsonify({'error': 'Missing user_id'}), 400)
    objeto_user = storage.get(User, dic["user_id"])
    if objeto_user is None:
        abort(404)
    if 'name' not in dic:
        return make_response(jsonify({'error': 'Missing name'}), 400)
    dic['city_id'] = city_id
    place = Place(**dic)
    place.save()
    return make_response(jsonify(place.to_dict()), 201)


@app_views.route("/places/<place_id>", methods=["PUT"], strict_slashes=False)
def update_place(place_id):
    """
    actuaiza un lugar
    """
    objeto = storage.get(Place, place_id)
    if objeto is None:
        abort(404)
    dic = request.get_json()
    if not dic:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for key in dic.keys():
        if key not in ["id", "state_id", "created_at", "updated_at"]:
            setattr(objeto, key, dic[key])
    objeto.save()
    return jsonify(objeto.to_dict())
