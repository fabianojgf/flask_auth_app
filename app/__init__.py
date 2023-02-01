import os
from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.utils import secure_filename

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

     # blueprint for any parts in our app
    from .account_profile import account_profile as account_profile_blueprint
    app.register_blueprint(account_profile_blueprint)
         
    # blueprint for any parts in our app
    from .account_permission import account_permission as account_permission_blueprint
    app.register_blueprint(account_permission_blueprint)

     # blueprint for any parts in our app
    from .permission import permission as permission_blueprint
    app.register_blueprint(permission_blueprint)

    # blueprint for any parts in our app
    from .department import department as department_blueprint
    app.register_blueprint(department_blueprint)

    return app