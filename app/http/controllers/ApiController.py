from flask import jsonify


def index():
    """Return Welcomme message"""
    return jsonify(
        {
            'status': 'ok',
            'message': 'Tudo funcionando por aqui!'
        }
    )


def login():
    return jsonify(
        {
            "targetUrl": "",
            "success": "true",
            "error": "",
            "unAuthorizedRequest": "false",
            "__abp": "true"
        }
    )
