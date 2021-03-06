from app.http.controllers import AuthController
from flask import Blueprint

auth = Blueprint("auth", __name__, url_prefix="/api/auth")


@auth.route("/check", methods=['POST'])
def exists():
    return AuthController.user_exists()


@auth.route('/login', methods=['POST'])
def login():
    return AuthController.login()


def init_app(app):
    app.register_blueprint(auth)

