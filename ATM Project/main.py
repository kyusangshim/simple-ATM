from bankapi import BankAPI
from atm import ATM
    

bank_api = BankAPI()
atm = ATM(bank_api)

atm.run()

