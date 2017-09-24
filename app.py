import os
from flask import Flask
from views import status_apis, forms
from database import db


def create_app(debug=False):
    app = Flask(__name__)
    app.debug = debug
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI',
                                                      'postgres://localhost:5432/klaviyo')
    # SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.register_blueprint(status_apis)
    app.register_blueprint(forms)
    db.init_app(app)

    return app
