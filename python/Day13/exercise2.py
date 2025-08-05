"""
SMARTPHONE PURCHASE:

ask user to input budget

1. check if the budget is at least $500, if it is, check if the budget is $1000 or more. then recommed "Google pixel 9pro", otherwise, recommed "Iphone"

2. if budget is below $500, if it is, and at least $200. then recommed "Redmi" otherwise recommed "save more"
"""


budget = int(input("Enter your budget to purchase a phone. \n $"))

if budget >= 500:
    if budget >= 1000:
        print("Google Pixel 9pro")
    else:
        print("iphone")
else:
    if budget >= 200:
        print("Redmi")
    else:
        print("Save more")

