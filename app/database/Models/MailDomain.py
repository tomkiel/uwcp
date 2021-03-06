from app.core.database import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime
from app.database.Models.Customer import Customer

Base = declarative_base()


class MailDomain(db.Model, Base, SerializerMixin):
    __tablename__ = "mail_domains"
    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(255), nullable=False)
    policy = db.Column(db.Boolean)
    dkim = db.Column(db.Boolean)
    dkim_selector = db.Column(db.String(255))
    dkim_private = db.Column(db.Text())
    dns_record = db.Column(db.Text())
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.TIMESTAMP, nullable=False, onupdate=datetime.utcnow)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), index=True)
    customer = orm.relationship("Customer")

    def __init__(self, domain, policy, dkim, dkim_selector, dkim_private, dns_record):
        self.domain = domain
        self.policy = policy
        self.dkim = dkim
        self.dkim_selector = dkim_selector
        self.dkim_private = dkim_private
        self.dns_record = dns_record
