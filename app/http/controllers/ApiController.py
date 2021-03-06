from flask import jsonify, request
from app.utils.helpers import http_error, hash_verify
from app.database.Models.User import User, token, user_schema
import jwt


def index():
    """Return Welcomme message"""
    return jsonify(
        {
            'status': 'ok',
            'message': 'Tudo funcionando por aqui!'
        }
    )
