from app import create_app
from database import Subscriber
from wunderground import get_current_conditions, get_average_temperature


def create_subject(current_temperature, average_temperature, condition):
    if condition == 'Clear' or average_temperature + 5 <= current_temperature:
        return "It's nice out! Enjoy a discount on us."
    elif "Rain" in condition or current_temperature <= average_temperature - 5:
        return "Not so nice out? That's okay, enjoy a discount on us."
    else:
        return "Enjoy a discount on us."


def create_email(city, state):
    current_temperature, condition = get_current_conditions(city, state)
    average_temperature = get_average_temperature(city, state)

    subject = create_subject(current_temperature, average_temperature, condition)
    body = "Current temperature in {city}, {state} is {current_temperature}, {condition}."\
        .format(city=city,
                state=state,
                current_temperature=current_temperature,
                condition=condition)
    return subject, body


def send_email(email, location):
    city, state = location.split(', ')

    subject, body = create_email(city, state)

    print "%s - %s\n\t%s" % (email, subject, body)


def send_emails():
    # I need this Flask app, because I made a mistake of using Flask-Sqlalchemy
    flask_app = create_app()
    with flask_app.app_context():
        subscribers = Subscriber.query.all()
        for subscriber in subscribers:
            send_email(subscriber.email, subscriber.city)
