from app.http.controllers import TemplateController
from flask import Blueprint

template = Blueprint("template", __name__, url_prefix="/templates")


@template.route("/", methods=["GET"])
def get():
    return TemplateController.get()


@template.route("/create", methods=["POST"])
def create():
    return TemplateController.create()


@template.route("/<template_id>", methods=["GET"])
def find(template_id):
    return TemplateController.find()


@template.route("/update", methods=["PUT"])
def update():
    return TemplateController.update()


def init_app(app):
    app.register_blueprint(template)
