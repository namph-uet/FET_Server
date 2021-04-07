import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'


class ProductionConfig(Config):
    DEBUG = False
    MONGO_URI = 'mongodb://localhost:27017/fet_db_product'


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    MONGO_URI = 'mongodb://localhost:27017/fet_db_staging'


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    MONGO_URI = 'mongodb://localhost:27017/fet_db_dev'


class TestingConfig(Config):
    TESTING = True
    DEBUG = False
    MONGO_URI = 'mongodb://localhost:27017/fet_db_test'

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig,
    staging=StagingConfig
)

key = Config.SECRET_KEY