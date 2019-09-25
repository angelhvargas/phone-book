# db.py
import sqlite3
import logging
import os


class DB:

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
        except sqlite3.Error as e:
            self.logger.error(e)

        return self.get_cursor()

    def close(self) -> None:
        """close database connection"""
        self.connection.close()
