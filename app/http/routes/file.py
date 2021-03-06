from app.http.controllers import FileController
from flask import Blueprint

file = Blueprint("file", __name__, url_prefix="/files")


@file.route("/", methods=["GET"])
def get():
    return FileController.get()


@file.route("/create", methods=["POST"])
def create():
    return FileController.create()


@file.route("/<file_id>", methods=["GET"])
def find(file_id):
    return FileController.find()


@file.route("/update", methods=["PUT"])
def update():
    return FileController.update()


def init_app(app):
    app.register_blueprint(file)
