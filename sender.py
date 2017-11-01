import os

import requests
from requests.auth import HTTPBasicAuth

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


def send_email_console(email, location):
    city, state = location.split(', ')

    subject, body = create_email(city, state)

    print "%s - %s\n\t%s" % (email, subject, body)


def send_email_mailgun(email, location):
    base_url = "https://api.mailgun.net/v3/mg.suleymanov.us"
    api_key = os.getenv('MAILGUN_API_KEY')
    email_from = 'damir@suleymanov.us'

    if not api_key:
        raise ValueError("Please provide MAILGUN_API_KEY")

    city, state = location.split(', ')
    subject, body = create_email(city, state)

    email_data = {
        'from': email_from,
        'to': email,
        'subject': subject,
        'text': body,
        # 'o:testmode': 'yes'
    }

    url = "%s/messages" % base_url
    response = requests.post(url, auth=HTTPBasicAuth("api", api_key),
                             data=email_data)
    if response.status_code == 400:
        print "Bad Request - Often missing a required parameter"
    elif response.status_code == 401:
        print "Unauthorized - No valid API key provided"
    elif response.status_code == 402:
        print "Request Failed - Parameters were valid but request failed"
    elif response.status_code == 404:
        print "Not Found - The requested item doesn't exist"
    elif response.status_code in [500, 502, 503, 504]:
        print "Server Errors - something is wrong on Mailgun's end"

    print "Sent an email to %s" % email


def send_emails():
    # I need this Flask app, because I made a mistake of using Flask-Sqlalchemy
    flask_app = create_app()
    with flask_app.app_context():
        subscribers = Subscriber.query.all()
        for subscriber in subscribers:
            send_email_mailgun(subscriber.email, subscriber.city)
