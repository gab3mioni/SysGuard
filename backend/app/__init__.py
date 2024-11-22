from flask import Flask
from flask_cors import CORS
from .routes import register_routes
from .database import db
from .config.settings import Config

def create_app():
    config = Config()
    app = Flask(__name__)

    CORS(app, resources={r"/api/*": {"origins": "http://localhost:3001"}})
    app.config.from_object(config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    register_routes(app)

    return app