from flask import Flask
from views import status_apis


def create_app(debug=False):
    app = Flask(__name__)
    app.debug = debug
    app.register_blueprint(status_apis)

    return app
