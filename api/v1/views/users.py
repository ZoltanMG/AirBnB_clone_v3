#!/usr/bin/python3

''' routes and views of web page '''
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models import storage
from models.user import User
from models.state import State


@app_views.route('/users', strict_slashes=False, methods=['GET'])
def list_users():
    ''' busca un usuario a partir de su id '''
    users = storage.all("User")
    lista = []
    for user in users.values():
        lista.append(user.to_dict())
    return jsonify(lista)


@app_views.route('/users/<user_id>', strict_slashes=False, methods=['GET'])
def user_id(user_id):
    ''' busca un usuario a partir de su id '''
    objeto = storage.get(User, user_id)
    if objeto is None:
        abort(404)
    return jsonify(objeto.to_dict())


@app_views.route('/users/<user_id>', strict_slashes=False, methods=['DELETE'])
def del_user_id(user_id):
    ''' elimina un user a partir de su id '''
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    user.delete()
    storage.save()
    return jsonify({})


@app_views.route('/users/<user_id>', strict_slashes=False, methods=['PUT'])
def update_user_id(user_id):
    ''' actualiza u user a partir de su pwd '''
    dic = request.get_json()
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    if not dic:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for key in dic.keys():
        if key not in ["id", "email", "created_at", "updated_at"]:
            setattr(user, key, dic[key])
    user.save()
    return jsonify(user.to_dict())


@app_views.route('/users', strict_slashes=False, methods=['POST'])
def user_post():
    '''crear un user a partir de su email y pwd'''
    dic = request.get_json()
    if not dic:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if "email" not in dic:
        return make_response(jsonify({'error': 'Missing email'}), 400)
    if "password" not in dic:
        return make_response(jsonify({'error': 'Missing password'}), 400)
    new_user = User(**dic)
    print(User(**dic))
    new_user.save()
    return make_response(jsonify(new_user.to_dict()), 201)
