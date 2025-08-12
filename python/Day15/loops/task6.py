"""
print and display numbers from the list that are divisible by 5 with the following conditions
1. if the number is greater than 150. skip the to the next number 
2. if the number is greater than 500, it should stop

"""

numbers = [12,75,150,180,145,525,50]

for number in numbers:
    if number > 500:
        break
    if number > 150:
        continue
    if number % 5 == 0:
        print(number)

