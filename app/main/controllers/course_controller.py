from flask import (
    current_app as app, 
    Blueprint, 
    jsonify,
    request,
    Blueprint,
    make_response
)
from app.main.services.course_service import (
    save_new_course,
    get_course_from_db,
    get_course_detail_from_db,
    save_new_vocabulary_to_course,
    check_course,
    get_vocabulary
)
from app.main.util.decorator import auth_required

course_controller = Blueprint('course_controller', __name__)

@course_controller.route('/courses', methods=['GET'])
@auth_required
def get_course():
    access_level = request.args.get('access_level')
    user_id = request.args.get('create_user_id')

    try:
        all_public_course = get_course_from_db(
            access_level=access_level,
            user_id=user_id
        )
    except:
        response_object = {
                'status': 'fail',
                'message': 'invalid param.',
            }
        return response_object, 422

    if all_public_course != None:
        response_object = {
                'status': 'success',
                'message': 'Successfully get courses.',
                'data': all_public_course
            }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'server error',
        }
        return response_object, 500


@course_controller.route('/courses', methods=['POST'])
@auth_required
def add_new_course():
    """Creates a new User """
    data = request.json
    if save_new_course(data=data) == True:
        response_object = {
                'status': 'success',
                'message': 'Successfully added a course.'
            }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'Course already exists. Please try again.',
        }
        return response_object, 409

@course_controller.route('/courses/<course_id>', methods=['GET'])
@auth_required
def get_course_detail(course_id):
    if course_id == None:
        response_object = {
                'status': 'fail',
                'message': 'invalid param.',
            }
        return response_object, 422

    course_detail = get_course_detail_from_db(course_id)
    response_object = {
            'status': 'sucess',
            'message': 'sucess get course detal.',
            'data': course_detail.__dict__
        }
    return response_object, 200

@course_controller.route('/courses/<course_id>/vocabulary', methods=['POST'])
@auth_required
def add_new_vocabulary(course_id):
    request_body = request.json
    new_vocabulary = request_body['new_vocabulary']
    if course_id == None :
        response_object = {
                'status': 'fail',
                'message': 'invalid param.',
            }
        return response_object, 400

    have_course = check_course(course_id)
    if not have_course:
        response_object = {
                'status': 'fail',
                'message': 'have not course.',
            }
        return response_object, 400

    can_save = save_new_vocabulary_to_course(course_id=course_id, new_vocabulary=new_vocabulary)
    if can_save:  
        response_object = {
                'status': 'sucess',
                'message': 'sucess add vocabulary to course.',
                # 'data': course_detail.__dict__
            }
        return response_object, 200
    else:
        response_object = {
                'status': 'fail',
                'message': 'server error.',
                # 'data': course_detail.__dict__
            }
        return response_object, 500

@course_controller.route('/courses/<course_id>/vocabulary', methods=['GET'])
@auth_required
def get_all_vocabulary_from_course(course_id):
    have_course = check_course(course_id)
    if not have_course:
        response_object = {
                'status': 'fail',
                'message': 'have not course.',
            }
        return response_object, 400

    all_vocabulary = get_vocabulary(course_id=course_id)
    print(all_vocabulary)
    response_object = {
            'status': 'sucess',
            'message': 'sucess get vocabulary.',
            'data': all_vocabulary
        }
    return response_object, 200



