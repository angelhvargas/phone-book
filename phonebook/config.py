import os
from pathlib import Path

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
    DATABASE = os.path.join(os.path.abspath(basedir), 'database.sqlite3')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    """
    Base configuration for testing environment
    """
    DEBUG = True
    TESTING = True
    DATABASE = os.path.join(os.path.abspath(basedir), 'database.sqlite3')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """
    Base configuration for production environment
    """
    DEBUG = False
    DATABASE = os.path.join(os.path.abspath(basedir), 'database.sqlite3')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE


config_by_name = dict(
    devevopment=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig
)

key = Config.SECRET_KEY