from app.http.controllers import MailAccountController
from flask import Blueprint

mailaccount = Blueprint("mailaccount", __name__, url_prefix="/mailaccounts")


@mailaccount.route("/", methods=["GET"])
def get():
    return MailAccountController.get()


@mailaccount.route("/create", methods=["POST"])
def create():
    return MailAccountController.create()


@mailaccount.route("/<mailaccount_id>", methods=["GET"])
def find(mailaccount_id):
    return MailAccountController.find()


@mailaccount.route("/update", methods=["PUT"])
def update():
    return MailAccountController.update()


def init_app(app):
    app.register_blueprint(mailaccount)
