import json

from flask import Blueprint, render_template, g

status_apis = Blueprint('status_apis', __name__)
forms = Blueprint('forms', __name__, template_folder='templates')


@status_apis.route('/status')
def status():
    return 'ok'


@forms.route('/')
def signup_form():
    return render_template("signup.html", cities=getattr(g, 'cities', []))


@forms.before_app_first_request
def load_cities():
    with open('cities.json', 'r') as cities_file:
        g.cities = json.load(cities_file)
