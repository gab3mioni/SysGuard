from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ContainerLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    container_name = db.Column(db.String(128), nullable=False)
    action = db.Column(db.String(128), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=db.func.now())