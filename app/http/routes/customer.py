from app.http.controllers import CustomerController
from flask import Blueprint

customer = Blueprint("customer", __name__, url_prefix="/customers")


@customer.route("/", methods=["GET"])
def get():
    return CustomerController.get()


@customer.route("/create", methods=["POST"])
def create():
    return CustomerController.create()


@customer.route("/<customer_id>", methods=["GET"])
def find(customer_id):
    return CustomerController.find()


@customer.route("/update", methods=["PUT"])
def update():
    return CustomerController.update()


def init_app(app):
    app.register_blueprint(customer)
