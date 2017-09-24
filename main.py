from flask import Flask
from views import status_apis


def create_app(debug=False):
    app = Flask(__name__)
    app.debug = debug

    return app


if __name__ == "__main__":
    app = create_app(debug=True)
    app.register_blueprint(status_apis)
    app.run()
