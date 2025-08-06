password = 1234
user_db = ["core", "tk", "mp"]
is_verified = True


user_name = input("Enter your username: ")

if user_name in user_db:
    print("Account exist")
    confirm = int(input("Enter your password: "))
    if confirm == password:
        print("password matches, login successful")
        if is_verified == True:
            print("You are verified")
        else:
            print("You are not verified")
    else:
        print("wrong password")
else:
    print("Account does not exist")
