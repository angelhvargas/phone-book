import pytest

from phonebook.data.db import DB


@pytest.fixture
def database_path():
    """
    path to database file location
    :return: None
    """
    return "test_database.sqlite3"


@pytest.fixture
def database_connection():
    """
    database connection
    :return: None
    """
    return DB("test_database.sqlite3").connect()


@pytest.mark.usefixtures("database_path", "database_connection")
class TestDatabase:
    """
    Unit testing for the database connectivity
    """
    database_connection = DB("test_database.sqlite3").connect()

    @classmethod
    def setup_class(cls):
        cls.database_connection.execute('''
        CREATE TABLE IF NOT EXISTS phone_book (
        id INTEGER PRIMARY KEY,
        surname TEXT NOT NULL,
        firstname TEXT NOT NULL,
        phone_number TEXT NOT NULL,
        address TEXT
    );
        ''')

    @classmethod
    def teardown_class(cls):
        cls.database_connection.execute('''
        DROP TABLE IF EXISTS phone_book;
        ''')

        cls.database_connection.close()

    @pytest.mark.parametrize("surname, firstname, phone_number, address", [

        ("Angel", "Vargas", "0831819734", "87 alexander court"),
        ("Michael", "Kenan", "0834484184", "6th Abbey road"),
        ("Alan", "Turing", "0831834242", "44 St. Vincent's")

    ])
    def test_create_entry_in_table(self, surname, firstname, phone_number, address) -> None:
        """
        test jnsert into phone_book database
        :param surname:
        :param firstname:
        :param phone_number:
        :param address:
        :return:
        """
        query = ('''INSERT INTO phone_book
        (surname, firstname, phone_number, address)
        VALUES (?, ?, ?, ?)''')

        values = (surname, firstname, phone_number, address)

        result = self.database_connection.execute(query, values)
        assert result.arraysize == 1

    @pytest.mark.parametrize("surname, firstname", [
        ("Michael", "Kenan")
    ])
    def test_select_an_entry_in_table_phone_book(self, surname, firstname):
        """
        test select a record from the test data.
        :param surname:
        :param firstname:
        :return:
        """

        query = (''' SELECT * FROM phone_book WHERE surname LIKE ? and firstname LIKE ?
        ''')
        values = (surname, firstname)
        stmt = self.database_connection.execute(query, values)
        results = stmt.fetchall()

        assert results == [(2, 'Michael', 'Kenan', '0834484184', '6th Abbey road')]

    @pytest.mark.parametrize("_id ,surname, firstname, address, old_phone_number, new_phone_number", [
        (2, "Michael", "Kenan", "6th Abbey road", "0834484184", "0837654321")
    ])
    def test_update_entry_in_table_phone_book(self, _id, surname, firstname, address, old_phone_number,
                                              new_phone_number):
        """
        test update entry in phone_book table
        :param _id:
        :param surname:
        :param firstname:
        :param address:
        :param old_phone_number:
        :param new_phone_number:
        :return:
        """

        query = ('''UPDATE phone_book 
        SET surname=?, firstname=?, phone_number=?, address=? WHERE id=?;
        ''')
        values = (surname, firstname, new_phone_number, address, str(_id))
        self.database_connection.execute(query, values)

        query = (''' SELECT * FROM phone_book WHERE id=?;
        ''')
        values = (str(_id))
        stmt = self.database_connection.execute(query, values)

        results = stmt.fetchall()

        assert results == [(2, 'Michael', 'Kenan', '0837654321', '6th Abbey road')]

    @pytest.mark.parametrize("_id ,surname, firstname", [
        (2, "Michael", "Kenan")
    ])
    def test_delete_entry_in_table_phone_book(self, _id, surname, firstname):
        """
        test delete entry from phone_book table
        :param _id:
        :param surname:
        :param firstname:
        :return:
        """

        query = ('''DELETE FROM phone_book 
         WHERE id=?;
        ''')
        values = (str(_id))
        self.database_connection.execute(query, values)

        query = (''' SELECT * FROM phone_book WHERE id=?;
        ''')
        values = (str(_id))
        stmt = self.database_connection.execute(query, values)

        results = stmt.fetchall()

        assert results == []
