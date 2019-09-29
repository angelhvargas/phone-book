from flask import (
    Blueprint, current_app as app, Flask, abort, g
)
import json
from phonebook.common.phonebook import PhoneBook
from phonebook.db import get_db

bp = Blueprint('phone_book_api', __name__)


@bp.route('/', methods=('GET',))
def home():
    _data = {"message": "phone book rest api, for api instructions navigate to: "}
    return api_response(_data, 200)


@bp.route('contact/all', methods=('GET',))
def get_contact_all() -> Flask.make_response:
    """
    Return all the contacts in the
    method: GET
    resource: /contact/all
    :return: JSON object |
    {id: _id, surname: _surname, firstname: _firstname, phone_number: _phone_number, address: _address}
    """
    db = get_db()
    pb = PhoneBook(db)
    try:
        _data = pb.all()

        data = list()

        for row in _data:
            data.append(list(row))

    except db.Error as e:
        return api_response({'error': e}, 500)

    return api_response(data, 200)


@bp.route('contact', methods=("GET",))
@bp.route('contact/<string:contact_id>', methods=("GET",))
def get_contact(contact_id=-1) -> Flask.make_response:
    """
    :param contact_id: valid integer id to match for search
    :return:
    """
    if contact_id == -1:
        get_contact_all()

    db = get_db()
    pb = PhoneBook(db)
    try:
        _data = pb.find(contact_id)
    except db.Error as e:
        return api_response({'error': e}, 500)

    return api_response(list(_data), 200)


@bp.route('contact/search/<string:contact_id>', methods=("GET",))
@bp.route('contact/<string:contact_id>/<string:attribute>', methods=("GET",))
def search_contact(search: str, attribute=None) -> Flask.make_response:
    """

    returns contact matching exactly a given value in a given attribute,
    by default this resource will use the contact
    id, this means is different than the search resource.

    :param search:
    :param attribute:
    :return:
    """


@bp.route('<path:path>', methods=('GET', 'POST', 'PUT', 'DELETE',))
def missing_request(path):
    """
    Handles any missing request which is not part of the API.
    :param path:
    :return:
    """
    abort(400, {'message': 'Invalid request'})


def api_response(data_, status_):
    """
    Prepares the API response.
    :param data_:
    :param status_:
    :return:
    """
    response_ = app.response_class(
        response=json.dumps(data_),
        status=status_,
        mimetype='application/json'
    )
    return response_
