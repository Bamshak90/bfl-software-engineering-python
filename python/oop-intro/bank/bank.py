'''Features for the Bank Account System 🏦

Create an account with:

Account holder’s name

Account number (we can generate this randomly)

Initial balance (default = 0)

Deposit money (increase balance).

Withdraw money (check balance first so it doesn’t go negative).

Check balance (display current balance).

(Optional later) Account type (Savings, Current).
'''
import random

class Bank:
  def __init__(self):
    self.customers = {}

  
  def generate_account_number(self):
    return int("2" + "".join([str(random.randint(0, 9)) for _ in range(9)]))


  def create_account(self,name,account_type = "savings"):
    while True:
      account_number = self.generate_account_number()
      if account_number not in self.customers:
        self.customers[account_number] = {
          "name": name,
          "account_type": account_type,
          "balance": 0,
          "Frozen": False
        }
        return account_number

  def deposit(self,account_number, top_up):
    if account_number in self.customers:
      if top_up <= 0:
        return f"{top_up} can not be 0 or negative"
      else:
        self.customers[account_number]["balance"] += top_up
        return f"Deposit successful. New balance: {self.customers[account_number]['balance']}"
    else:
      return f"{account_number} does not exist"

  def withdraw(self, account_number, amount):
    if account_number in self.customers:
        if amount <= 0:
            return "Withdrawal amount must be greater than 0"
        
        if self.customers[account_number]["balance"] >= amount:
            self.customers[account_number]["balance"] -= amount
            return f"You have withdrawn {amount} from {account_number}. New balance: {self.customers[account_number]['balance']}"
        else:
            return "Insufficient funds"
    else:
        return f"{account_number} does not exist"
    
  def check_balance(self, account_number):
    if account_number in self.customers:
        balance = self.customers[account_number]["balance"]
        return f"Balance for {account_number}: {balance}"
    else:
        return f"{account_number} does not exist"
    
  def transfer(self, from_account, to_account):
     if from_account in self.customers:
        if self.customers[account_number]["balance"] > 0:
           




bank = Bank()
acc1 = bank.create_account("Mark",)
acc2 = bank.create_account("John", "Current")


print(bank.deposit(acc1, 50000)) 
print(bank.deposit(acc2, -100)) 
print(bank.deposit(123456, 200))

print(bank.withdraw(acc1, 40000))

print(bank.check_balance(acc1))  
print(bank.check_balance(12345)) 

print("Accounts created:")
print(bank.customers)
print("Mark’s account number:", acc1)
