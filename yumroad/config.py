import os


class BaseConfig:
    TESTING = False
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
    SQLALCHEMY_ECHO = True
    WTF_CSRF_ENABLED = True

    SECRET_KEY = os.getenv('YUMROAD_SECRET_KEY', '00000abcdef')


class DevConfig(BaseConfig):
    DEBUG = True


class TestConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False


class ProdConfig(BaseConfig):
    pass


configurations = {
    'dev': DevConfig,
    'test': TestConfig,
    'prod': ProdConfig,
}
