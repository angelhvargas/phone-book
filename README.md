phone-book
--------------

_Description:_ 

This is a simple phone book rest api and a linux console client which support the following actions:

- List all entries in the phone book.
- Create a new entry to the phone book.
- Remove an existing entry in the phone book.
- Update an existing entry in the phone book.
- Search for entries in the phone book by surname.

Contacts can store the following information:
- Surname
- Firstname
- Phone number
- Address (optional)


Requirements:
-------------
1. Python 3.6.x

Install:
--------

1. clone repository `git clone https://github.com/angelhvargas/phone-book` 
2. navigate to the directory
3. within the project directory, create a virtual python environment and activate it

    run `python3 -m venv venv`
    
    To activate the virtual environment on Windows: 
    
    run `\env\Scripts\activate.bat`
    
    To activate the virtual environment on Linux:
    
    run `source ./python_env/bin/activate`
    
4. Install dependencies
 
    `pip install -r requirements.txt`


Launch Application
------------------
###### 1.1 set environment Windows base system:

`set FLASK_APP=phonebook`

`set FLASK_ENV=development`

###### 1.2 set environment Windows base system:

`export FLASK_APP=phonebook`

`export FLASK_ENV=development`

###### 2. run database migration command

`flan init-db`

###### 3. run server

from the base directory execute:

`flask run`


###### 4. test with the consumer client

phone_book.py

Client usage
------------

The client needs the server running to get it connected to the Phone Book service.

Run from your console:
 
`phonebook.py --help`

#### some usage examples:

```

usage: python3 -m phone_book.py [-h] [--surname [SURNAME]]
                                [--first-name [FIRST_NAME]]
                                [--phone-number [PHONE_NUMBER]]
                                [--address [ADDRESS]] [--id [ID]] [-l [LIST] |
                                -g [GET] | -c [CREATE] | -u [UPDATE] | -d
                                [DELETE] | -s [SEARCH]]

Phone Book API client -------------- Author: Angel Vargas

optional arguments:
  -h, --help            show this help message and exit
  --surname [SURNAME]   surname attribute --surname [surname]
  --first-name [FIRST_NAME]
                        first name attribute --first-name [first-name]
  --phone-number [PHONE_NUMBER]
                        phone number attribute --phone-number [phone-number]
  --address [ADDRESS]
  --id [ID]             contact id, required for operations such find and
                        delete
  -l [LIST], --list [LIST]
                        lists entries in the phone book
  -g [GET], --get [GET]
                        get an entry by id from the phone book
  -c [CREATE], --create [CREATE]
                        creates a new entry in the phone book
  -u [UPDATE], --update [UPDATE]
                        updates an existing entry in the phone book
  -d [DELETE], --delete [DELETE]
                        deletes an entry in the phone book
  -s [SEARCH], --search [SEARCH]
                        search for an entry in the phonebook
```


Testing:
--------

Test can be run from the base dir using `pytest`

    run `pytest -v`

Test Coverage:
--------------

To run and view the test coverage:

    run `pytest --cov=phonebook`
    
once the process finish, open the directory created: `htmlcov`

and open in your preferred browser `index.html` and inspect current test coverage

Current test coverage:

```

----------- coverage: platform win32, python 3.6.7-final-0 -----------
Name                               Stmts   Miss  Cover
------------------------------------------------------
phonebook\__init__.py                 28      6    79%
phonebook\common\__init__.py           0      0   100%
phonebook\common\contactentry.py      30      0   100%
phonebook\common\phonebook.py         64      2    97%
phonebook\config.py                   28      5    82%
phonebook\db\DB.py                    32     10    69%
phonebook\db\__init__.py              29      2    93%
phonebook\phone_book_api.py           72     16    78%
phonebook\support.py                   8      2    75%
------------------------------------------------------
TOTAL                                291     43    85%




```

First pre-release is published.

Author: Angel Vargas