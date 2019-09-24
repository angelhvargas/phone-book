from src.PhoneBook import PhoneBook
from src.Contact import ContactEntry
import pytest


@pytest.fixture()
def phone_book():
    return PhoneBook()


@pytest.fixture()
def contact_entry():
    return ContactEntry("Vargas", "Angel", "08388764345", "12 court far, India")


@pytest.mark.usefixtures("phone_book", "contact_entry")
class TestPhoneBook:
    """
    Test units for the PhoneBook class
    """

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
