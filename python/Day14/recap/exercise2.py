print(
    """
    Password Validation app
    """
)

password = int(input("Create a Password"))
confirm = int(input("Confirm password"))

if password == confirm:
    print("Password match")
else:
    print("password dose not match")
