"""
Task 1: Music Concert Ticketing System
During the Jos Summer Music Concert, ticket sales were recorded as follows:

tickets = {"VIP": 50, "Regular": 150, "Student": 75}

Later in the day:
- A new "Backstage" experience with 10 tickets was introduced.
- The "Student" category sold out completely.
- The team wanted to keep a record of the day’s sales before preparing for next week’s concert.
"""

tickets = {"VIP": 50, "Regular": 150, "Student": 75}

# adding a new key and value
tickets.update({"Backstage": 10})

# removing the Student category 
soldout = tickets.pop("Student")
print(tickets)

# suming todays record

todays_record = {
    "Avaliable": tickets,
    "soldout": soldout
}

print(todays_record)

