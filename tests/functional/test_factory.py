import pytest
import flask


@pytest.mark.usefixtures('app', 'client', 'runner')
class TestFactory:

    def test_request_context(self, app):
        """

        :param app:
        :return:
        """
        with app.test_request_context('/contact?name=Peter'):
            assert flask.request.path == '/contact'
            assert flask.request.args['name'] == 'Peter'

    def test_config(self, client):
        with client as c:
            resp = c.get('/contact/all')
            data = flask.json.loads(resp.data)
            assert data == "hello"