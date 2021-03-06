from app.core.database import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime


Base = declarative_base()


class SystemConfiguration(db.Model, Base, SerializerMixin):
    __tablename__ = "system_configurations"
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(255), nullable=False)
    value = db.Column(db.String(255))
    type = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.TIMESTAMP, nullable=False, onupdate=datetime.utcnow)

    def __init__(self, label, value, type):
        self.label = label
        self.value = value
        self.type = type
