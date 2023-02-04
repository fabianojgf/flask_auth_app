from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from . import db
from .models import User, UserType, Permission, PermissionType, PermissionStatus, Department
import os

admin_user = Blueprint('admin_user', __name__)

@admin_user.route('/admin/users')
@login_required
def users():
    nav_levels = ["Área Interna", "Admin", "Usuários"]

    userTypes = UserType.query.filter_by().all()
    users = User.query.filter_by(active=True).all()
    
    return render_template('admin/users/list.html', 
        user = current_user,  
        users = users, 
        userTypes = userTypes, 
        nav_levels = nav_levels)

@admin_user.route('/admin/user/new')
@login_required
def user_new():
    nav_levels = ["Área Interna", "Admin", "Usuários", "Novo"]

    userTypes = UserType.query.filter_by().all()
    
    return render_template('admin/users/form-new.html', 
        userTypes = userTypes, 
        nav_levels = nav_levels)

@admin_user.route('/admin/user/new', methods=['POST'])
@login_required
def user_new_post():
    # code to validate and add user to database goes here
    email = request.form.get('email')
    name = request.form.get('name')
    userTypeId = request.form.get('userTypeSelect',type=int)
    password = request.form.get('password')   
    password_repeat = request.form.get('password-repeat')

    if userTypeId == 0:
        flash('Tipo de Usuário não especificado..', 'error')
        return redirect(url_for('admin_user.user_new'))

    if password != password_repeat:
        flash('A senha e a repetição estão diferentes.', 'error')
        return redirect(url_for('admin_user.user_new'))

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email já cadastrado.', 'error')
        return redirect(url_for('admin_user.user_new'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(name=name, 
        email=email, 
        password=generate_password_hash(password, method='sha256'), 
        user_type_id=userTypeId,
        active=True,
        authorized=False,
        creation_date=datetime.now(), 
        update_date=None)

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('admin_user.users'))