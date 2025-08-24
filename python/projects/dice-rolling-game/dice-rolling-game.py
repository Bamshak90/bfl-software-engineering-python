import  random
print("welcome to the Dice Rolling Game")

while True:
    choice = input("Do you want to roll a dice?(\"Y/Na\"): ").lower()

    if choice == "y":
        rand = random.randint(1,30)
        print(rand)
    elif choice == "n":
        print("Thank you for playing")
        break



