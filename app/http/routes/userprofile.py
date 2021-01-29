from app.http.controllers import UserprofileController
from flask import Blueprint

userprofile = Blueprint("userprofile", __name__, url_prefix="/userprofiles")


@userprofile.route("/", methods=["GET"])
def index():
    return UserprofileController.index()


@userprofile.route("/create", methods=["POST"])
def index():
    return UserprofileController.create()


@userprofile.route("/<userprofile>", methods=["GET"])
def find(userprofile_id):
    return UserprofileController.find()


@userprofile.route("/update", methods=["PUT"])
def update():
    return UserprofileController.update()


def init_app(app):
    app.register_blueprint(userprofile)
