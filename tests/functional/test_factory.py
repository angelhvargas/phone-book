import pytest
import flask
import phonebook


@pytest.mark.usefixtures('app', 'client', 'runner')
class TestFactory:
    """TestFactory

    Mocks application core functionality
    """

    def test_create_api_app(self):
        """"""
        app = phonebook.create_app()
        assert isinstance(app, flask.Flask)

        app = phonebook.create_app(None)
        assert isinstance(app, flask.Flask)

    def test_request_context(self, app):
        """
        does test the flask application in context mode.
        :param app:
        :return:
        """
        with app.test_request_context('/contact?name=Peter'):
            assert flask.request.path == '/contact'
            assert flask.request.args['name'] == 'Peter'