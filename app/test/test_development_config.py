import os
import unittest

from flask import current_app
from flask_testing import TestCase

from manage import app
from app.main.config import basedir

class TestDevelopmentConfig(TestCase): 
    def create_app(self):
        app.config.from_object('app.main.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertFalse(current_app is None)
        self.assertFalse(app.config['SECRET_KEY'] == 'test')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertTrue(
            app.config['MONGO_URI'] == 'mongodb://localhost:27017/fet_db_dev'
        )

class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertFalse(app.config['SECRET_KEY'] == 'my_precious')
        self.assertTrue(app.config['DEBUG'] == False)
        self.assertTrue(
            app.config['MONGO_URI'] == 'mongodb://localhost:27017/fet_db_test'
        )


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config['DEBUG'] == False)
        self.assertTrue(
            app.config['MONGO_URI'] == 'mongodb://localhost:27017/fet_db_product'
        )

class TestStagingConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.StagingConfig')
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config['DEBUG'] == True)
        self.assertTrue(
            app.config['MONGO_URI'] == 'mongodb://localhost:27017/fet_db_staging'
        )

if __name__ == '__main__':
    unittest.main()