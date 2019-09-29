import pytest
import flask


@pytest.mark.usefixtures('app', 'client', 'runner')
class TestFactory:
    """TestFactory

    Mocks application core functionality
    """
    def test_request_context(self, app):
        """
        Testing flask application in context mode.
        :param app:
        :return:
        """
        with app.test_request_context('/contact?name=Peter'):
            assert flask.request.path == '/contact'
            assert flask.request.args['name'] == 'Peter'