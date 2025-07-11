



#write a code that takes users current age and returns the actual age 

date_of_birth = int(input("Enter your date of birth:"))
current_year = int(2025)
actaul_age = current_year - date_of_birth

print(f"You are {actaul_age} years old")


#write a program that returns the remaining balance in the account for the user 

account_balance = 10000

withdraw = float(input(f"How much do you want to spend from: ${account_balance} \n>>> "))

remaining_balance = 10000 - withdraw

print(f"Your remaining balance is ${remaining_balance:,.2f}")


#using string slicing out python to the user

message = "rpyoagrhmtn"


py = message[1:3]
t = message[9:10]
h = message[7:8]
o = message[3:4]
n = message[10]

print(f"{py}{t}{h}{o}{n}")




