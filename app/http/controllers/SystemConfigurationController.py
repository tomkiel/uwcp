from app.database.Models.SystemConfiguration import SystemConfiguration
from flask import jsonify, request
from app.utils.helpers import http_error
from app.core.database import db


def get():
    systemconfiguration = SystemConfiguration.query.all() or http_error(204)
    return jsonify({"data": systemconfiguration}), 200


def create():
    return jsonify({"message": "users"})


def find(systemconfiguration_id):
    systemconfiguration = SystemConfiguration.query.filter_by(
        id=systemconfiguration_id
    ).first() or http_error(204)
    return jsonify({"message": systemconfiguration}), 200


def update():
    return jsonify({"message": "systemconfiguration"}), 200
