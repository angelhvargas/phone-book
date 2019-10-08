#!/usr/bin/env python3
"""
Phone Book API client
--------------


Author: Angel Vargas
"""
import argparse
import requests

_first_name = None
_surname = None
_phone_number = None
_address = None
PORT = '5000'
SERVER_URI = 'http://127.0.0.1'
SERVER_BASE = SERVER_URI + ':' + PORT


def search_contact():
    """todo"""
    pass


def list_contacts() -> None:
    """ List Contacts

    consume resource GET /contacts

    :return: None
    """
    try:
        response = requests.get(SERVER_BASE + '/contacts').json()
        print(response)
    except requests.HTTPError as e:
        argparse.ArgumentError(e)


def create_contact(**kwargs) -> None:
    """ Creates a new contact

    call to resource POST contacts/

    :return: None
    """
    data = {
        "surname":      kwargs.get('surname'),
        "firstname":    kwargs.get('firstname'),
        "phone_number": kwargs.get('phone_number'),
        "address":      kwargs.get('address')
    }

    try:
        response = requests.post(SERVER_BASE + '/contacts', data)
        if response.status_code == 200:
            print('contact have been saved!')
        else:
            print('Error: ' + response.status_code + ' ' + response.json())

    except requests.HTTPError as e:
        argparse.ArgumentError(e)


def get_contact():
    """Read/Get a contact based on their id"""
    pass


def update_contact():
    """todo"""
    pass


def delete_contact(contact_id: str) -> None:
    """"""
    try:
        response = requests.delete(SERVER_BASE + '/contacts/' + contact_id)
        if response.status_code == 200:
            print('contact have been deleted!')
        else:
            print('Error: ' + response.status_code + ' ' + response.json())

    except requests.HTTPError as e:
        argparse.ArgumentError(e)


def _main() -> None:
    """

    :return:
    """
    arg_parser = argparse.ArgumentParser(prog='python3 -m phone_book.py',
                                         description=__doc__)
    # data attributes
    arg_parser.add_argument('--surname',
                            nargs='?', const='', type=str, help="surname attribute --surname [surname]")
    arg_parser.add_argument('--first-name', dest="first_name",
                            nargs='?', const='', type=str, help="first name attribute  --first-name [first-name]")
    arg_parser.add_argument('--phone-number', dest="phone_number",
                            nargs='?', const='',  type=str, help="phone number attribute --phone-number [phone-number]")
    arg_parser.add_argument('--address',
                            nargs='?', const=False, type=str)
    arg_parser.add_argument('--id',
                            nargs='?', const='', type=str, help="contact id, required for operations "
                                                                "such find and delete")
    # operations
    opt_group = arg_parser.add_mutually_exclusive_group()
    opt_group.add_argument('-l', '--list', help="lists entries in the phone book",
                           nargs='?', const=True, type=bool)
    opt_group.add_argument('-c', '--create', help="creates a new entry in the phone book",
                           nargs='?', const=True, type=bool)
    opt_group.add_argument('-u', '--update', help="updates an existing entry in the phone book",
                           nargs='?', const=True, type=bool)
    opt_group.add_argument('-d', '--delete', help="deletes an entry in the phone book",
                           nargs='?', const=True, type=bool)
    opt_group.add_argument('-s', '--search', help="search for an entry in the phonebook",
                           nargs='?', const=True, type=bool)
    opt_group.add_argument('-p', '--prettify', help="", nargs='?', const=True, type=bool)
    args = arg_parser.parse_args()

    if args.list:
        # list contacts
        list_contacts()

    elif args.create:
        # create a new contact
        if args.surname == '':
            arg_parser.error('surname is required')
        if not args.first_name:
            arg_parser.error('first name is required')
        if not args.phone_number:
            arg_parser.error('phone number is required')

        create_contact(surname=args.surname, firstname=args.first_name,
                       phone_number=args.phone_number, address=args.address)

    elif args.update:
        # update contact
        if not args.surname and not args.first_name and not args.phone_number and not args.address:
            arg_parser.error('at least one attribute is required: [--surname] '
                             'or [--first-name] or [--phone-number] or [--address]')
        pass

    elif args.delete:
        # delete contact
        if not args.id:
            arg_parser.error('A contact id is required')
        else:
            _id = args.id
            delete_contact(_id)
    elif args.search:
        # search contact
        pass

    print('this worked')


if __name__ == '__main__':
    """Start Phone Book client app
    
    This client app will consume the phone book API.
    
    """
    _main()
