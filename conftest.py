import pytest
import phonebook
from phonebook.config import TestingConfig


@pytest.fixture()
def app():
    """prepare application and pass configuration for testing environment"""
    return phonebook.create_app(TestingConfig)


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
