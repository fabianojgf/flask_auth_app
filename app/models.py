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

class Department(db.Model):
    __tablename__ = 'department'
    __table_args__ = {'schema':'general'}

    id = db.Column(db.Integer, db.Sequence("department_seq", schema="general"), primary_key=True)
    name = db.Column(db.String(200))
    active = db.Column(db.Boolean)  
    creation_date = db.Column(db.Date)
    update_date = db.Column(db.Date)

class PermissionType(db.Model):
    __tablename__ = 'permission_type'
    __table_args__ = {'schema':'general'}

    id = db.Column(db.Integer, db.Sequence("permission_type_seq", schema="general"), primary_key=True)
    description = db.Column(db.String(30))

class Permission(db.Model):
    __tablename__ = 'permission'
    __table_args__ = {'schema':'general'}

    id = db.Column(db.Integer, db.Sequence("permission_seq", schema="general"), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('general.user.id'))
    department_id = db.Column(db.Integer, db.ForeignKey('general.department.id'))
    permission_type_id = db.Column(db.Integer, db.ForeignKey('general.permission_type.id'))
    begin = db.Column(db.Date)
    end = db.Column(db.Date)
    active = db.Column(db.Boolean)  
    authorized = db.Column(db.Boolean)
    creation_date = db.Column(db.Date)
    update_date = db.Column(db.Date)

class Access(db.Model):
    __tablename__ = 'access'
    __table_args__ = {'schema':'general'}

    id = db.Column(db.Integer, db.Sequence("access_seq", schema="general"), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('general.user.id'))
    user = db.relationship("User", backref=db.backref("user", uselist=False))
    address = db.Column(db.String(30))
    user_agent = db.Column(db.String(200))
    date_in = db.Column(db.Date)
    date_out = db.Column(db.Date)
    