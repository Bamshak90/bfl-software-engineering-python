count = 1
secret_number = 5
i = 1

while count <= 5:
    user_guess = int(input("Enter a number:\n >>> "))
    if user_guess == secret_number:
        print("correct")
        break
    else:
        print("incorret")
        count += 1
