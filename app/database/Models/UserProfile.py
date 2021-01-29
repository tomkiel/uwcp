from app.core.database import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime
from app.database.Models.User import User
from app.database.Models.Country import Country
from app.database.Models.File import File

Base = declarative_base()


class UserProfile(db.Model, Base, SerializerMixin):
    __tablename__ = "user_profiles"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    gender = db.Column(db.String(10))
    phone_number = db.Column(db.String(255))
    alternative_phone_number = db.Column(db.String(255))
    zip_code = db.Column(db.String(255))
    street = db.Column(db.String(255))
    address_complement = db.Column(db.String(255))
    house_number = db.Column(db.Integer)
    apt_number = db.Column(db.Integer)
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.TIMESTAMP, nullable=False, onupdate=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), index=True)
    user = orm.relationship(User, remote_side=id, back_populates="user_profiles")
    country_id = db.Column(db.Integer, db.ForeignKey("countries.id"), index=True)
    country = orm.relationship(Country, remote_side=id, back_populates="user_profiles")
    file_id = db.Column(db.Integer, db.ForeignKey("files.id"), index=True)
    file = orm.relationship(File, remote_side=id, back_populates="user_profiles")

    def __init__(
        self,
        firstname,
        lastname,
        gender,
        phone_number,
        alternative_phone_number,
        zip_code,
        street,
        address_complement,
        house_number,
        apt_number,
        city,
        state,
    ):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.phone_number = phone_number
        self.alternative_phone_number = alternative_phone_number
        self.zip_code = zip_code
        self.street = street
        self.address_complement = address_complement
        self.house_number = house_number
        self.apt_number = apt_number
        self.city = city
        self.state = state
