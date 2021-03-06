from app.core.database import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime
from app.database.Models.User import User
from app.database.Models.Country import Country

Base = declarative_base()


class Customer(db.Model, Base, SerializerMixin):
    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key=True)
    costumer_name = db.Column(db.String(255), nullable=False)
    costumer_code = db.Column(db.String(255), unique=True, nullable=False)
    language = db.Column(db.String(255))
    street = db.Column(db.String(255))
    zip_code = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    added_by = db.Column(db.String(255), nullable=False)
    notes = db.Column(db.Text())
    locked = db.Column(db.Boolean, default=False)
    canceled = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.TIMESTAMP, nullable=False, onupdate=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), index=True)
    user = orm.relationship("User")
    country_id = db.Column(db.Integer, db.ForeignKey("countries.id"), index=True)
    country = orm.relationship("Country")

    def __init__(
        self,
        costumer_name,
        costumer_code,
        language,
        street,
        zip_code,
        city,
        state,
        added_by,
        notes,
        locked,
        canceled,
    ):
        self.costumer_name = costumer_name
        self.costumer_code = costumer_code
        self.language = language
        self.street = street
        self.zip_code = zip_code
        self.city = city
        self.state = state
        self.added_by = added_by
        self.notes = notes
        self.locked = locked
        self.canceled = canceled
