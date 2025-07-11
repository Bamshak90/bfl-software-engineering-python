'''
PI = 3.1415
print(f"The initial value of PI to two decimal {PI:.6f}")

remainder = 5 / 3 

print(f"Balance: {remainder:.2f}")

'''

'''
heigth = float(input("Enter your heigth: \n >>>"))
print(f"Your heigth is {heigth:.2f}")

'''
account_balance = 50000000
print(f"Your account balance is: \n${account_balance:,.2f}")

bio = 'I am a "programmer" '

print(bio)

#shows how to add tab using backslash 
print("id|\t Name | \t Gender")
print("1| \t Mark | \t Male")
print("2| \t Mimi | \t Female")
print("Backslash \\")

#this code makes an alert sound
#print("backslash \a`")


#checking if the character starts with the present letter in the string and it returns true or false
name = "My name is Mark"
print(name.startswith("My"))

'''

isMarried = input("").lower()
print(isMarried.startswith("true"))

'''

fruits = "Apple Mango Orange Banana Kiwi"
print(fruits)
list_of_fruits = fruits.split(" ")
print(list_of_fruits)
print(list_of_fruits[2])
celebrities = "Davido-Wizkid-Rema-Ruger-Buju"
list_of_celebrities = celebrities.split("-")
print(list_of_celebrities)
