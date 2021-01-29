from app.http.controllers import FileController
from flask import Blueprint

file = Blueprint("file", __name__, url_prefix="/files")


@file.route("/", methods=["GET"])
def index():
    return FileController.index()


@file.route("/create", methods=["POST"])
def create():
    return ''


def init_app(app):
    app.register_blueprint(file)
