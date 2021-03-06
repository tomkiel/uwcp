from app.database.Models.User import User, user_schema, token, last_login
from flask import jsonify, request
from app.utils.helpers import http_error, hash_verify


def user_exists():
    username = request.json.get('username') or http_error(500, 'USERNAME is required!')
    user = User.query.filter_by(username=username).first() or http_error(204, 'USERNAME is required!')
    return jsonify({"username": user.username}), 200


def login():
    username = request.json.get('username') or http_error(500, 'USERNAME is required!')
    password = request.json.get('password') or http_error(500, 'PASSWORD is required!')
    user = User.query.filter_by(username=username).first() or http_error(401, 'Unauthorized! USER not found!')
    last_login(username)
    if user.check_password(password):
        return jsonify(
            {
                'user': user_schema.dump(user),
                "token": token(user.id)
            }
        )
    else:
        return http_error(401, 'Unauthorized! PASSWORD not found!')
