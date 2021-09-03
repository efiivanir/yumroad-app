class BaseConfig:
    TESTING = False
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
    SQLALCHEMY_ECHO = True


class DevConfig(BaseConfig):
    DEBUG = True


class TestConfig(BaseConfig):
    TESTING = True


class ProdConfig(BaseConfig):
    pass


configurations = {
    'dev': DevConfig,
    'test': TestConfig,
    'prod': ProdConfig,
}
