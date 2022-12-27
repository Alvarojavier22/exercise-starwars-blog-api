"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Favorites, Planets, Characters
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/favorites/<int:user_param>')
def get_user_favorite(user_param):
    user_favorites = Favorites.query.filter(Favorites.user_id==user_param).all()
    favorite_list = []
    for i in range(len(user_favorites)):
        favorite_item = user_favorites[i].serialize()

        if (user_favorites[i].favorite_type=='planet'):
            favorite_planet = Planets.query.get(user_favorites[i].favorite_id)
            favorite_item["data"] = favorite_planet.serialize()
        
        if (user_favorites[i].favorite_type == 'character'):
            favorite_character = Characters.query.get(user_favorites[i].favorite_id)
            favorite_item["data"] = favorite_character.serialize()

        favorite_list.append(favorite_item)

    return jsonify(favorite_list)