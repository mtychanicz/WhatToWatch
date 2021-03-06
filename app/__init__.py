from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

def register_blueprints():
    from .main import home_blueprint, sing_up_blueprint, login_blueprint, account_blueprint, settings_blueprint, \
        how_it_works_blueprint, result_blueprint
    app.register_blueprint(home_blueprint)
    app.register_blueprint(sing_up_blueprint)
    app.register_blueprint(login_blueprint)
    app.register_blueprint(account_blueprint)
    app.register_blueprint(settings_blueprint)
    app.register_blueprint(how_it_works_blueprint)
    app.register_blueprint(result_blueprint)


login_manager = LoginManager()
db = SQLAlchemy()
bcrypt = Bcrypt()
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SECRET_KEY'] = 'secret'
app.debug = True
register_blueprints()

login_manager.init_app(app)
db.init_app(app)
bcrypt.init_app(app)

with app.app_context():
    if not os.path.exists('database.sqlite3'):
        db.create_all(app=app)


