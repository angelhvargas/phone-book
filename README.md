phone-book
--------------
Author: Angel Vargas

Usage
-----

Run from your console:
 
``

where: 
    
    

Requirements:
-------------
1. Python 3.7

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

Current coverage:

```bash
Name                               Stmts   Miss  Cover
------------------------------------------------------
phonebook\__init__.py                  0      0   100%
phonebook\__main__.py                  0      0   100%
phonebook\app.py                      12     12     0%
phonebook\common\__init__.py           0      0   100%
phonebook\common\contactentry.py      30      0   100%
phonebook\common\phonebook.py         55      2    96%
phonebook\data\__init__.py             0      0   100%
phonebook\data\db.py                  32     10    69%
------------------------------------------------------
TOTAL                                129     24    81%

```