class ContactEntry:
    """
    ContactEntry DTO
    """
    def __init__(self, surname: str, firstname: str, phone_number: str, address=""):
        self.surname = surname
        self.firstname = firstname
        self.phone_number = phone_number
        self.address = address

    @property
    def surname(self) -> str:
        return self._surname

    @property
    def firstname(self) -> str:
        return self._firstname

    @property
    def phone_number(self) -> str:
        return self._phone_number

    @property
    def address(self) -> str:
        return self._address

    @surname.setter
    def surname(self, surname: str) -> None:
        self._surname = surname

    @firstname.setter
    def firstname(self, firstname: str) -> None:
        self._firstname = firstname

    @phone_number.setter
    def phone_number(self, phone_number: str) -> None:
        self._phone_number = phone_number

    @address.setter
    def address(self, address: str) -> None:
        self._address = address