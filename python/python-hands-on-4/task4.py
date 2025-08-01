"""
Task 4: Tech Conference Registration
The Jos Tech Conference registered participants under ticket categories:

participants = {"VIP": "Alice", "Regular": "Bob", "Student": "Charlie"}

During the first day:
- A "Guest" participant named "Daisy" joined.
- The "Student" participant canceled their registration.
- The organizers created a record for the day before removing the most recently added participant from the live system.
"""

# print(participants_snapshot)
# print(participants)
#

participants = {"VIP": "Alice", "Regular": "Bob", "Student": "Charlie"}




# Added the new guest 

participants.update({"Guest": "Daisy"})

# remove students 
participants.pop("Student")
print(participants)

# record before removing last

new_record = participants.copy()

print(new_record)

print(f"The new record is ", new_record)

participants.popitem()

print(participants)



