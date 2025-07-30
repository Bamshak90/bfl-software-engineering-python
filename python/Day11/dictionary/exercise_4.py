contact_list = {
    "MP": 903985,
    "Fly": 82938,
    "Dave": 9183838,
    "Tosin": 7838383,
    "Mark": 3
}
print(contact_list)
print(contact_list["MP"])
print(contact_list.get("Fly"))
# the update method can be used to add a new value or change a value 

contact_list.update({"Dave": 9898})
contact_list.update({"Bello": 9898})
print(contact_list)

# the del keywored deletes an existing key and value from the dictionary

del contact_list["Bello"]
print(contact_list)

# the pop deletes an existing key

contact_list.pop("Fly")
print(contact_list.items(), type(contact_list.items()))

# the popitem method is used to remove the last item 
contact_list.popitem()
print(contact_list)

# the copy method is used to copy the dictionary to a new memory location in a new variable

new = contact_list.copy()
print(new)

# the method below stores the same contact_list to the new2 variable and if an item is deleted from new2 it also deletes on contact_list cause the use the same memory location

new2 = contact_list 
print(new2)
