class BankAccount():
    _name = ""
    _phone = ""
    _address = ""
    _balance = 0

    def __init__(self, name, phone, address):
        self._name = name
        self._phone = phone
        self._address = address

    @property
    def name(self):
        return self._name

    @property
    def phone(self):
        return self._phone

    @property
    def address(self):
        return self._address

    @property
    def balance(self):
        return self._balance

    def deposit(self, value):
        if (value < 0):
            raise Exception("invalid value")

        self._balance += value

    def withdraw(self, value):
        if (value < 0):
            raise Exception("invalid value")

        if (value > self._balance):
            raise Exception("insuficient funds")

        self._balance -= value
        return value
