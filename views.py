import json

from flask import Blueprint, render_template

from cities import get_cities

status_apis = Blueprint('status_apis', __name__)
forms = Blueprint('forms', __name__, template_folder='templates')


@status_apis.route('/status')
def status():
    return 'ok'


@forms.route('/')
def signup_form():
    return render_template("signup.html", cities=get_cities())
