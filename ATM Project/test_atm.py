import unittest
from atm import ATM
from bankapi import BankAPI

class TestATM(unittest.TestCase):
    def setUp(self):
        self.bank_api = BankAPI()
        self.atm = ATMController(self.bank_api)
        self.card_number = "1111-1111"
        self.pin = "1111"
    
    def test_insert_card(self):
        self.assertTrue(self.atm.insert_card(self.card_number))
    
    def test_invalid_card(self):
        self.assertFalse(self.atm.insert_card("9999-9999"))
    
    def test_enter_pin(self):
        self.atm.insert_card(self.card_number)
        self.assertTrue(self.atm.enter_pin(self.pin))
    
    def test_invalid_pin(self):
        self.atm.insert_card(self.card_number)
        self.assertFalse(self.atm.enter_pin("0000"))
    
    def test_get_balance(self):
        self.atm.insert_card(self.card_number)
        self.atm.enter_pin(self.pin)
        self.atm.select_account("checking")
        self.assertEqual(self.atm.get_balance(), 500)
    
    def test_withdraw_success(self):
        self.atm.insert_card(self.card_number)
        self.atm.enter_pin(self.pin)
        self.atm.select_account("checking")
        self.assertTrue(self.atm.withdraw(100))
        self.assertEqual(self.atm.get_balance(), 400)
    
    def test_withdraw_fail(self):
        self.atm.insert_card(self.card_number)
        self.atm.enter_pin(self.pin)
        self.atm.select_account("checking")
        self.assertFalse(self.atm.withdraw(1000))
    
    def test_deposit(self):
        self.atm.insert_card(self.card_number)
        self.atm.enter_pin(self.pin)
        self.atm.select_account("checking")
        self.assertTrue(self.atm.deposit(200))
        self.assertEqual(self.atm.get_balance(), 700)

if __name__ == "__main__":
    unittest.main()
