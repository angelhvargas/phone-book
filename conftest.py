# conftest.py
"""
this file defines the test fixtures to get prepare Flask framework for testing.
"""
import pytest
import os
from flask import (
    Flask
)
import phonebook


@pytest.fixture()
def app():
    """prepare application and pass configuration for testing environment"""
    app = Flask(__name__, instance_path=os.path.dirname(__file__))
    # load the test config if passed in
    app.config.from_object(phonebook.config.TestingConfig)

    # ensure the app instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError as e:
        pass

    # register db initiator
    with app.app_context():
        from phonebook import db
        db.init_app(app)
        app.db = db.get_db()

    import phonebook.phone_book_api as phone_book_api

    # register server control blueprint
    app.register_blueprint(phone_book_api.bp, url_prefix='/')

    return app


@pytest.fixture()
def client(app):
    """
    Prepare a client instance of the application, for resource testing
    :return: None
    """
    app.testing = True
    app.secret_key = "testing"
    return app.test_client()


@pytest.fixture()
def runner(app):
    """Test runner"""
    return app.test_client()
