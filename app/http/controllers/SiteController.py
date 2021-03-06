from app.database.Models.Site import Site
from flask import jsonify, request
from app.utils.helpers import http_error
from app.core.database import db


def get():
    site = Site.query.all() or http_error(204)
    return jsonify({"data": site}), 200


def create():
    return jsonify({"message": "users"})


def find(site_id):
    site = Site.query.filter_by(id=site_id).first() or http_error(204)
    return jsonify({"message": site}), 200


def update():
    return jsonify({"message": "site"}), 200
