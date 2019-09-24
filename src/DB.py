# DB.py
import sqlite3
import logging
import os


class DB:

    DEFAULT_PATH = 'database.sqlite3'
    ERROR_LOG_FILENAME = 'error_sqlite.log'
    con = None

    def __init__(self, database_path=DEFAULT_PATH):
        self.database_path = os.path.join(os.path.dirname(__file__), database_path)
        # simple log configuration
        self.logger = logging.getLogger('sqlite')
        self.logger.setLevel(logging.ERROR)
        fh = logging.FileHandler(self.ERROR_LOG_FILENAME)
        self.logger.addHandler(fh)

    def connect(self) -> sqlite3.connect:
        """
        connect to the database
        :return:
        """
        try:
            self.con = sqlite3.connect(
                self.database_path,
                detect_types=sqlite3.PARSE_DECLTYPES
            )
        except sqlite3.Error as e:
            self.logger.error("DB error: {}" % e)
            return False

        return self.con

    def cursor(self) -> sqlite3:
        """return sqlite3 cursor"""
        return self.con.cursor()

    def close(self) -> None:
        """close database connection"""
        self.con.close()
