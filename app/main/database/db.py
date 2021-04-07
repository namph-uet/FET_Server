from flask import current_app
from flask_pymongo import PyMongo

def get_db():
    mongodb_client = PyMongo()
    return mongodb_client  