#!/usr/bin/python3
''' routes and views of web page '''
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models import storage
from models.review import Review
from models.place import Place
from models.user import User


@app_views.route('/places/<place_id>/reviews',
                 strict_slashes=False, methods=['GET'])
def route_state_review(place_id):
    ''' all place's object '''
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    reviews = [obj.to_dict() for obj in
               place.reviews if obj.place_id == id]
    return jsonify(reviews)


@app_views.route('/reviews/<review_id>', strict_slashes=False, methods=['GET'])
def route_review_id(review_id):
    ''' search a place with specific id '''
    obj = storage.get(Review, review_id)
    if obj is None:
        abort(404)
    return jsonify(obj.to_dict())


@app_views.route('/reviews/<review_id>',
                 strict_slashes=False, methods=['DELETE'])
def route_review_delete(review_id):
    ''' delete object '''
    obj = storage.get(Review, review_id)
    if obj is None:
        abort(404)
    obj.delete()
    storage.save()
    return jsonify({})


@app_views.route('/places/<place_id>/reviews',
                 strict_slashes=False, methods=['POST'])
def route_review_post(place_id):
    ''' post object '''
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    req = request.get_json()
    if type(req) is not dict:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'user_id' not in req:
        return make_response(jsonify({'error': 'Missing user_id'}), 400)
    print(req)
    user = storage.get(User, req['user_id'])
    if user is None:
        abort(404)
    if 'text' not in req:
        return make_response(jsonify({'error': 'Missing text'}), 400)
    req["place_id"] = place_id
    review = Review(**req)
#    setattr(review, 'place_id', id)
    storage.save()
    return make_response(jsonify(review.to_dict()), 201)


@app_views.route('/reviews/<review_id>', strict_slashes=False, methods=['PUT'])
def route_review_put(review_id):
    ''' search a place with specific id '''
    ignore_values = ['id', 'user_id', 'place_id', 'created_at', 'updated_at']
    req = request.get_json()
    if type(req) is not dict:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    obj = storage.get(Review, review_id)
    if obj is None:
        abort(404)
    for key, value in req.items():
        if key not in ignore_values:
            setattr(obj, key, value)
    obj.save()
    return jsonify(obj.to_dict())
