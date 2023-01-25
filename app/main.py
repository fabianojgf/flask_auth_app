from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/profile/personal')
@login_required
def profilePersonal():
    return render_template('profile/personal.html')

@main.route('/profile/security')
@login_required
def profileSecurity():
    return render_template('profile/security.html')

@main.route('/profile/permissions')
@login_required
def profilePermissions():
    return render_template('profile/permissions.html')