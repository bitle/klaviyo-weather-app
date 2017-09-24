from database import Subscriber, db


def add_subscriber(email, location):
    subscriber = Subscriber(email, location)
    db.session.add(subscriber)
