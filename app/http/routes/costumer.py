from app.http.controllers import CostumerController
from flask import Blueprint

costumer = Blueprint("costumer", __name__, url_prefix="/costumers")


@costumer.route("/", methods=["GET"])
def index():
    return CostumerController.index()


@costumer.route("/create", methods=["POST"])
def index():
    return CostumerController.create()


@costumer.route("/<costumer>", methods=["GET"])
def find(costumer_id):
    return CostumerController.find()


@costumer.route("/update", methods=["PUT"])
def update():
    return CostumerController.update()


def init_app(app):
    app.register_blueprint(costumer)
