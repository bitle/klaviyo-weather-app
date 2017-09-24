from database import db


class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    city = db.Column(db.String(255))

    def __init__(self, email, city):
        self.email = email
        self.city = city
