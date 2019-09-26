import os

basedir = os.path.abspath(os.path.dirname(__file__))


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
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    """
    Base configuration for testing environment
    """
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test_database.sqlite3')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """
    Base configuration for production environment
    """
    DEBUG = False


config_by_name = dict(
    devevopment=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig
)

key = Config.SECRET_KEY