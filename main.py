from app import create_app


if __name__ == "__main__":
    # Running in debug mode
    app = create_app(debug=True)
    app.run()
else:
    # Running from gunicorn
    app = create_app()
