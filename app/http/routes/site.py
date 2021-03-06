from app.http.controllers import SiteController
from flask import Blueprint

site = Blueprint("site", __name__, url_prefix="/sites")


@site.route("/", methods=["GET"])
def get():
    return SiteController.get()


@site.route("/create", methods=["POST"])
def create():
    return SiteController.create()


@site.route("/<site_id>", methods=["GET"])
def find(site_id):
    return SiteController.find()


@site.route("/update", methods=["PUT"])
def update():
    return SiteController.update()


def init_app(app):
    app.register_blueprint(site)
