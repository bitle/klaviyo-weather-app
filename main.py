from flask import Flask


def create_app(debug=False):
    app = Flask(__name__)
    app.debug = debug

    return app


if __name__ == "__main__":
    app = create_app(debug=True)
    app.run()
