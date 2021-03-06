from app.http.controllers import MailDomainController
from flask import Blueprint

maildomain = Blueprint("maildomain", __name__, url_prefix="/maildomains")


@maildomain.route("/", methods=["GET"])
def get():
    return MailDomainController.get()


@maildomain.route("/create", methods=["POST"])
def create():
    return MailDomainController.create()


@maildomain.route("/<maildomain_id>", methods=["GET"])
def find(maildomain_id):
    return MailDomainController.find()


@maildomain.route("/update", methods=["PUT"])
def update():
    return MailDomainController.update()


def init_app(app):
    app.register_blueprint(maildomain)
