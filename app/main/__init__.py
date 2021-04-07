from flask import Flask
from flask_bcrypt import Bcrypt
from .config import config_by_name
from app.main.database.db import get_db
from flask_pymongo import PyMongo

flask_bcrypt = Bcrypt()
mongo = PyMongo()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    flask_bcrypt.init_app(app)
    with app.app_context():
        # mongo = get_db()
        mongo.init_app(app)
    return app