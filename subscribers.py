import logging

from sqlalchemy.exc import IntegrityError

from database import Subscriber, db


class SubscriptionError(Exception):
    pass


def add_subscriber(email, location):
    subscriber = Subscriber(email, location)
    db.session.add(subscriber)
    try:
        db.session.commit()
    except IntegrityError, e:
        logger = logging.getLogger(__name__)
        logger.exception("Failed to add a subscriber")
        raise SubscriptionError("Subscriber with this email already exists")
