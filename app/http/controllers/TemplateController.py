from app.database.Models.Template import Template
from flask import jsonify, request
from app.utils.helpers import http_error
from app.core.database import db


def get():
    template = Template.query.all() or http_error(204)
    return jsonify({"data": template}), 200


def create():
    return jsonify({"message": "users"})


def find(template_id):
    template = Template.query.filter_by(id=template_id).first() or http_error(204)
    return jsonify({"message": template}), 200


def update():
    return jsonify({"message": "template"}), 200
