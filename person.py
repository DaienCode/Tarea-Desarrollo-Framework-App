import json


class Client(object):
    def __init__(self, id_person: int, fullname: str = 'Name', phone: str = '+001234567890', email: str = 'fullname@example.com'):
        self._id = id_person
        self._fullname = fullname
        self._phone = phone
        self._email = email

    def __str__(self):
        return '%s, %s, %s, %s' % (self._id, self._fullname, self._phone, self._email)
    
    @property
    def id_person(self) -> int:
        return self._id

    @id_person.setter
    def id_person(self, id_person: int):
        self._id = id_person

    @property
    def fullname(self) -> str:
        return self._fullname

    @fullname.setter
    def fullname(self, fullname: str):
        self._fullname = fullname

    @property
    def phone(self) -> str:
        return self._phone
    
    @phone.setter
    def phone(self, phone):
        self._phone = phone

    @property
    def email(self) -> str:
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email


class ClientEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__