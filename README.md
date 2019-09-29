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

###### 2. run server

from the base directory execute:

`flask run`


Client usage
------------

The client needs the server running to get it connected to the Phone Book service.

Run from your console:
 
`phonebook.py --help`

#### some usage examples:

`phonebook.py --list-all `

`phonebook.py --find [args] `

`phonebook.py --create [args] `

`phonebook.py --delete [args] `

`phonebook.py --search [args]`  

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

```bash
----------- coverage: platform win32, python 3.6.7-final-0 -----------
Name                               Stmts   Miss  Cover
------------------------------------------------------
phonebook\__init__.py                 28     23    18%
phonebook\common\__init__.py           0      0   100%
phonebook\common\contactentry.py      30      0   100%
phonebook\common\phonebook.py         63      2    97%
phonebook\config.py                   30      5    83%
phonebook\db\DB.py                    32     10    69%
phonebook\db\__init__.py              24      5    79%
phonebook\phone_book_api.py           40      8    80%
------------------------------------------------------
TOTAL                                247     53    79%


```

Work on progress, no releases yet.

Author: Angel Vargas