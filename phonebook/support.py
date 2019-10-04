from .common.contactentry import ContactEntry
from flask import (abort)


def valid_contact(surname: str, firstname: str, phone_number: str, address=None) -> ContactEntry:
    """
    Validates a contact and returns a ContactEntry DTO.
    :param surname:
    :param firstname:
    :param phone_number:
    :param address:
    :return:
    """
    try:
        contact_entry = ContactEntry(surname, firstname, phone_number, address)
    except Exception as e:
        return abort(400, "invalid ContactEntry object: {}".format(e))
    return contact_entry
