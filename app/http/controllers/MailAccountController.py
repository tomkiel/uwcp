from app.database.Models.MailAccount import MailAccount
from flask import jsonify, request
from app.utils.helpers import http_error
from app.core.database import db


def get():
    mailaccount = MailAccount.query.all() or http_error(204)
    return jsonify({"data": mailaccount}), 200


def create():
    return jsonify({"message": "users"})


def find(mailaccount_id):
    mailaccount = MailAccount.query.filter_by(id=mailaccount_id).first() or http_error(
        204
    )
    return jsonify({"message": mailaccount}), 200


def update():
    return jsonify({"message": "mailaccount"}), 200
