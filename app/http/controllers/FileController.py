from app.database.Models.File import File
from flask import jsonify, request
from app.utils.helpers import http_error
from app.core.database import db


def get():
    file = File.query.all() or http_error(204)
    return jsonify({"data": file}), 200


def create():
    return jsonify({"message": "users"})


def find(file_id):
    file = File.query.filter_by(id=file_id).first() or http_error(204)
    return jsonify({"message": file}), 200


def update():
    return jsonify({"message": "file"}), 200
