from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate   # type: ignore
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv


import os


load_dotenv('.env')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['UPLOAD_FILES'] = r'static/data'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'index'
bcrypt = Bcrypt(app)


from apps.views import index
from apps.models import Contato
