# A list is a collection of items in a particular order

# A list is a collection of items. A list houses different elements of different data-type.

#using a constructor to define list
list_of_countries = list()
print(type(list_of_countries))

# Using the square bracket
states = []
print(type(states))

countries = ["Australia", "Malawi", "Russia", "Nigeria", "USA", "Iran"]
print(countries)

# Adding elements to a list

favourite_fruits = ["Mango", "Apple", "Orang", "Kiwi", "Banana"]
print("Before adding")
print(favourite_fruits)
favourite_fruits[0] = "Coco-nut"
print("After updating")
print(favourite_fruits)

countries = ["Australia", "Malawi", "Russia", "Nigeria", "USA", "Iran"]
print(countries[0:3])


# Nested list
andriod = ["samsung", "Itel", "Redmi", "Oppo"]
ios = ["11pro max", "xr", "16 plus", "7 plus"]
phones = [andriod,ios]

print(phones)
