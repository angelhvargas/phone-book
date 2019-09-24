from src.DB import DB


class PhoneBook:
    """
    PhoneBook class

    Describe and controls behaviour of the operations in the phone book.
    """
    def __init__(self):
        """"""
        database = DB()
        self.db = database.connect()


