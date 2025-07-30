import pprint;

oxford = {
    "apple": "a common fruit",
    "ball": "a round object",
    "cat": "an animal of the family Felidae",
    "dog": "nangwans dog meat",
    "egg": "a spherical object",
    "fish": "a cold blooded vertebrate",
    "goat": "Messi",
    "house": "a building",
    "idiot": "wild animal",
    "jackal": "a wild animal"
}

pprint.pprint(oxford)

print("meaning of ball: " + oxford["ball"])

oxford["kettle"] = "a vessel used to boil water"

# we can change the value of a key using the method below 

oxford["jackal"] = "a wild animal in the bush"
pprint.pprint(oxford)

# the print below allows us to print the keys of the dictionary oxford
print(oxford.keys())

# the print below allows us to print the values of the dictionary oxford
print(oxford.values())
