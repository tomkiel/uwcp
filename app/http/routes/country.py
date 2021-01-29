from app.http.controllers import CountryController
from flask import Blueprint

country = Blueprint("country", __name__, url_prefix="/countries")


@country.route("/", methods=["GET"])
def index():
    return CountryController.index()


@country.route("/create", methods=["POST"])
def index():
    return CountryController.create()


@country.route("/<country>", methods=["GET"])
def find(country_id):
    return CountryController.find()


@country.route("/update", methods=["PUT"])
def update():
    return CountryController.update()


def init_app(app):
    app.register_blueprint(country)
