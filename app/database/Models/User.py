from app.core.database import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime
from app.core.marshmallow import ma

Base = declarative_base()


class User(db.Model, Base, SerializerMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    lastlogin = db.Column(db.TIMESTAMP)
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.TIMESTAMP, nullable=False, onupdate=datetime.utcnow)

    def __init__(self, username, email, password, lastlogin):
        self.username = username
        self.email = email
        self.password = password
        self.lastlogin = lastlogin


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ("id", "username", "email", "lastlogin", "created_at")
        model = User

    id = ma.auto_field()
    username = ma.auto_field()
    email = ma.auto_field()
    lastlogin = ma.auto_field()
    created_at = ma.auto_field()


user_schema = UserSchema()
users_schema = UserSchema(many=True)