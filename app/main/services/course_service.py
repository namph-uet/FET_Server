from app.main import mongo
from app.main.models.course import Course
from app.main.util.course_util import AccessLevel
from app.main.models.course_detail import CourseDetail

def save_new_course(data):
    course = mongo.db.course.find_one({
        'course_name': data['course_name'],
        'user_id': data['user_id']
    })
    if course is None:
        new_course = Course(
            course_name=data['course_name'],
            learn_language=data['learn_language'],
            access_level=data['access_level']
        )
        mongo.db.user.insert_one(new_course.__dict__)
        return True
    else:
        return False


def get_course_from_db(access_level, user_id):
    all_course = None
    
    if access_level == AccessLevel.private and user_id == None:
        raise Exception('invalid param')

    if user_id != None and access_level == None:
        all_course = [course for course in mongo.db.course.find({
            'create_user_id': user_id
            })]

    elif user_id != None and access_level != None:
        all_course = [course for course in mongo.db.course.find({
            'create_user_id': user_id,
            'access_level': access_level
            })]
    
    else:
        all_course = [course for course in mongo.db.course.find({
            'access_level': 0
            })]
    
    return all_course


def save_new_course(data):
    course = mongo.db.user.find_one({
        'course_name': data['course_name'],
        'user_id': data['user_id']
        })
    if course is None:
        new_course = Course(
            course_name=data['course_name'],
            create_user_id=data['create_user_id'],
            learn_language=data['learn_language'],
            access_level=data['access_level'],
        )
        mongo.db.user.insert_one(new_course.__dict__)
        return True
    else:
        return False


def get_course_detail_from_db(course_id):
    course_info = mongo.db.course.find_one({'course_id': course_id})
    all_vocabulary = [vocabulary for vocabulary in mongo.db.vocabulary.find({
            'course_id': course_id
            })]
    course_detail = CourseDetail(course=course_info, vocabulary=all_vocabulary)
    return course_detail
