import sqlite3
import click
from flask import current_app, g, Flask
from flask.cli import with_appcontext


def get_db() -> sqlite3.Connection:
    """
    fetch db instance form the current application
    :return: sqlite3.Connection
    """
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None) -> None:
    """
    close the db connection and kill the db instance from main application
    :param e:
    :return: None
    """
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db() -> None:
    """
    load schema.sql and read it's to execute the commands in the active database.
    :return: None
    """
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """init_db command
    - should be run from the console, #$ flash init-db
    This command clear the existing data and create new tables and populates with test data"""
    init_db()
    click.echo('Initialized the database.')


def init_app(app: Flask):
    """
    tells Flask to call that function when cleaning up after returning the response.
    also adds a new command that can be called with the flask command.
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
