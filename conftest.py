import pytest
import phonebook


@pytest.fixture()
def app():
    return phonebook.create_app()


@pytest.fixture()
def client(app):
    """
    Prepare an instance of the application
    :return: None
    """
    app.testing = True
    app.secret_key = "testing"
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_client()