'''

You try to withdraw money from a Nigerian ATM.
  The ATM has only ₦1000 notes and you have ₦10,000 in your account.
   The machine allows withdrawal only if the amount requested is less than or equal to your balance.
  The user enters the amount.

   Your  program  should decide:
   Whether to allow the transaction?
   Or deny it with a message: 
   “Insufficient funds or invalid amount”?

'''

account_balance = 10000

withdrawal = float(input("Enter the amount to withdraw: \n$"))

balance = account_balance - withdrawal

if withdrawal > 0 and withdrawal <= account_balance:
    if withdrawal % 1000 == 0:
        print(f"You have been paid the sum of ${withdrawal:,.2f} \nYour remaining balance is ${balance:,.2f}")
    else:
        print("invalid amount")

elif withdrawal > account_balance:
    print("Insufficient funds")
else:
    print("Amount out of range")

