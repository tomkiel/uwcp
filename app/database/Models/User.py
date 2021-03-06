from dynaconf import settings
from app.core.database import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timedelta
from app.core.marshmallow import ma
from app.database.Models.UserProfile import UserProfile
from app.utils.helpers import hash_create, hash_verify
import jwt

Base = declarative_base()


class User(db.Model, Base, SerializerMixin):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    lastlogin = db.Column(db.TIMESTAMP)
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.TIMESTAMP, nullable=False, onupdate=datetime.utcnow)
    profile = orm.relationship(UserProfile, back_populates="user", uselist=False)

    def __init__(self, username, email, password, lastlogin=None):
        self.username = username
        self.email = email
        self.set_password(password)
        self.lastlogin = lastlogin

    def set_password(self, secret):
        self.password = hash_create(secret)

    def check_password(self, secret):
        return hash_verify(self.password, secret)


def last_login(username):
    user = User.query.filter_by(username=username).update(dict(lastlogin=datetime.utcnow()))
    db.session.commit()
    return user


def token(user, time=60):
    payload = {"id": user, "exp": datetime.utcnow() + timedelta(minutes=time)}
    return jwt.encode(payload, settings.SECRET_KEY).decode('utf-8')


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ("id", "username", "email", "lastlogin", "created_at", "profile")
        model = User

    id = ma.auto_field()
    username = ma.auto_field()
    email = ma.auto_field()
    lastlogin = ma.auto_field()
    created_at = ma.auto_field()


user_schema = UserSchema()
users_schema = UserSchema(many=True)
