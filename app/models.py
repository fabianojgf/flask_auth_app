from flask_login import UserMixin
from app import db

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    __table_args__ = {'schema':'general'}

    id = db.Column(db.Integer, db.Sequence("user_seq", schema="general"), primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(1000))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    active = db.Column(db.Boolean)  
    authorized = db.Column(db.Boolean)
    creation_date = db.Column(db.Date)
    update_date = db.Column(db.Date)
    