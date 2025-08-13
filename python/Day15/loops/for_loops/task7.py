'''
print the numbers in a reverse other with out using any method

print the largest number
'''

numbers = [12,75,150,180,145,525,50]


count = len(numbers) - 1
for number in range(len(numbers)):
    print(numbers[count])
    count = count -1


big = 0

for number in numbers:
    if number > big:
        big = number
print(f"{big} is the largest")
