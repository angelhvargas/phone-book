from flask import (
    Blueprint, current_app as app, json, abort
)

from phonebook.common.phonebook import PhoneBook

bp = Blueprint('phone_book_api', __name__)


@bp.route('contact/all')
def get_contact_all():
    """"""
    return api_response("hello", 200)


@bp.route('<path:path>', methods=('GET', 'POST', 'PUT', 'DELETE',))
def missing_request(path):
    """"""
    abort(400, {'message': 'Invalid request'})


def api_response(data_, status_):
    response_ = app.response_class(
        response=json.dumps(data_),
        status=status_,
        mimetype='application/json'
    )
    return response_
