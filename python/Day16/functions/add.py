# 

from datetime import datetime

def calculate_age(year_of_birth):
  current_year = datetime.now().year
  return current_year - year_of_birth
#print(calculate_age(2000))


def bio(name,year,gender):
  return {
    "name": name,
    "year": calculate_age(year),
    "gender": gender
  }

print(bio("mark", 2000, "M"))

def task16_factorial(n):
    """
    Task 16:
    Write a function that accepts a number and returns its factorial
    using a loop (not recursion).
    Example: factorial(5) → 120
    """
    factorial = 1
    for num in range(n, 1, - 1):
        factorial *= num
    print(factorial)
task16_factorial(5)

