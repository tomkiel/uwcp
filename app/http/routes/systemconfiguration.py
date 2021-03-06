from app.http.controllers import SystemConfigurationController
from flask import Blueprint

systemconfiguration = Blueprint(
    "systemconfiguration", __name__, url_prefix="/systemconfigurations"
)


@systemconfiguration.route("/", methods=["GET"])
def get():
    return SystemConfigurationController.get()


@systemconfiguration.route("/create", methods=["POST"])
def create():
    return SystemConfigurationController.create()


@systemconfiguration.route("/<systemconfiguration_id>", methods=["GET"])
def find(systemconfiguration_id):
    return SystemConfigurationController.find()


@systemconfiguration.route("/update", methods=["PUT"])
def update():
    return SystemConfigurationController.update()


def init_app(app):
    app.register_blueprint(systemconfiguration)
