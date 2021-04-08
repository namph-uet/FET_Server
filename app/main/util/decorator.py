from functools import wraps
from flask import request
from app.main.services.user_service import validate_jwt

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not validate_jwt(request):
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401

        return f(*args, **kwargs)

    return decorated