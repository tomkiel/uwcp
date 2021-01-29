from flask import Blueprint
from app.http.controllers import UserController
user = Blueprint('user', __name__, url_prefix='/api/users')


@user.route("", methods=['GET'])
def root():
    return UserController.get()


@user.route("/create", methods=['POST'])
def create():
    return UserController.create()


@user.route('/<user_id>', methods=['GET'])
def find(user_id):
    return UserController.find(user_id)


@user.route('/update', methods=['PUT'])
def update():
    return UserController.update()


def init_app(app):
    app.register_blueprint(user)

