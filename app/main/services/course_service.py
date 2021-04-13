from app.main import mongo
from app.main.models.course import Course
from app.main.util.course_util import AccessLevel
from app.main.models.course_detail import CourseDetail
from bson.objectid import ObjectId

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
            'access_level': str(access_level)
            })]
    
    else:
        all_course = [course for course in mongo.db.course.find({
            'access_level': '0'
            })]

    for course in all_course:
        course['_id'] = str(course['_id'])
    return all_course


def save_new_course(data):
    course = mongo.db.course.find_one({
        'course_name': data['course_name'],
        'user_id': data['create_user_id']
        })
    if course is None:
        new_course = Course(
            course_name=data['course_name'],
            create_user_id=data['create_user_id'],
            learn_language=data['learn_language'],
            access_level=data['access_level'],
        )
        mongo.db.course.insert_one(new_course.__dict__)
        return True
    else:
        return False


def get_course_detail_from_db(course_id):
    course_info = mongo.db.course.find_one({'_id': ObjectId(course_id)})
    all_vocabulary = get_vocabulary(course_id)
    course_detail = CourseDetail(course=course_info, vocabulary=all_vocabulary)
    course_detail.course['_id'] = str(course_detail.course['_id'])
    return course_detail


def save_new_vocabulary_to_course(course_id, new_vocabulary):
    course = mongo.db.vocabulary.find_one({'course_id': course_id})
    if(course == None): 
        print('dasdasddddd')
        mongo.db.vocabulary.save({
            'course_id': course_id,
            'vocabulary': new_vocabulary
        })
    else:
        try:
            mongo.db.vocabulary.update({
                'course_id': course_id
            },
            {
                '$push': {
                    'vocabulary': {
                        '$each': new_vocabulary
                    }
                }
            }
            )
        except E:
            print(E)
            return False

    return True

def check_course(course_id):
    course = mongo.db.course.find_one({'_id': ObjectId(course_id)})
    if(course == None): return False
    else: return True

def get_vocabulary(course_id):
    course_vocabulary = mongo.db.vocabulary.find_one({
            'course_id': course_id
            })

    return [vocabulary for vocabulary in course_vocabulary['vocabulary']]
