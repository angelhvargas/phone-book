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


def list_contacts() -> None:
    """ List Contacts

    consume resource GET /contacts

    :return: None
    """
    try:
        response = requests.get(SERVER_BASE + '/contacts')
        if response.status_code == 200:
            resp_data = response.json()
            for v in resp_data:
                print('id:           ' + str(v[0]))
                print('surname:      ' + v[1])
                print('first name:   ' + v[2])
                print('phone number: ' + v[3])
                print('address:      ' + v[4])
                print('--------------^')
        else:
            print('Error: ' + str(response.status_code) + ": " + response.text)
    except requests.HTTPError as e:
        argparse.ArgumentError(e)


def create_contact(**kwargs) -> None:
    """ Creates a new contact

    call to resource POST /contacts

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
            print('Error: ' + str(response.status_code) + ": " + response.text)

    except requests.HTTPError as e:
        argparse.ArgumentError(e)


def get_contact(_id: str) -> None:
    """
    Fetch a given contact if this exists, using GET /contacts/[id]
    :param _id: contact_id
    :return: None
    """
    try:
        response = requests.get(SERVER_BASE + '/contacts/{}'.format(_id))
        if response.status_code == 200:
            v = response.json()
            print('**************')
            print('id:           ' + str(v[0]))
            print('surname:      ' + v[1])
            print('first name:   ' + v[2])
            print('phone number: ' + v[3])
            print('address:      ' + v[4])
            print('-------------^')
        else:
            print('Error: ' + str(response.status_code) + ": " + response.text)
    except requests.HTTPError as e:
        print('An error happened: ' + e.strerror)


def update_contact(_id: str, data: dict) -> None:
    """
    Update a contact using PUT /contacts/[id]

    :param _id: contact_id
    :param data: any valid key:value attribute
    :return: None
    """
    try:
        response = requests.put(SERVER_BASE + '/contacts/{}'.format(_id), params=data)
        if response.status_code == 200:
            print('The contact id: {} has been update'.format(_id))
    except requests.HTTPError as e:
        print('An error happened: ' + e.strerror)


def delete_contact(contact_id: str) -> None:
    """
    Delete a contact using DELETE /contacts/[id]
    :param contact_id: contact_ids
    :return:
    """
    try:
        response = requests.delete(SERVER_BASE + '/contacts/' + contact_id)
        if response.status_code == 200:
            print('contact have been deleted!')
        else:
            print('Error: ' + response.status_code + ' ' + response.json())

    except requests.HTTPError as e:
        argparse.ArgumentError(e)


def search_contact(_id: str, _data: dict):
    """todo"""
    try:
        response = requests.get(SERVER_BASE + '/contacts', params=_data)
        if response.status_code == 200:
            resp_data = response.json()
            for v in resp_data:
                print('id:           ' + str(v[0]))
                print('surname:      ' + v[1])
                print('first name:   ' + v[2])
                print('phone number: ' + v[3])
                print('address:      ' + v[4])
                print('--------------^')
    except requests.HTTPError as e:
        print('An error happened: ' + e.strerror)


def _main() -> None:
    """
    main function handle the script routing depending on the user input, depending on the user input, the function will
    call more functions to execute the desired command given by the user or script interacting with.
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
    opt_group.add_argument('-g', '--get', help="get an entry by id from the phone book",
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
        if not args.id:
            arg_parser.error('A contact id is required --id [id]')
        if not args.surname and not args.first_name and not args.phone_number and not args.address:
            arg_parser.error('at least one attribute is required: [--surname] '
                             'or [--first-name] or [--phone-number] or [--address]')

        _data = {}
        _id = args.id

        if args.surname != '':
            _data['surname'] = args.surname
        if args.first_name != '':
            _data['firstname'] = args.first_name
        if args.phone_number != '':
            _data['phone_number'] = args.phone_number
        if args.address == '':
            _data['address'] = args.address
        update_contact(_id, _data)

    elif args.delete:
        # delete contact
        if not args.id:
            arg_parser.error('A contact id is required --id [id]')
        else:
            _id = args.id
            delete_contact(_id)
    elif args.get:
        # get contact by id
        if not args.id:
            arg_parser.error('A contact id is required --id [id]')
        get_contact(args.id)

    elif args.search:
        # search contact
        if not args.surname and not args.first_name and not args.phone_number and not args.address:
            arg_parser.error('at least one attribute is required: [--surname] '
                             'or [--first-name] or [--phone-number] or [--address]')

        _data = {}
        _id = args.id

        if args.surname != '':
            _data['surname'] = args.surname
        if args.first_name != '':
            _data['firstname'] = args.first_name
        if args.phone_number != '':
            _data['phone_number'] = args.phone_number
        if args.address == '':
            _data['address'] = args.address

        search_contact(_id, _data)

if __name__ == '__main__':
    """Start Phone Book client app
    
    This client app will consume the phone book API.
    
    """
    _main()
