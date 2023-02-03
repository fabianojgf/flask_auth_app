from flask_login import UserMixin
from enum import Enum
from datetime import date
from app import db

class UserType(db.Model):
    __tablename__ = 'user_type'
    __table_args__ = {'schema':'general'}

    id = db.Column(db.Integer, db.Sequence("user_type_seq", schema="general"), primary_key=True)
    description = db.Column(db.String(30))

    ADMIN = 1
    COMMON = 2    

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    __table_args__ = {'schema':'general'}

    id = db.Column(db.Integer, db.Sequence("user_seq", schema="general"), primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(1000))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    user_type_id = db.Column(db.Integer, db.ForeignKey('general.user_type.id'))   
    user_type = db.relationship("UserType", backref=db.backref("user_type", uselist=False)) 
    active = db.Column(db.Boolean)  
    authorized = db.Column(db.Boolean)
    creation_date = db.Column(db.Date)
    update_date = db.Column(db.Date)

    @property
    def creation_date_str(self):
        return self.creation_date.strftime("%d/%m/%Y")
    @property
    def is_admin(self):
        return self.type == UserType.ADMIN
    @property
    def is_active(self):
        return self.active
    @property
    def is_authorized(self):
        return self.authorized

class Department(db.Model):
    __tablename__ = 'department'
    __table_args__ = {'schema':'general'}

    id = db.Column(db.Integer, db.Sequence("department_seq", schema="general"), primary_key=True)
    name = db.Column(db.String(200))
    parent_id = db.Column(db.Integer, db.ForeignKey('general.department.id'))
    active = db.Column(db.Boolean)  
    creation_date = db.Column(db.Date)
    update_date = db.Column(db.Date)

    children = db.relationship('Department', backref=db.backref('parent', remote_side=[id]))

class PermissionType(db.Model):
    __tablename__ = 'permission_type'
    __table_args__ = {'schema':'general'}

    id = db.Column(db.Integer, db.Sequence("permission_type_seq", schema="general"), primary_key=True)
    description = db.Column(db.String(30))

class PermissionStatus(db.Model):
    __tablename__ = 'permission_status'
    __table_args__ = {'schema':'general'}

    id = db.Column(db.Integer, db.Sequence("permission_status_seq", schema="general"), primary_key=True)
    description = db.Column(db.String(30))

class Permission(db.Model):
    __tablename__ = 'permission'
    __table_args__ = {'schema':'general'}

    id = db.Column(db.Integer, db.Sequence("permission_seq", schema="general"), primary_key=True)   
    user_id = db.Column(db.Integer, db.ForeignKey('general.user.id'))
    user = db.relationship("User", backref=db.backref("user", uselist=False))   
    department_id = db.Column(db.Integer, db.ForeignKey('general.department.id'))   
    department = db.relationship("Department", backref=db.backref("department", uselist=False))   
    permission_type_id = db.Column(db.Integer, db.ForeignKey('general.permission_type.id'))   
    permission_type = db.relationship("PermissionType", backref=db.backref("permission_type", uselist=False))   
    permission_status_id = db.Column(db.Integer, db.ForeignKey('general.permission_status.id'))   
    permission_status = db.relationship("PermissionStatus", backref=db.backref("permission_status", uselist=False)) 
    begin = db.Column(db.Date)
    end = db.Column(db.Date)
    active = db.Column(db.Boolean)
    creation_date = db.Column(db.Date)
    update_date = db.Column(db.Date)

class Access(db.Model):
    __tablename__ = 'access'
    __table_args__ = {'schema':'general'}

    id = db.Column(db.Integer, db.Sequence("access_seq", schema="general"), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('general.user.id'))
    user = db.relationship("User")
    address = db.Column(db.String(30))
    user_agent = db.Column(db.String(200))
    date_in = db.Column(db.Date)
    date_out = db.Column(db.Date)
    