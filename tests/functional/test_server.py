import pytest
import flask


@pytest.mark.usefixtures('app', 'client', 'runner')
class TestServer:
    """
    Unit Tests for phone book api blueprint.
    """

    def test_get_all_contacts(self, client: flask.Flask) -> None:
        """
        Test resource GET -> /contacts ¬ returns -> JSON object with all the contacts in the phone book
        :param client:
        :return:
        """
        with client as c:
            resp = c.get('/contacts')
            data = flask.json.loads(resp.data)
            assert data == flask.json.loads(
                '[[4, "Dijkstra", "Edsger", "3581321345589", "19-68 Algo"], [3, "Noam", "Chomsky", "3581321345589", '
                '"19-56 R block"], [2, "Stroustrup", "Bjarne", "3581321345589", "19-79 C block"], [1, "Ritchie", '
                '"Dennis", "1235813213455", "19-41 C block"]]'
            )

    @pytest.mark.parametrize("surname, firstname, phone_number, address, expected",
                             [("Vargas","Angel", "27364523", "somewhere",
                               '{"address": "somewhere","firstname": "Angel","id": 5, '
                               '"phone_number": "27364523", "surname": "Vargas"}')])
    def test_create_new_contact(self, surname, firstname, phone_number, address, expected, client: flask.Flask) -> None:
        """
        Test resource POST:/contacts does create a new entry in the phonebook
        :param surname:
        :param firstname:
        :param phone_number:
        :param address:
        :param expected:
        :param client:
        :return:
        """
        with client as c:
            data = dict(surname=surname, firstname=firstname, phone_number=phone_number, address=address)
            resp = c.post('/contacts', data=data, follow_redirects=True)
            data = flask.json.loads(resp.data)
        assert data == flask.json.loads(expected)

    @pytest.mark.parametrize("_id,expected", [
        ("3", '[3, "Noam", "Chomsky", "3581321345589", "19-56 R block"]'),
        ("2", '[2, "Stroustrup", "Bjarne", "3581321345589", "19-79 C block"]'),
        ("1", '[1, "Ritchie", "Dennis", "1235813213455", "19-41 C block"]')

    ])
    def test_get_contact_by_id(self, _id, expected, client: flask.Flask) -> None:
        """
        Test resource GET -> /contacts/[id] ¬ returns -> JSON object with a matching contact found in the phone book
        :param _id:
        :param expected:
        :param client:
        :return:
        """

        with client as c:
            resp = c.get('/contacts/{}'.format(_id))
            data = flask.json.loads(resp.data)
            assert data == flask.json.loads(
                expected
            )

    @pytest.mark.parametrize("_id,expected", [
        ("5", "0"),
        ("4", '1'),
        ("44", '0')

    ])
    def test_delete_contact_by_id(self, _id, expected, client: flask.Flask) -> None:
        """
        Test resource GET -> /contacts/[id] ¬ returns -> JSON object with a matching contact found in the phone book
        :param _id:
        :param expected:
        :param client:
        :return:
        """

        with client as c:
            resp = c.delete('/contacts/{}'.format(_id))
            data = flask.json.loads(resp.data)
            assert data == flask.json.loads(
                expected
            )

    @pytest.mark.parametrize("attr, search, expected", [('surname','Stroustrup', '[[2, "Stroustrup", "Bjarne", '
                                                                                '"3581321345589", "19-79 C block"]]')])
    def test_search_contact_by_attribute(self, attr, search, expected, client: flask.Flask) -> None:
        """
        Test resource GET ->/contacts?attr=search
        :param attr:
        :param search:
        :param expected:
        :param client:
        :return:
        """
        _data = {attr: search}
        with client as c:
            resp = c.get('/contacts', query_string=_data)
            data = flask.json.loads(resp.data)
            assert data == flask.json.loads(expected)

