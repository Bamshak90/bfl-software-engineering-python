"""
MOVIE TICKET DISCOUNT:

You are building a movie ticketing system.

1. persons 18 or older can buy a ticket.
out put "can buy a ticket"

2. If they are 60 or older, they get "senior discount":
output: "senior discount"

3 If they are under 18 and 12 years old, they can buy teen ticket.

output: "teen ticket"

otherwise, they can buy "kids ticket"

"""


age = int(input("Enter your age to buy a movie ticket: \n"))


if age >= 18:
    print("Can buy a Ticket")
    if age >= 60:
        print("Senior Discount")
elif age < 18 and age == 12:
    print("Teen ticket")
else:
   print("Kids ticket") 
