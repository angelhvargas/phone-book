import pytest
import flask
import json


@pytest.mark.usefixtures('app', 'client', 'runner')
class TestServer:
    """
    Unit Tests for phone book api blueprint.
    """
    def test_fetch_all_contacts(self, client: flask.Flask) -> None:
        """
        Test resource GET -> /contact/all ¬ returns -> JSON object with all the contacts in the phone book
        :param client:
        :return:
        """
        with client as c:
            resp = c.get('/contact/all')
            data = flask.json.loads(resp.data)
            assert data == flask.json.loads(
                '[[4, "Dijkstra", "Edsger", "3581321345589", "19-68 Algo"], [3, "Noam", "Chomsky", "3581321345589", '
                '"19-56 R block"], [2, "Stroustrup", "Bjarne", "3581321345589", "19-79 C block"], [1, "Ritchie", '
                '"Dennis", "1235813213455", "19-41 C block"]]'
            )
