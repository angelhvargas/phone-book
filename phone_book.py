#!/usr/bin/env python3
"""
Phone Book API client
--------------


Author: Angel Vargas
"""
import argparse

_first_name = None
_surname = None
_phone_number = None
_address = None


def process():
    """"""
    pass


def _main():
    """"""
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
                           nargs='?', const=1, type=int)
    opt_group.add_argument('-c', '--create', help="creates a new entry in the phone book",
                           nargs='?', const=1, type=int)
    opt_group.add_argument('-u', '--update', help="updates an existing entry in the phone book",
                           nargs='?', const=1, type=int)
    opt_group.add_argument('-d', '--delete', help="deletes an entry in the phone book",
                           nargs='?', const=1, type=int)
    opt_group.add_argument('-s', '--search', help="search for an entry in the phonebook",
                           nargs='?', const=1, type=int)

    args = arg_parser.parse_args()


if __name__ == '__main__':
    """Start Phone Book client app
    
    This client app will consume the phone book API.
    
    """
    _main()
