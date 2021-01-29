from app.database.Models.Costumer import Costumer
from flask import jsonify, request
from app.utils.helpers import http_error
from app.core.database import db


def get():
    costumer = Costumer.query.all() or http_error(204)
    return jsonify({"data": costumer}), 200


def create():
    return jsonify({"message": "users"})


def find(costumer_id):
    costumer = Costumer.query.filter_by(id=costumer_id).first() or http_error(204)
    return jsonify({"message": costumer}), 200


def update():
    return jsonify({"message": "costumer"}), 200
