"""
TASK: Create a BankAccount class.

Requirements:
1. Each account should have an owner name and a starting balance.
2. Provide a method to deposit money.
3. Provide a method to withdraw money (only if sufficient balance).
4. Provide a method to check current balance.

Example Usage:
    acc = BankAccount("Alice", 1000)
    acc.deposit(500)
    acc.withdraw(200)
    print(acc.get_balance())  # 1300
"""

class BankAccount:
  def __init__(self):
    self.customer = {}
  
  def register_customer(self, name, balance):
    if name not in self.customer:
      self.customer[name] = balance
      print(f"{name} has register successfully")

    else: 
      print(f"{name} is already a customer")

  def deposit_amount(self, name, balance):
    if name in self.customer:
      self.customer[name] += balance
      print(f"{name} you have deposited {balance} to your account")
      print(self.customer)
    else:
      print(f"{name}, You are not a customer")

  def withdraw_amount(self, name, balance):
    if name in self.customer:
      if self.customer[name] >= balance:
        self.customer[name] -= balance
        print(f"{name}, You have successfully withdrawed {balance}")
        print(self.customer)
      else:
        print(f"{name}, you don't have sufficient balance")
    else:
      print(f"{name}, You are not a customer")

  def check_balance(self, name):
    if name in self.customer:
        print(f"{name}, your balance is: {self.customer[name]}")
    else:
        print(f"{name}, you are not a customer")



account = BankAccount()
account.register_customer("Mark", 1000)
account.deposit_amount("Mark", 10000)
account.withdraw_amount("Mark", 100000)
account.check_balance("Mark")