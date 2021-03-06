from app.core.database import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime
from app.database.Models.MailDomain import MailDomain

Base = declarative_base()


class MailAccount(db.Model, Base, SerializerMixin):
    __tablename__ = "mail_accounts"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email_account = db.Column(db.String(255), unique=True, nullable=False)
    email_password = db.Column(db.String(255), nullable=False)
    quota = db.Column(db.Float)
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.TIMESTAMP, nullable=False, onupdate=datetime.utcnow)
    mail_domain_id = db.Column(db.Integer, db.ForeignKey("mail_domains.id"), index=True)
    mail_domain = orm.relationship(MailDomain)

    def __init__(self, name, email_account, email_password, quota):
        self.name = name
        self.email_account = email_account
        self.email_password = email_password
        self.quota = quota
