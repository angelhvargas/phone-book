from src.PhoneBook import PhoneBook
from src.Contact import ContactEntry
from src.DB import DB
import pytest


@pytest.fixture
def database_path():
    """
    path to database file location
    :return: None
    """
    return "test_database.sqlite3"


@pytest.fixture()
def phone_book(database_path):
    """"""
    return PhoneBook(database_path)


@pytest.fixture()
def contact_entry():
    """"""
    return ContactEntry("Vargas", "Angel", "08388764345", "12 court far, India")


@pytest.mark.usefixtures("phone_book", "contact_entry")
class TestPhoneBook(object):
    """
    Test units for the PhoneBook class
    """

    def test_setup_database(self) -> None:
        """
        test table creation
        :return:
        """
        database_connection = DB("test_database.sqlite3").connect()
        database_connection.execute('''
         CREATE TABLE IF NOT EXISTS phone_book (
         id INTEGER PRIMARY KEY,
         surname TEXT NOT NULL,
         firstname TEXT NOT NULL,
         phone_number TEXT NOT NULL,
         address TEXT
     );
         ''')

        database_connection.close()

    def test_create_phone_book_class_instance(self, phone_book) -> None:
        """
        test if a PhoneBook instance can be created
        :return:
        """
        _phone_book = phone_book
        assert isinstance(_phone_book, PhoneBook)

    def test_create_contact_dto_class_instance(self, contact_entry) -> None:
        """
        test if a ContactEntry DTO can be instantiated
        :return:
        """
        _contact_entry = contact_entry
        assert isinstance(_contact_entry, ContactEntry)

    def test_add_entry_to_phone_book(self, phone_book, contact_entry) -> None:
        _result = phone_book.create(contact_entry)
        assert _result == 1

    def test_find_entry_in_phone_book(self, phone_book) -> None:
        """

        :param phone_book:
        :return:
        """
        _result = phone_book.find(1)
        assert _result == (1, 'Vargas', 'Angel', '08388764345', '12 court far, India')

    def test_update_phone_book_entry(self, phone_book) -> None:
        """

        :param phone_book:
        :return:
        """
        _result = phone_book.update(idx=1, firstname="Rufino")
        _result = phone_book.find(1)
        assert _result == (1, 'Vargas', 'Rufino', '08388764345', '12 court far, India')

    def test_delete_entry_in_phone_book(self, phone_book) -> None:
        """

        :param phone_book:
        :return:
        """
        _result = phone_book.delete("1")
        assert _result == 1

    def test_teardown_table(self) -> None:
        """drops table created for tests"""
        database_connection = DB("test_database.sqlite3").connect()
        database_connection.execute('''
         DROP TABLE IF EXISTS phone_book;
         ''')

        database_connection.close()
