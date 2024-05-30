import unittest
from baking_system import BankAccount


class TestBankAccount(unittest.TestCase):
    def test_should_generate_bank_account_with_name_phone_address(self):
        bank_account = BankAccount(
            "Luan",
            "11976098818",
            "Natale Beneli Street, 27, Planalto"
        )

        self.assertEqual(bank_account.name, "Luan")
        self.assertEqual(bank_account.phone, "11976098818")
        self.assertEqual(bank_account.address,
                         "Natale Beneli Street, 27, Planalto")
        self.assertEqual(bank_account.balance, 0)

    def test_should_not_allow_update_properties_directly(self):
        bank_account = BankAccount(
            "Luan",
            "11976098818",
            "Natale Beneli Street, 27, Planalto"
        )

        try:
            bank_account.name = 123
            raise Exception("should have failed with attribute error")
        except AttributeError:
            self.assertEqual(bank_account.name, "Luan")

        try:
            bank_account.phone = 123
            raise Exception("should have failed with attribute error")
        except AttributeError:
            self.assertEqual(bank_account.phone, "11976098818")

        try:
            bank_account.address = 123
            raise Exception("should have failed with attribute error")
        except AttributeError:
            self.assertEqual(bank_account.address,
                             "Natale Beneli Street, 27, Planalto")

        try:
            bank_account.balance = 10000
            raise Exception("should have failed with attribute error")
        except AttributeError:
            self.assertEqual(bank_account.balance, 0)

    def test_deposit(self):
        bank_account = BankAccount(
            "Luan",
            "11976098818",
            "Natale Beneli Street, 27, Planalto"
        )

        bank_account.deposit(2000)

        self.assertEqual(bank_account.balance, 2000)

    def test_deposit_with_negative_value(self):
        bank_account = BankAccount(
            "Luan",
            "11976098818",
            "Natale Beneli Street, 27, Planalto"
        )

        try:
            bank_account.deposit(-2000)
            raise Exception("should have failed with invalid value")
        except Exception as error:
            self.assertEqual(bank_account.balance, 0)
            self.assertEqual(error.__str__(), "invalid value")

    def test_withdraw_greater_than_balance(self):
        bank_account = BankAccount(
            "Luan",
            "11976098818",
            "Natale Beneli Street, 27, Planalto"
        )

        try:
            bank_account.withdraw(2000)
            raise Exception("should have failed with insuficient funds")
        except Exception as error:
            self.assertEqual(bank_account.balance, 0)
            self.assertEqual(error.__str__(), "insuficient funds")

    def test_withdraw_with_negative_value(self):
        bank_account = BankAccount(
            "Luan",
            "11976098818",
            "Natale Beneli Street, 27, Planalto"
        )

        try:
            bank_account.withdraw(-2000)
            raise Exception("should have failed with invalid value")
        except Exception as error:
            self.assertEqual(bank_account.balance, 0)
            self.assertEqual(error.__str__(), "invalid value")

    def test_withdraw(self):
        bank_account = BankAccount(
            "Luan",
            "11976098818",
            "Natale Beneli Street, 27, Planalto"
        )

        bank_account.deposit(2000)

        withdraw = bank_account.withdraw(500)

        self.assertEqual(withdraw, 500)
        self.assertEqual(bank_account.balance, 1500)
