from flask import Blueprint
from app.http.controllers import WebController

web = Blueprint('web', __name__)


@web.route("/", methods=['GET'])
def get():
    return WebController.get()


@web.route("/home", methods=['GET'])
def home():
    return WebController.home()


def init_app(app):
    app.register_blueprint(web)
