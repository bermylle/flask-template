from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import psycopg2

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

# Import Blueprints Here
from src.user.routes import sample_blueprint


def create_app(config_filename=None):
    
    app = Flask(__name__,template_folder='templates')
    app.config['SECRET_KEY'] = 'sa,ple_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize app 
    db.init_app(app)
  
    app.register_blueprint(sample_blueprint)

    return app