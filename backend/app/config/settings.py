class Config:
    def __init__(self):
        self.JSONIFY_PRETTYPRINT_REGULAR = True
        self.SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False