import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import EncryptedType

db = SQLAlchemy()


def get_secret_key():
    return os.getenv('EMAIL_ENCRYPTION_KEY') or "secret_key"


class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(EncryptedType(db.String(255), get_secret_key()), unique=True)
    city = db.Column(db.String(255))

    def __init__(self, email, city):
        self.email = email
        self.city = city
