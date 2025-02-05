import time

class ATM:
    def __init__(self, bank_api):
        self.bank_api = bank_api
        self.current_card = None
        self.current_account = None
    
    def insert_card(self, card_number):
        if card_number in self.bank_api.accounts:
            self.current_card = card_number
            return True
        return False
    
    def enter_pin(self, pin):
        if self.current_card and self.bank_api.verify_pin(self.current_card, pin):
            return True
        return False
    
    def select_account(self, account_type):
        if self.current_card and account_type in self.bank_api.accounts[self.current_card]["balances"]:
            self.current_account = account_type
            return True
        return False
    
    def get_balance(self):
        if self.current_card and self.current_account:
            return self.bank_api.get_balance(self.current_card, self.current_account)
        return None
    
    def deposit(self, amount):
        if self.current_card and self.current_account:
            return self.bank_api.deposit(self.current_card, self.current_account, amount)
        return False
    
    def withdraw(self, amount):
        if self.current_card and self.current_account:
            return self.bank_api.withdraw(self.current_card, self.current_account, amount)
        return False
    
    def eject_card(self):
        self.current_card = None
        self.current_account = None
    
    def run(self):
        pin_count = 0
        card_count = 0
        while True: 
            if self.insert_card(input("카드 번호를 입력하세요: ")):
                print()
                time.sleep(1)
                while True:
                    if self.enter_pin(input("핀 번호를 입력하세요: ")):
                        print()
                        time.sleep(0.5)
                        while True:
                            n = input("계좌를 선택하세요: \n1. checking, 2. savings\n")
                            if n == "1":
                                if self.select_account("checking"):
                                    while True:
                                        print()
                                        time.sleep(0.5)
                                        service = input("원하는 서비스를 선택하세요: \n1. 잔액 조회 2. 입금 3. 출금\n")
                                        
                                        if service == "1":
                                            print()
                                            time.sleep(1)
                                            print(f"현재 잔액: {self.get_balance()} 원")
                                            while True:
                                              print()
                                              time.sleep(1)
                                              q = input("서비스를 종료하시겠습니까? : (Y/N)\n")
                                              if q == 'Y':
                                                  time.sleep(1)
                                                  print()
                                                  self.eject_card()
                                                  print("카드가 반환되었습니다.\n감사합니다.")
                                                  return
                                              elif q == 'N':
                                                  break
                                              else:
                                                  print()
                                                  print('다시 입력하세요.')
                                        
                                        elif service == "2":
                                            print()
                                            time.sleep(0.5)
                                            amount = int(input("입금할 금액을 입력하세요: "))
                                            if self.deposit(amount):
                                                print()
                                                time.sleep(1)
                                                print(f"{amount} 원 입금 완료! 현재 잔액: {self.get_balance()} 원")
                                                while True:
                                                  print()
                                                  time.sleep(1)
                                                  q = input("서비스를 종료하시겠습니까? : (Y/N)\n")
                                                  if q == 'Y':
                                                      time.sleep(1)
                                                      print()
                                                      self.eject_card()
                                                      print("카드가 반환되었습니다.\n감사합니다.")
                                                      return
                                                  elif q == 'N':
                                                      break
                                                  else:
                                                      print()
                                                      print('다시 입력하세요.')
                                            else:
                                                print()
                                                print("입금 실패! 올바른 금액을 입력하세요.")

                                        elif service == "3":
                                            print()
                                            time.sleep(0.5)
                                            amount = int(input("출금할 금액을 입력하세요: "))
                                            if self.withdraw(amount):
                                                print()
                                                time.sleep(1)
                                                print(f"{amount} 원 출금 완료! 현재 잔액: {self.get_balance()} 원")
                                                while True:
                                                  print()
                                                  time.sleep(1)
                                                  q = input("서비스를 종료하시겠습니까? : (Y/N)\n")
                                                  if q == 'Y':
                                                      time.sleep(1)
                                                      print()
                                                      self.eject_card()
                                                      print("카드가 반환되었습니다.\n감사합니다.")
                                                      return
                                                  elif q == 'N':
                                                      break
                                                  else:
                                                      print()
                                                      print('다시 입력하세요.')
                                            else:
                                                print()
                                                print("출금 실패! 잔액을 확인하세요.")
                                        
                                        else:
                                            print()
                                            print("잘못된 입력입니다. 다시 선택하세요.")

                                else:
                                    print()
                                    print("checking 계좌가 존재하지 않습니다.")
                                    return
                            
                            elif n == "2":
                                if self.select_account("savings"):
                                    while True:
                                        print()
                                        time.sleep(0.5)
                                        service = input("원하는 서비스를 선택하세요: \n1. 잔액 조회 2. 입금 3. 출금 4. 카드 반환\n")
                                        
                                        if service == "1":
                                            print()
                                            time.sleep(1)
                                            print(f"현재 잔액: {self.get_balance()} 원")
                                            while True:
                                              print()
                                              time.sleep(1)
                                              q = input("서비스를 종료하시겠습니까? : (Y/N)\n")
                                              if q == 'Y':
                                                  time.sleep(1)
                                                  print()
                                                  self.eject_card()
                                                  print("카드가 반환되었습니다.\n감사합니다.")
                                                  return
                                              elif q == 'N':
                                                  break
                                              else:
                                                  print()
                                                  print('다시 입력하세요.')
                                        
                                        elif service == "2":
                                            print()
                                            time.sleep(0.5)
                                            amount = int(input("입금할 금액을 입력하세요: "))
                                            if self.deposit(amount):
                                                print()
                                                time.sleep(1)
                                                print(f"{amount} 원 입금 완료! 현재 잔액: {self.get_balance()} 원")
                                                while True:
                                                  print()
                                                  time.sleep(1)
                                                  q = input("서비스를 종료하시겠습니까? : (Y/N)\n")
                                                  if q == 'Y':
                                                      time.sleep(1)
                                                      print()
                                                      self.eject_card()
                                                      print("카드가 반환되었습니다.\n감사합니다.")
                                                      return
                                                  elif q == 'N':
                                                      break
                                                  else:
                                                      print()
                                                      print('다시 입력하세요.')
                                            else:
                                                print()
                                                print("입금 실패! 올바른 금액을 입력하세요.")

                                        elif service == "3":
                                            print()
                                            time.sleep(0.5)
                                            amount = int(input("출금할 금액을 입력하세요: "))
                                            if self.withdraw(amount):
                                                print()
                                                time.sleep(1)
                                                print(f"{amount} 원 출금 완료! 현재 잔액: {self.get_balance()} 원")
                                                while True:
                                                  print()
                                                  time.sleep(1)
                                                  q = input("서비스를 종료하시겠습니까? : (Y/N)\n")
                                                  if q == 'Y':
                                                      time.sleep(1)
                                                      print()
                                                      self.eject_card()
                                                      print("카드가 반환되었습니다.\n감사합니다.")
                                                      return
                                                  elif q == 'N':
                                                      break
                                                  else:
                                                      print()
                                                      print('다시 입력하세요.')
                                            else:
                                                print()
                                                print("출금 실패! 잔액을 확인하세요.")
                                        else:
                                            print()
                                            print("잘못된 입력입니다. 다시 선택하세요.")
                                else:
                                    print()
                                    print("savings 계좌가 존재하지 않습니다.")
                                    return
                            else:
                                print("잘못된 번호입니다. ")
                                continue
                    else:
                        pin_count += 1
                        if pin_count == 3:
                            print(f"핀번호를 잘못 입력하셨습니다! {pin_count}/3")
                            print()
                            print("3번의 오류 발생! 시스템이 종료됩니다.")
                            return
                        print(f"핀번호를 잘못 입력하셨습니다! {pin_count}/3")
            else:
                card_count += 1
                if card_count == 3:
                    print(f"카드번호를 잘못 입력하셨습니다! {card_count}/3")
                    print()
                    print("3번의 오류 발생! 시스템이 종료됩니다.")
                    return
                print(f"카드번호를 잘못 입력하셨습니다! {card_count}/3")