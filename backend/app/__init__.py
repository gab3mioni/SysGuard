from flask import Flask
from .routes import bp as routes_bp
from .models import db

def create_app():
    app = Flask(__name__)
    app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    db.init_app(app)

    app.register_blueprint(routes_bp)

    return app