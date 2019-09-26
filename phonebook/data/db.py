# db.py
import logging
import os

import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db() -> sqlite3.Connection:
    """
    fetch db instance form the current application
    :return: sqlite3.Connection
    """
    if 'db' not in g:
        g.db = DB('prod.sqlite3').connect()
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


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


class DB:
    """
    DB have the responsability to provide an interface within the sqlite3 library acting as wrapper for added extra
    functionality.
    """
    DEFAULT_PATH = 'database.sqlite3'
    ERROR_LOG_FILENAME = 'error_sqlite.log'
    connection = None
    cursor = None

    def __init__(self, database_path=DEFAULT_PATH):
        self.database_path = os.path.join(os.path.dirname(__file__), database_path)
        # simple log configuration
        self.logger = logging.getLogger('sqlite')
        self.logger.setLevel(logging.ERROR)
        fh = logging.FileHandler(self.ERROR_LOG_FILENAME)
        self.logger.addHandler(fh)

    def connect(self):
        """
        connect to the database
        :return:
        """
        try:
            self.connection = sqlite3.connect(
                self.database_path,
                detect_types=sqlite3.PARSE_DECLTYPES
            )
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            self.logger.error("DB error: {}" % e)
            raise sqlite3.Error(e)

        return self.connection

    def get_cursor(self) -> sqlite3.Cursor:
        """return sqlite3 cursor"""
        return self.cursor

    def execute(self, query, params=None) -> sqlite3.Cursor:
        """
        Execute a given query, if fails will log the error to the log file
        :param query:
        :param params:
        :return:
        """
        try:
            self.get_cursor().execute(query, params)
        except Exception as e:
            self.logger.error("DB error: {}" % e)

        return self.get_cursor()

    def close(self) -> None:
        """close database connection"""
        self.connection.close()
