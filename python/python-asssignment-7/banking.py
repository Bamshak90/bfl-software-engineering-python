accounts = {}

def create_account(account_number, name, **kwargs):
    """Create an account with optional features like overdraft_limit."""
    if account_number in accounts:
        return f"Account {account_number} already exists!"
    
    accounts[account_number] = {
        "name": name,
        "balance": kwargs.get("balance", 0.0),
        "overdraft_limit": kwargs.get("overdraft_limit", 0.0)
    }
    return f"Account for {name} created successfully."


def deposit(account_number, *amounts):
    """Deposit money into account.
       return "Account not found!" (if account does not exist)
    """
    if account_number not in accounts:
        return "Account not found!"
    
    total = sum(amounts)
    accounts[account_number]["balance"] += total
    return f"Deposited {total} into {accounts[account_number]['name']}'s account."


def withdraw(account_number, *amounts):
    """Withdraw money if balance is sufficient. else: insufficient funds"""
    if account_number not in accounts:
        return "Account not found!"
    
    total = sum(amounts)  
    balance = accounts[account_number]["balance"]
    overdraft = accounts[account_number]["overdraft_limit"]
    
    if balance + overdraft >= total:
        accounts[account_number]["balance"] -= total
        return f"Withdrew {total} from {accounts[account_number]['name']}'s account."
    else:
        return "Insufficient funds!"


def transfer(from_acc, to_acc, amount):
    """Transfer money between accounts. if funds is sufficient"""
    if from_acc not in accounts or to_acc not in accounts:
        return "One or both accounts not found!"
    
    balance = accounts[from_acc]["balance"]
    overdraft = accounts[from_acc]["overdraft_limit"]
    
    if balance + overdraft >= amount:
        accounts[from_acc]["balance"] -= amount
        accounts[to_acc]["balance"] += amount
        return f"Transferred {amount} from {accounts[from_acc]['name']} to {accounts[to_acc]['name']}."
    else:
        return "Insufficient funds!"



print(create_account("A1", "Mark", balance=1000, overdraft_limit=200))
print(create_account("A2", "Bob", balance=500))
print(deposit("A1", 200, 300))    
print(withdraw("A2", 100, 200))   
print(transfer("A1", "A2", 400))
print(accounts)
