import uuid
import datetime
import os
import jwt 
import base64

from app.main.database import db
from app.main.models.user import User
from app.main.database.db import get_db
from app.main import mongo
from flask import jsonify, current_app
from app.main.config import key

def save_new_user(data):
    user = None
    if user is None:
        print(data['email'])
    user = mongo.db.user.find_one({'email': data['email']})
    if user is None:
        new_user = User(
            email=data['email'],
            username=data['username'],
            password=base64.b64encode(data['password'].encode()),
            registered_on=datetime.datetime.utcnow()
        )
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


def get_a_user(id):
    return mongo.db.users.find({'_id': id})

def get_a_user_by_email(email):
    return mongo.db.user.find_one({'email': email})

def decode_auth_token(auth_token):
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(auth_token, key)
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'

def encode_auth_token(user_id, email):
    """
    Generates the Auth Token
    :return: string
    """
    print(key)
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=100, seconds=5),
            'iat': datetime.datetime.utcnow(),
            'sub': email + str(user_id)
        }
        return jwt.encode(
            payload,
            key,
            algorithm='HS256'
        )
    except Exception as e:
        return e