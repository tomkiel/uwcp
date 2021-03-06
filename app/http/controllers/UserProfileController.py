from app.database.Models.UserProfile import UserProfile
from app.database.Models.Country import Country
from app.database.Models.User import User
from flask import jsonify, request
from app.utils.helpers import http_error
from app.core.database import db


def get():
    userprofile = UserProfile.query.all() or http_error(204)
    return jsonify({"data": userprofile}), 200


def create():
    country_id = None
    user_id = request.json.get('user_id') or None
    username = request.json.get('username') or http_error(500, 'USERNAME is required!')
    email = request.json.get('email') or http_error(500, 'EMAIL is required!')
    password = request.json.get('password') or http_error(500, 'PASSWORD is required!')
    lastname = request.json.get('lastname')
    gender = request.json.get('gender')
    phone_number = request.json.get('phone_number')
    alternative_phone_number = request.json.get('alternative_phone_number')
    zip_code = request.json.get('zip_code')
    street = request.json.get('street')
    address_complement = request.json.get('address')
    house_number = request.json.get('house_number')
    apt_number = request.json.get('apt_number')
    city = request.json.get('city')
    state = request.json.get('state')

    country = Country.query.filter_by(code=request.json.get('country')).first()
    if country:
        country_id = country.id

    user = User.query.filter_by(id=user_id).first()

    return jsonify({"country": country_id, "user": user})


def find(userprofile_id):
    userprofile = UserProfile.query.filter_by(id=userprofile_id).first() or http_error(
        204
    )
    return jsonify({"message": userprofile}), 200


def update():
    return jsonify({"message": "userprofile"}), 200


def login():
    return jsonify({'e': ''}), 200

