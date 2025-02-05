class BankAPI:
    def __init__(self):
        self.accounts = {
            "1111-1111": {"pin": "1111", "balances": {"checking": 500, "savings": 1000}},
            "2222-2222": {"pin": "2222", "balances": {"checking": 300, "savings": 800}}
        }
    
    def verify_pin(self, card_number, pin):
        return self.accounts.get(card_number, {}).get("pin") == pin
    
    def get_balance(self, card_number, account_type):
        return self.accounts.get(card_number, {}).get("balances", {}).get(account_type, None)
    
    def deposit(self, card_number, account_type, amount):
        if amount > 0:
            self.accounts[card_number]["balances"][account_type] += amount
            return True
        return False
    
    def withdraw(self, card_number, account_type, amount):
        if 0 < amount <= self.accounts[card_number]["balances"][account_type]:
            self.accounts[card_number]["balances"][account_type] -= amount
            return True
        return False