from phonebook.data.db import DB
from phonebook.common.contactentry import ContactEntry


class PhoneBook:
    """
    common class

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
        :return: data index
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

        result = self.db.execute(query, value)
        self.db.commit()
        return result.lastrowid

    def find(self, _id) -> dict:
        """
        Find an entry in the Phone Book based on their id
        :param _id:
        :return: return a dict with the data queried from the database
        """
        query = ('''SELECT * FROM phone_book
        WHERE id=?''')

        value = (
            str(_id)
        )

        result = self.db.execute(query, value)
        return result.fetchone()

    def update(self, **kwargs) -> int:
        """
        Update phone book entry
        :param kwargs:
        :return: number of entries updated
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

        result = self.db.execute(query, values)
        self.db.commit()
        row_count = result.rowcount

        return row_count

    def delete(self, _id) -> int:
        """
        Find an entry in the Phone Book based on their id and delete it
        :param _id:
        :return: number of entries deleted
        """
        query = ('''DELETE FROM phone_book
        WHERE id=?''')

        value = (
            str(_id)
        )

        result = self.db.execute(query, value)
        self.db.commit()
        return result.rowcount

    def search(self, **kwargs) -> dict:
        """
        Search for an entry in the table phone_book
        :param kwargs: [table columns]=value, can search by multiple columns, or a single column,
        :return: collection
        """
        cols = ""
        values = ()
        keys = ()
        tup_idx = 0
        for key, value in kwargs.items():
            if cols != "":
                cols += "and "
            cols += "{0["+str(tup_idx)+"]} LIKE ? "
            values = values + ("%"+value+"%",)
            keys = keys + (key,)
            tup_idx += 1

        query = "SELECT * from phone_book WHERE " + cols
        query = query.format(keys)
        result = self.db.execute(query, values)

        return result.fetchall()












