from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from datetime import datetime
from .models import User, Access
from . import db

auth = Blueprint('auth', __name__)

# LOGIN #

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    # login code goes here
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page

    if not user.authorized:
        flash('The user is not authorized.')
        return redirect(url_for('auth.login')) # if the user exists, but is not authorized.

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    
    new_access = Access(user_id=user.id,
        user_agent=request.user_agent.string,
        address=request.remote_addr,
        date_in=datetime.now(),
        date_out=None)

    # add the new access to the database
    db.session.add(new_access)
    db.session.commit()

    session['user_firstname'] = user.name.split()[0]
    session['access_id'] = new_access.id
    session['access_begin'] = new_access.date_in

    return redirect(url_for('main.profile'))

# SIGNUP #

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')   
    password_repeat = request.form.get('password-repeat')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    if password != password_repeat:
        flash('The password and confirmation are different')
        return redirect(url_for('auth.signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(name=name, 
        email=email, 
        password=generate_password_hash(password, method='sha256'), 
        type=2,
        active=True,
        authorized=False,
        creation_date=datetime.now(), 
        update_date=None)

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

# LOGOUT #

@auth.route('/logout')
@login_required
def logout():
    logout_user()

    if 'access_id' in session:
        access_id = session['access_id']
        access = Access.query.filter_by(id=access_id).first()
        if access:
            access.date_out = datetime.now()
            db.session.commit()

        session.pop('access_id', None)
        session.pop('access_begin', None)

    return redirect(url_for('main.index'))