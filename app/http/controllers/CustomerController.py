from app.database.Models.Customer import Customer
from flask import jsonify, request
from app.utils.helpers import http_error
from app.core.database import db


def get():
    customer = Customer.query.all() or http_error(204)
    return jsonify({"data": customer}), 200


def create():
    return jsonify({"message": "users"})


def find(customer_id):
    customer = Customer.query.filter_by(id=customer_id).first() or http_error(204)
    return jsonify({"message": customer}), 200


def update():
    return jsonify({"message": "customer"}), 200
