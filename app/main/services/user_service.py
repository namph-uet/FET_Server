import uuid
import datetime
from app.main.database import db
from app.main.models.user import User
from app.main.database.db import get_db
from app.main import mongo
from flask import jsonify


def save_new_user(data):
    user = None
    if user is None:
        print('hahahahahahah')
    user = mongo.db.users.find_one({'username': data['username']})
    print(user)
    if user is None:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        print(new_user)
        mongo.db.user.insert_one(new_user.__dict__)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    all_user = mongo.db.users.find();
    print(all_user)
    return all_user;


def get_a_user(public_id):
    return mongo.db.users.find({'id': public_id})
