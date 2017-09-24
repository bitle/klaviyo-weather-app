from flask import Blueprint

status_apis = Blueprint('status_apis', __name__)


@status_apis.route('/status')
def status():
    return 'ok'
