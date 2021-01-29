#!/usr/bin/python3

'''
routes and views of web page
'''
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities', strict_slashes=False, methods=['GET'])
def get_amenities():
    ''' busca un usuario a partir de su id '''
    amenities = storage.all("Amenity")
    lista = []
    for amenity in amenities.values():
        lista.append(amenity.to_dict())
    return jsonify(lista)


@app_views.route('/amenities/<amenity_id>',
                 strict_slashes=False, methods=['GET'])
def amenities_id(amenity_id):
    ''' busca un usuario a partir de su id '''
    objeto = storage.get(Amenity, amenity_id)
    if objeto is None:
        abort(404)
    return jsonify(objeto.to_dict())


@app_views.route('/amenities/<amenity_id>',
                 strict_slashes=False, methods=['DELETE'])
def del_amenity_id(amenity_id):
    ''' elimina un user a partir de su id '''
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    amenity.delete()
    storage.save()
    return jsonify({})


@app_views.route('/amenities', strict_slashes=False, methods=['POST'])
def amenity_post():
    '''crear un user a partir de su email y pwd'''
    dic = request.get_json()
    if not dic:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if "name" not in dic:
        return make_response(jsonify({'error': 'Missing email'}), 400)
    new_user = Amenity(**dic)
    new_user.save()
    return make_response(jsonify(new_user.to_dict()), 201)


@app_views.route('/amenities/<amenity_id>',
                 strict_slashes=False, methods=['PUT'])
def update_amenity_id(amenity_id):
    ''' actualiza u user a partir de su pwd '''
    dic = request.get_json()
    amenity = storage.get(Amenity, user_id)
    if amenity is None:
        abort(404)
    if not dic:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for key in dic.keys():
        if key not in ["id", "email", "created_at", "updated_at"]:
            setattr(amenity, key, dic[key])
    amenity.save()
    return jsonify(amenity.to_dict())
