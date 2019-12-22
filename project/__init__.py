from flask import request
from flask import jsonify
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from project.config import HOST

load_dotenv(dotenv_path=".env")

### Init App ###
app = Flask(__name__, static_folder='front/static', template_folder='front/templates')

# Database configuration
app.config.from_object('project.config')
db = SQLAlchemy(app, use_native_unicode=True)
migrate = Migrate(app, db)

def getHost(method = ''):
    if (method[0] == '/') and (HOST[-1] == '/'):
        return HOST[:-1] + method
    else:
        return HOST + method

from project.view import views
