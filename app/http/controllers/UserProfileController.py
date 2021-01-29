from app.database.Models.UserProfile import UserProfile
from flask import jsonify, request
from app.utils.helpers import http_error
from app.core.database import db


def get():
    userprofile = UserProfile.query.all() or http_error(204)
    return jsonify({"data": userprofile}), 200


def create():
    return jsonify({"message": "users"})


def find(userprofile_id):
    userprofile = UserProfile.query.filter_by(id=userprofile_id).first() or http_error(
        204
    )
    return jsonify({"message": userprofile}), 200


def update():
    return jsonify({"message": "userprofile"}), 200
