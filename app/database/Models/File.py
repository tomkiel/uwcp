from app.core.database import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime


Base = declarative_base()


class File(db.Model, Base, SerializerMixin):
    __tablename__ = "files"
    id = db.Column(db.Integer, primary_key=True)
    doc_type = db.Column(db.String(255))
    path = db.Column(db.String(255))
    name = db.Column(db.String(255))
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.TIMESTAMP, nullable=False, onupdate=datetime.utcnow)

    def __init__(self, doc_type, path, name):
        self.doc_type = doc_type
        self.path = path
        self.name = name
