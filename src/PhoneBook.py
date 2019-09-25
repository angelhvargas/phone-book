from src.DB import DB
from src.Contact import ContactEntry


class PhoneBook:
    """
    PhoneBook class

    Describe and controls behaviour of the operations in the phone book.
    """
    db = None

    def __init__(self, db_path='test_database.sqlite3'):
        """"""
        database = DB(db_path).connect()
        self.db = database

    def create(self, contact_entry: ContactEntry) -> int:
        """
        Create an entry in the Phone Book
        :param contact_entry:
        :return: db index
        """
        query = ('''INSERT INTO phone_book
        (surname, firstname, phone_number, address)
        VALUES (?, ?, ?, ?)''')

        value = (
            contact_entry.surname,
            contact_entry.firstname,
            contact_entry.phone_number,
            contact_entry.address
        )

        result = self.db.cursor().execute(query, value)
        self.db.commit()
        return result.lastrowid

    def find(self, _id) -> dict:
        """
        Find an entry in the Phone Book based on their id
        :param _id:
        :return:
        """
        query = ('''SELECT * FROM phone_book
        WHERE id=?''')

        value = (
            str(_id)
        )

        result = self.db.cursor().execute(query, value)
        return result.fetchone()

    def update(self, **kwargs) -> dict:
        """
        Update phone book entry
        :param kwargs:
        :return: dict
        """
        cols = ""
        idx = kwargs.pop('idx')
        values = ()
        for key, value in kwargs.items():
            if key == 'idx':
                continue
            cols += key+"=? "
            values = values + (value,)

        values = values + (str(idx),)

        query = "UPDATE phone_book SET " + cols + " WHERE id=?"

        self.db.cursor().execute(query, values)
        row_count = self.db.cursor().rowcount

        return row_count

    def delete(self, _id) -> dict:
        """
        Find an entry in the Phone Book based on their id and delete it
        :param _id:
        :return:
        """
        query = ('''DELETE FROM phone_book
        WHERE id=?''')

        value = (
            str(_id)
        )

        result = self.db.cursor().execute(query, value)
        self.db.commit()
        return result.rowcount








