from phonebook.common.phonebook import PhoneBook
from phonebook.common.contactentry import ContactEntry
from phonebook.data.db import DB
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
    Test unit for the common class
    """

    def test_setup_database(self) -> None:
        """
        test phone_book table creation
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
        :param contact_entry: fixture
        :return:
        """
        _contact_entry = contact_entry
        assert isinstance(_contact_entry, ContactEntry)

    def test_add_single_entry_to_phone_book(self, phone_book, contact_entry) -> None:
        """

        :param phone_book:
        :param contact_entry: fixture
        :return:
        """
        _result = phone_book.create(contact_entry)
        assert _result == 1

    @pytest.mark.parametrize("surname, firstname, phone_number, address, expected", [

        ("Murray", "Aodhan", "0831241244", "69 road nowhere", 2),
        ("Kenan", "Michael", "0814423424", "6th Abbey road", 3),
        ("Turing", "Alan", "0831834242", "44 St. Vincent's", 4)

    ])
    def test_add_many_entries_to_phone_book(self, surname, firstname, phone_number, address, expected, phone_book) -> None:
        contact_entry = ContactEntry(surname, firstname, phone_number, address)
        _result = phone_book.create(contact_entry)
        assert _result == expected

    def test_find_entry_in_phone_book(self, phone_book) -> None:
        """

        :param phone_book:
        :return:
        """
        _result = phone_book.find(1)
        assert _result == (1, 'Vargas', 'Angel', '08388764345', '12 court far, India')

    def test_update_phone_book_entry(self, phone_book) -> None:
        """

        :param phone_book: fixture
        :return:
        """
        # test single field update
        _result = phone_book.update(idx=1, firstname="Humberto")
        assert _result == 1

    @pytest.mark.parametrize("surname, firstname, phone_number, address, expected", [

        ("Murray", "Aodhan", "0831241244", "69 road nowhere", ("Murray", "Aodhan", "0831241244", "69 road nowhere")),
        ("Kenan", "Michael", "0814423424", "6th Abbey road",  ("Kenan", "Michael", "0814423424", "6th Abbey road")),
        ("Turing", "Alan", "0831834242", "44 St. Vincent's", ("Turing", "Alan", "0831834242", "44 St. Vincent\'s"))

    ])
    def test_search_phone_book_entry(self, surname, firstname, phone_number, address, expected, phone_book) -> None:
        """
        test asserts correct search results using different search keys (columns)
        :param surname:
        :param firstname:
        :param phone_number:
        :param address:
        :param expected:
        :param phone_book: fixture
        :return:
        """
        # test search by surname
        _result_surname = phone_book.search(surname=surname)
        assert _result_surname[0][1] == expected[0]
        # test search by firstname
        _result = phone_book.search(firstname=firstname)
        assert _result_surname[0][2] == expected[1]
        # test search by phone_number
        _result = phone_book.search(phone_number=phone_number)
        assert _result_surname[0][3] == expected[2]
        # test search by address
        _result = phone_book.search(address=address)
        assert _result_surname[0][4] == expected[3]
        # test search by name


    def test_delete_entry_in_phone_book(self, phone_book) -> None:
        """

        :param phone_book:
        :return:
        """
        # test successful deletion
        _result = phone_book.delete("1")
        assert _result == 1
        # test failed deletion
        _result = phone_book.delete("1")
        assert _result == 0

    def test_teardown_table(self) -> None:
        """drops table created for tests"""
        database_connection = DB("test_database.sqlite3").connect()
        database_connection.execute('''
         DROP TABLE IF EXISTS phone_book;
         ''')

        database_connection.close()
