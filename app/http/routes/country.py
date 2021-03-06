from app.http.controllers import CountryController
from flask import Blueprint

country = Blueprint("country", __name__, url_prefix="/api/countries")


@country.route("/", methods=["GET"])
def get():
    return CountryController.get()


@country.route("/create", methods=["POST"])
def create():
    return CountryController.create()


@country.route("/<country_id>", methods=["GET"])
def find(country_id):
    return CountryController.find()


@country.route("/update", methods=["PUT"])
def update():
    return CountryController.update()


def init_app(app):
    app.register_blueprint(country)
