from flask import Flask
from .routes import register_routes
from .database import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.settings.Config')

    db.init_app(app)

    with app.app_context():
        db.create_all()

    register_routes(app)

    return app