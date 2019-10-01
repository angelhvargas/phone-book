import os

basedir = os.path.abspath(os.path.dirname(__file__))


def get_env_variable(name):
    try:
        return os.environ.get(name)
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)


class Config:
    """
    Config wrapper class, acts as a configuration repository to
    provide
    """
    SECRET_KEY = os.getenv('SECRET_KEY', '328975423098563209756')
    DEBUG = True


class DevelopmentConfig(Config):
    """
    Base configuration for development environment
    """
    DEBUG = True
    TEST_SQL_PATH = os.path.join(os.path.abspath(basedir), 'tests', '')
    DATABASE = os.path.join(os.path.abspath(basedir), 'dev_database.sqlite3')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    """
    Base configuration for testing environment
    """
    DEBUG = True
    TESTING = True
    DATABASE = os.path.join(os.path.abspath(basedir), 'test_database.sqlite3')
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(Config):
    """
    Base configuration for production environment
    """
    DEBUG = False
    DATABASE = os.path.join(os.path.abspath(basedir), 'prod.sqlite3')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE


config_by_name = dict(
    devevopment=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig
)

key = Config.SECRET_KEY