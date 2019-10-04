from flask import (
    Blueprint, current_app as app, Flask, abort, request
)
import json
from phonebook.common.phonebook import PhoneBook
from phonebook.common.contactentry import ContactEntry
from phonebook.db import get_db

bp = Blueprint('phone_book_api', __name__)


@bp.route('/', methods=('GET',))
def home():
    _data = dict(message="phone book rest api, for api instructions navigate to: ")
    return api_response(_data, 200)


@bp.route('contacts', methods=('GET', 'POST'))
def contacts_resource() -> Flask.make_response:
    """
    >> resource GET '/contacts' return a list of all contacts
    >> resource GET '/contacts?attribute=search' return the contacts matching the given search
    >> resource POST '/contacts?surname=<surname>&firstname=<firstname>&phone_number=32234234&address=fadsf' creates a
    new entry in the phonebook.
    This resource requires the following parameters to create a new entry:
        surname: str
        firstname: str
        phone_number: str
        address: str (Optional)
    :return: response 200: if resource does created a new entry in the phone book
    """

    if request.method == 'GET':
        db = get_db()
        pb = PhoneBook(db)
        qs = request.args
        try:
            if qs:
                rows = pb.search(**qs)
            else:
                rows = pb.all()
            data = list()

            for row in rows:
                data.append(list(row))

        except db.Error as e:
            return api_response({'error': e}, 500)

        return api_response(data, 200)

    elif request.method == 'POST':
        db = get_db()
        pb = PhoneBook(db)
        try:
            contact_entry = valid_contact(surname=request.form['surname'], firstname=request.form['firstname'],
                                          phone_number=request.form['phone_number'], address=request.form['address'])
            if isinstance(contact_entry, ContactEntry):
                contact_entry_id = pb.create(contact_entry)
                data = {
                    "id": contact_entry_id,
                    "surname": contact_entry.surname,
                    "firstname": contact_entry.firstname,
                    "phone_number": contact_entry.phone_number,
                    "address": contact_entry.address
                }

                return api_response(data, 200)

        except RuntimeError as e:
            return api_response({"error": e}, 400)
    else:
        return abort(400, {'message': 'Invalid request'})


@bp.route('contacts/<string:contact_id>', methods=("GET", "DELETE"))
def contact(contact_id=-1) -> Flask.make_response:
    """
    >> resource GET 'contacts/<contact_id>' Returns a contact if the parameter id is included
    and is valid or is found in the database.
    >> resource DELETE 'contacts/<contact_id>' Deletes the given contact if the id exists in the phone book
    :param contact_id: valid integer id to match for search
    :return:
    """
    if request.method == "GET":
        db = get_db()
        pb = PhoneBook(db)
        try:
            _data = pb.find(contact_id)
        except db.Error as e:
            return api_response({'error': e}, 500)

        return api_response(list(_data), 200)

    elif request.method == "PUT":
        pass
    elif request.method == "DELETE":
        #
        db = get_db()
        pb = PhoneBook(db)
        try:
            _data = pb.delete(contact_id)
        except db.Error as e:
            return api_response({'error': e}, 500)

        return api_response(_data, 200)


@bp.route('<path:path>', methods=('GET', 'POST', 'PUT', 'DELETE',))
def missing_request(path):
    """
    Handles any missing request which is not part of the API.
    :param path:
    :return:
    """
    return abort(400, {'message': 'Invalid request'})


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


def valid_contact(surname: str, firstname: str, phone_number: str, address=None) -> ContactEntry:
    """

    :param surname:
    :param firstname:
    :param phone_number:
    :param address:
    :return:
    """
    try:
        contact_entry = ContactEntry(surname, firstname, phone_number, address)
    except Exception as e:
        return abort(400, "invalid ContactEntry object: {}".format(e))
    return contact_entry
