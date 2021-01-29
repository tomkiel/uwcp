from app.database.Models.Country import Country
from flask import jsonify, request
from app.utils.helpers import http_error
from app.core.database import db


def get():
    country = Country.query.all() or http_error(204)
    return jsonify({"data": country}), 200


def create():
    return jsonify({"message": "users"})


def find(country_id):
    country = Country.query.filter_by(id=country_id).first() or http_error(204)
    return jsonify({"message": country}), 200


def update():
    return jsonify({"message": "country"}), 200
