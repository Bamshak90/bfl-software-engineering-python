import  random
print("welcome to the Dice Rolling Game")

while True:
    choice = input("Do you want to roll a dice?(\"Y/Na\"): ").lower()

    if choice == "y":
        rand1 = random.randint(1,10)
        rand2 = random.randint(1,20)
        print(f"You roll {rand1} and {rand2}")
    elif choice == "n":
        print("Thank you for playing")
        break
    else:
        print("Invalid choice")



