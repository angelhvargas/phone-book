from phonebook.config import *
from phonebook import (
    common
)
from flask import (
    Flask, request, jsonify
)

import os


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__, instance_path=os.path.dirname(__file__))

    if config_class is None:
        app.config.from_mapping(
            SECRET_KEY='1234567890987654321',
            DATABASE=os.path.join(app.instance_path, 'database.sqlite3'),
        )
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_object(config_class)

    # ensure the app instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError as e:
        pass

    # register db initiator
    from . import db
    db.init_app(app)

    from . import phone_book_api

    # register server control blueprint
    app.register_blueprint(phone_book_api.bp, url_prefix='/')

    # handle missing
    @app.errorhandler(404)
    @app.errorhandler(405)
    def _handle_api_error(ex):
        if request.path.startswith('/'):
            return ex
        else:
            return ex

    @app.errorhandler(400)
    def _handle_missing(error):
        data = jsonify({'message': error.description['message']})
        response = app.response_class(
            response=data,
            status=400,
            mimetype='application/json'
        )
        return response

    return app
