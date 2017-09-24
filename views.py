from flask import Blueprint, render_template, request

from cities import get_cities
from subscribers import add_subscriber, SubscriptionError

status_apis = Blueprint('status_apis', __name__)
forms = Blueprint('forms', __name__, template_folder='templates')


@status_apis.route('/status')
def status():
    return 'ok'


@forms.route('/')
def signup_form(error=None):
    return render_template("signup.html", cities=get_cities(), error=error)


@forms.route('/', methods=['POST'])
def signup_form_submit():
    email = request.form['email']
    location = request.form['location']

    try:
        add_subscriber(email, location)
    except SubscriptionError:
        return signup_form(error="Subscriber with this email already exists")

    return signup_form()
