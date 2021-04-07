from flask import request
from flask_restful import Resource, Api
from app.main.services.user_service import save_new_user, get_a_user, get_all_users
from flask import current_app as app
from flask import Blueprint
from flask import jsonify

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/')
def get_user_list():
    all_user = get_all_users()
    return jsonify(all_user)


@user_controller.route('/', methods=['POST'])
def post():
    """Creates a new User """
    data = request.json
    return save_new_user(data=data)


# @user_controller.route('/<public_id>')
# @user_controller.param('public_id', 'The User identifier')
# @user_controller.response(404, 'User not found.')
# def get(self, public_id):
#     """get a user given its identifier"""
#     user = get_a_user(public_id)
#     if not user:
#         app.abort(404)
#     else:
#         return user