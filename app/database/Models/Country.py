from app.core.database import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime


Base = declarative_base()


class Country(db.Model, Base, SerializerMixin):
    __tablename__ = "countries"
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(2), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    phone_code = db.Column(db.String(4))
    code_iso = db.Column(db.String(3))
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.TIMESTAMP, nullable=False, onupdate=datetime.utcnow)

    def __init__(self, code, name, phone_code, code_iso):
        self.code = code
        self.name = name
        self.phone_code = phone_code
        self.code_iso = code_iso
