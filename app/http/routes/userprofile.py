from app.http.controllers import UserProfileController
from flask import Blueprint

userprofile = Blueprint("userprofile", __name__, url_prefix="/api/userprofiles")


@userprofile.route("/", methods=["GET"])
def get():
    return UserProfileController.get()


@userprofile.route("/create", methods=["POST"])
def create():
    return UserProfileController.create()


@userprofile.route("/<userprofile>", methods=["GET"])
def find(userprofile_id):
    return UserProfileController.find()


@userprofile.route("/update", methods=["PUT"])
def update():
    return UserProfileController.update()


def init_app(app):
    app.register_blueprint(userprofile)
