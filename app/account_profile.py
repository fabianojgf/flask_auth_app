from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from . import db
from .models import User, Access
import os

account_profile = Blueprint('account_profile', __name__)

@account_profile.route('/profile')
@login_required
def profile():
    return redirect(url_for('account_profile.profile_personal'))

@account_profile.route('/profile/personal')
@login_required
def profile_personal():
    user = User.query.filter_by(id=current_user.id).first()
    if user:
        return render_template('account/profile/personal.html', user = user)
    return 'Unable to get user data.'

@account_profile.route('/profile/personal', methods=['POST'])
@login_required
def profile_personal_post():
    email = request.form.get('email')
    name = request.form.get('name')
    current_password = request.form.get('current-password')

    user = User.query.filter_by(id=current_user.id).first()

    if not check_password_hash(user.password, current_password):
        flash('The current password entered is incorrect.')
        return redirect(url_for('account_profile.profile_personal'))

    user.email = email
    user.name = name
    user.update_date = datetime.now()
    db.session.commit()
    
    return redirect(url_for('account_profile.profile_personal'))

@account_profile.route('/profile/security')
@login_required
def profile_security():
    user = User.query.filter_by(id=current_user.id).first()
    if user:
        return render_template('account/profile/security.html', user = user)
    return 'Unable to get user data.'

@account_profile.route('/profile/security', methods=['POST'])
@login_required
def profile_security_post():
    new_password = request.form.get('new-password')
    new_password_repeat = request.form.get('new-password-repeat')
    current_password = request.form.get('current-password')  

    user = User.query.filter_by(id=current_user.id).first()

    if not check_password_hash(user.password, current_password):
        flash('The current password entered is incorrect.')
        return redirect(url_for('account_profile.profile_security'))

    if new_password != new_password_repeat:
        flash('The new password and confirmation are different')
        return redirect(url_for('account_profile.profile_security'))

    user.password=generate_password_hash(new_password, method='sha256')
    user.update_date = datetime.now()
    db.session.commit()
    
    return redirect(url_for('account_profile.profile_security'))

@account_profile.route('/profile/access')
@login_required
def profile_access():
    accesses = Access.query.filter_by(user_id=current_user.id).all()
    
    return render_template('account/profile/access.html', accesses=accesses)