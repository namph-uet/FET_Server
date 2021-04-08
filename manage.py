import os
import unittest

from flask_script import Manager
from app.main import create_app
from app.main.controllers.user_controller import user_controller
from app.main.controllers.course_controller import course_controller

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(user_controller)
app.register_blueprint(course_controller)
app.app_context().push()

manager  = Manager(app)

@manager.command
def run():
    app.run()

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()