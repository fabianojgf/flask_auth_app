from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_required, current_user
from datetime import datetime
from . import db
from .models import User
from werkzeug.utils import secure_filename
import os

main = Blueprint('main', __name__)

app = Flask(__name__)  

#UPLOAD_FOLDER = 'C:/Users/fabia/DIR_FILES/MinhaUFC/upload/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

HOME_DIR = os.path.expanduser("~")
UPLOAD_FOLDER = os.path.join(HOME_DIR, "DIR_FILES", "MinhaUFC", "upload")

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return 'file uploaded successfully'
    return ''

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/profile/personal')
@login_required
def profile_personal():
    user = User.query.filter_by(id=current_user.id).first()
    if user:
        return render_template('profile/personal.html', user = user)
    return 'Unable to get user data.'

@main.route('/profile/personal', methods=['POST'])
@login_required
def profile_personal_post():
    email = request.form.get('email')
    name = request.form.get('name')

    user = User.query.filter_by(id=current_user.id).first()
    if user:
        user.email = email
        user.name = name
        user.update_date = datetime.now()
        db.session.commit()

    upload_file()
    
    return redirect(url_for('main.profile_personal'))

@main.route('/profile/security')
@login_required
def profile_security():
    return render_template('profile/security.html')

@main.route('/profile/permissions')
@login_required
def profile_permissions():
    return render_template('profile/permissions.html')