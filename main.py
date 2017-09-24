from app import create_app
from database import db


if __name__ == "__main__":
    # Running in debug mode
    app = create_app(debug=True)
    db.create_all(app=app)
    app.run()
else:
    # Running from gunicorn
    app = create_app()
