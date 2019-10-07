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


def create_contact():
    """todo"""
    pass


def read_contact():
    """todo"""
    pass


def update_contact():
    """todo"""
    pass


def delete_contact():
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


def process():
    """todo"""
    pass


def beauty_output():
    """todo"""


def _main() -> None:
    """

    :return:
    """
    arg_parser = argparse.ArgumentParser(prog='python3 -m phone_book.py',
                                         description=__doc__)
    # data attributes
    arg_parser.add_argument('--surname', type=str, help="surname attribute -s [surname] --s [surname]")
    arg_parser.add_argument('--firstname', type=str)
    arg_parser.add_argument('--phone-number', type=str)
    arg_parser.add_argument('--address', type=str)
    arg_parser.add_argument('--data', type=str)
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

    print(args)

    if args.list:
        list_contacts()
    elif args.create:
        pass


if __name__ == '__main__':
    """Start Phone Book client app
    
    This client app will consume the phone book API.
    
    """
    _main()
