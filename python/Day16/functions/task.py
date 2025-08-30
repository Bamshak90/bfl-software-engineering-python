'''
write a function get_first_item(items) that returns the first item in list
'''


fruits = ["apple","banana","cherry","orange"]
numbers = [10,20,30,40,50]
names = ["Alice","Bob","Charlie"]
school = []

def get_first_item(items):
    if len(items) == 0:
        pass
    for item in items:
        return items[0]
    return items
print(get_first_item(school))


'''
write a function get_max(numbers) that returns the largest number in a list
'''

list1 = [4,9,2,7,5]
list2 = [100,259,30,400,15]
list3 = [-5,-10,-3,-8,-1]
list4 = []

def get_max(numbers):
    total = 0
    for num in numbers:
        if num > total:
            total = num
    return total


print(get_max(list4))
