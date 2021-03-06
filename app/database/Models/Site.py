from app.core.database import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime
from app.database.Models.Customer import Customer

Base = declarative_base()


class Site(db.Model, Base, SerializerMixin):
    __tablename__ = "sites"
    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.TIMESTAMP, nullable=False, onupdate=datetime.utcnow)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), index=True)
    customer = orm.relationship("Customer")

    def __init__(self, domain):
        self.domain = domain
