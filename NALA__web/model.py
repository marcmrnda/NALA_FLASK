from . import db
from sqlalchemy.sql import func

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    emailAddress = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    account_type = db.Column(db.String(10), default="User")
    created = db.Column(db.DateTime(timezone=True), default=func.now())