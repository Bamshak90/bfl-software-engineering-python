"""
student = {
    "name": "legolas",
    "has_registered": True,
    "has_paid": True,
    "has_internet": False
 }

only student that have registered are eligible for exams. Any student that has not registered should be denied access with message "Access denied".

1. In as much as students have registered, if they haven't paid fees, the should be denied access to exams with the message "pay your fees".

2. If they have paid and have internet access, message "Allow access", else "check your internet connection"

"""

student = {
    "name": "legolas",
    "has_registered": True,
    "has_paid": True,
    "has_internet": False
 }

registered = student["has_registered"]
paid = student["has_paid"]
internet = student["has_internet"]


if registered == True:
    if paid == True:
        if internet == True:
            print("Allow access")
        else: 
            print("Check your internet connection")
    else:
        print("pay your fees")
else:
    print("Access denied")

