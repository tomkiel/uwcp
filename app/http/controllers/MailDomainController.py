from app.database.Models.MailDomain import MailDomain
from flask import jsonify, request
from app.utils.helpers import http_error
from app.core.database import db


def get():
    maildomain = MailDomain.query.all() or http_error(204)
    return jsonify({"data": maildomain}), 200


def create():
    return jsonify({"message": "users"})


def find(maildomain_id):
    maildomain = MailDomain.query.filter_by(id=maildomain_id).first() or http_error(204)
    return jsonify({"message": maildomain}), 200


def update():
    return jsonify({"message": "maildomain"}), 200
