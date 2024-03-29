import pytest

from phonebook import create_app


from phonebook.config import get_env_variable
from phonebook.config import TestingConfig


@pytest.yield_fixture
def app():
    def _app(config_class):
        app = create_app(config_class)
        app.test_request_context().push()

        if config_class is TestingConfig:

            # always starting with an empty DB
            db.drop_all()
            from project.models.model1 import Model1

            db.create_all()

        return app

    yield _app
    db.session.remove()
    if str(db.engine.url) == TestingConfig.SQLALCHEMY_DATABASE_URI:
        db.drop_all()