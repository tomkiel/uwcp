from app.database.Models.User import User
from flask import jsonify, request
from app.utils.helpers import http_error
from app.core.database import db


def get():
    user = User.query.all() or http_error(204)
    return jsonify({"data": user}), 200


def create():
    return jsonify({"message": "users"})


def find(user_id):
    user = User.query.filter_by(id=user_id).first() or http_error(204)
    return jsonify({"message": user}), 200


def update():
    return jsonify({"message": "user"}), 200
