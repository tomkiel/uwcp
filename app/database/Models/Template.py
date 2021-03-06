from app.core.database import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime


Base = declarative_base()


class Template(db.Model, Base, SerializerMixin):
    __tablename__ = "templates"
    id = db.Column(db.Integer, primary_key=True)
    limit_web_domain = db.Column(db.Integer)
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.TIMESTAMP, nullable=False, onupdate=datetime.utcnow)

    def __init__(self, limit_web_domain):
        self.limit_web_domain = limit_web_domain
