import os
from flask import (
    Flask, request, jsonify
)


def create_app(test_config=None):
    app = Flask(__name__, instance_path=os.path.dirname(__file__))
    app.config.from_mapping(
            SECRET_KEY='1234567890987654321',
            DATABASE=os.path.join(app.instance_path, 'database.sqlite3'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # load states allowed for the robots

    from .data import db
    # register db initiator
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
