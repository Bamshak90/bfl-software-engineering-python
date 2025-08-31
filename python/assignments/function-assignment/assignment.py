# assignment 
# ======================
# FUNCTIONS & SCOPE TASKS
# ======================

# 1
def task1_sum_of_two_numbers(a, b):
    """
    Task 1:
    Write a function that accepts two numbers (a and b) as parameters
    and returns their sum.
    Test the function by calling it with different numbers.
    """
    result = a + b 
    return result
total = task1_sum_of_two_numbers(2,5)
print(total)


# 2
def task2_square_number(n):
    """
    Task 2:
    Write a function that accepts a number and returns its square.
    Example: square_number(5) → 25
    """
    square = n * n
    return square
total = task2_square_number(5)
print(total)

# 3
def task3_greet_user(name):
    """
    Task 3:
    Write a function that accepts a person's name as a parameter
    and prints a greeting message like: "Hello, John!"
    """
    name = f"hello {name}"
    return name
total = task3_greet_user("Mark")
print(total)


# 4
def task4_area_of_rectangle(length, width):
    """
    Task 4:
    Write a function that accepts the length and width of a rectangle
    and returns its area.
    Formula: area = length * width
    """
    area = length * width
    return area
total = task4_area_of_rectangle(5, 10)
print(total)


# 5
def task5_perimeter_of_square(side):
    """
    Task 5:
    Write a function that accepts the side length of a square
    and returns its perimeter.
    Formula: perimeter = 4 * side
    """
    perimeter = 4 * side
    return perimeter
total = task5_perimeter_of_square(6)
print(total)


# 6
def task6_celsius_to_fahrenheit(celsius):
    """
    Task 6:
    Write a function that converts a temperature from Celsius to Fahrenheit.
    Formula: (celsius * 9/5) + 32
    """
    calculate = (celsius * 9/5) + 32
    return calculate
total = task6_celsius_to_fahrenheit(8)
print(total)


# 7
def task7_find_max(a, b, c):
    """
    Task 7:
    Write a function that accepts three numbers as parameters
    and returns the largest number.
    """
    numbers = [a,b,c]
    max = 0
    for num in numbers:
        if num > max:
            max = num
    return max
total = task7_find_max(6,50,20)
print(total)



# 8
def task8_even_or_odd(n):
    """
    Task 8:
    Write a function that accepts a number and returns
    "Even" if the number is even, and "Odd" if the number is odd.
    """
    if n % 2 == 0:
        return "even"
    else:
        return "odd"
total = task8_even_or_odd(9)
print(total)


# 9
def task9_count_vowels(word):
    """
    Task 9:
    Write a function that accepts a word as a parameter
    and returns the number of vowels (a, e, i, o, u) in the word.
    Example: count_vowels("apple") → 2
    """
    count = 0
    vowels = "a,e,i,o,u" 
    for character in word:
        if character.lower() in vowels:
            count += 1
    return count
total = task9_count_vowels("fantastic")
print(total)


# 10
def task10_multiply_list(numbers):
    """
    Task 10:
    Write a function that accepts a list of numbers as a parameter
    and returns the product of all the numbers in the list.
    Example: multiply_list([1, 2, 3, 4]) → 24
    """
    total = 1
    for num in list1:
        total *= num
    return total
list1 = [1, 2, 5, 4]
total = task10_multiply_list(list1)
print(total)

    


# 11
def task11_reverse_string(text):
    """
    Task 11:
    Write a function that accepts a string as a parameter
    and returns the string reversed.
    Example: reverse_string("hello") → "olleh"
    """

    return text[::-1]
total = task11_reverse_string("mark")
print(total)


# 12
def task12_is_prime(n):
    """
    Task 12:
    Write a function that accepts a number as a parameter
    and returns True if the number is prime, otherwise False.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

total = task12_is_prime(5)
print(total)

# 13

trail = "i am global"
def task13_scope_demo():
    """
    Task 13:
    Demonstrate local and global scope.
    Create a global variable, and then inside a function,
    create a local variable with the same name. Print both
    to show how local and global scope works.
    """
    local = "i am local"
    print(local)
task13_scope_demo()
print(trail)


# 14
def task14_sum_list(numbers):
    """
    Task 14:
    Write a function that accepts a list of numbers
    and returns the sum of all the elements in the list.
    Do not use Python's built-in sum() function.
    """
    total = 0
    for num in numbers:
        total += num
    return total
total = task14_sum_list([2,3,4,5,6,7,8,9,90,1])
print(total)


# 15
def task15_average_of_list(numbers):
    """
    Task 15:
    Write a function that accepts a list of numbers
    and returns the average.
    Formula: average = sum of numbers / count of numbers
    """
    count_of_numbers = len(numbers)
    sum_of_numbers = 0
    for num in numbers:
        sum_of_numbers += num
    average = sum_of_numbers / count_of_numbers
    return average
total = task15_average_of_list([2,3,5,10])
print(total)





# 16
def task16_factorial(n):
    """
    Task 16:
    Write a function that accepts a number and returns its factorial
    using a loop (not recursion).
    Example: factorial(5) → 120
    """
    factorial = 1
    for num in range(1, n + 1):
        factorial *= num
    return factorial
total = task16_factorial(5)
print(total)


# 17
def task17_palindrome_check(word):
    """
    Task 17:
    Write a function that checks if a word is a palindrome.
    A palindrome reads the same forwards and backwards.
    Example: palindrome_check("madam") → True
    """
    w = word.lower()
    return w == w[::-1]
total = task17_palindrome_check("madam")
print(total)

# 18
def task18_convert_minutes_to_hours(minutes):
    """
    Task 18:
    Write a function that accepts minutes as input
    and converts it into hours and minutes.
    Example: 130 minutes → "2 hour(s) 10 minute(s)"
    """
    hours = minutes // 60
    minutes = minutes % 60
    total = f"the time is {hours} hour(s) {minutes} minute)s"
    return total
print(task18_convert_minutes_to_hours(130))


# 19
def task19_find_min(numbers):
    """
    Task 19:
    Write a function that accepts a list of numbers
    and returns the smallest number.
    Do not use Python's built-in min() function.
    """
    min = numbers[0]
    for num in numbers:
        if num < min:
            min = num
    return min
print(task19_find_min([2,3,4,5,6,7,8]))
    


# 20
def task20_simple_interest(principal, rate, time):
    """
    Task 20:
    Write a function that calculates simple interest.
    Formula: (principal * rate * time) / 100
    """
    interest = (principal * rate * time) / 100
    return interest
total = task20_simple_interest(20,13,7)
print(total)


# 21
def task21_calculator(a, b, operation):
    """
    Task 21:
    Write a function that works like a simple calculator.
    It should accept two numbers and an operation (+, -, *, /)
    and return the result.
    Example: calculator(4, 2, "+") → 6
    """
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    else:
        return f"invalid operation"
    
total = task21_calculator(2,5,"+")
print(total)


# 22
def task22_string_length(text):
    """
    Task 22:
    Write a function that accepts a string
    and returns its length without using len().
    """
    count = 0
    for _ in text:
        count += 1
    return count
print(task22_string_length("mark"))


# 23
def task23_grade_student(score):
    """
    Task 23:
    Write a function that accepts a score (0–100)
    and returns the grade based on this scale:
    A: 70–100
    B: 60–69
    C: 50–59
    D: 40–49
    E: 30–39
    F: 0–29
    """
    if score < 0 or score > 100:
        return "Invalid Score"
    if 70 <= score <= 100:
        return "A"
    elif 60 <= score <= 69:
        return "B"
    elif 50 <= score <= 59:
        return "C"
    elif 40 <= score <= 49:
        return "D"
    elif 30 <= score <= 39:
        return "E"
    else:
        return "F"
    
total = task23_grade_student(90)
print(total)


# 24
def task24_swap_values(a, b):
    """
    Task 24:
    Write a function that accepts two values
    and returns them swapped.
    Example: swap_values(3, 7) → (7, 3)
    """
    swap = b,a
    return swap
print(task24_swap_values(2,3))


# 25
counter = 0
def task25_scope_counter():
    """
    Task 25:
    Create a counter function that uses a global variable.
    Each time the function is called, it should increase
    the counter by 1 and print the current count.
    This demonstrates modifying global variables inside functions.
    """
    global counter
    counter += 1
    print(counter)
task25_scope_counter()



# ================================
# ADDITIONAL 25 FUNCTION TASKS
# ================================

# 26
def task26_calculate_bmi(weight, height):
    """
    Task 26:
    Write a function that accepts weight (kg) and height (m),
    and returns the Body Mass Index (BMI).
    Formula: BMI = weight / (height^2)
    Round the result to 2 decimal places.
    """
    if height <= 0:
        return None
    bmi = weight / (height **2 )
    return round(bmi)
total = task26_calculate_bmi(2,5)
print(total)


# 27
def task27_discounted_price(price, discount_percent):
    """
    Task 27:
    Write a function that accepts an item's price and discount percentage,
    and returns the final price after discount.
    Example: discounted_price(1000, 20) → 800
    """
    discount = (discount_percent / 100) * price
    fee_to_pay =  price - discount_percent
    return round(fee_to_pay)
total = task27_discounted_price(1000, 20)
print(total)


# 28
def task28_movie_ticket_price(age):
    """
    Task 28:
    Write a function that determines ticket price based on age:
    - Age < 12: 500
    - 12 <= Age < 18: 700
    - 18 <= Age < 60: 1000
    - Age >= 60: 600
    Return the ticket price.
    """
    if age < 12:
        return 500
    elif age < 18:
        return 700
    elif age < 60:
        return 1000
    else:
        return 600
total = task28_movie_ticket_price(8)
print(total)

# 29
def task29_shopping_total(prices):
    """
    Task 29:
    Write a function that accepts a list of item prices
    and returns the total cost of all items.
    """
    total = 0
    for price in prices:
        total += price
    return total
total = task29_shopping_total([2,3,4,6,7,8,10])
print(total)


# 30
def task30_convert_to_seconds(hours, minutes, seconds):
    """
    Task 30:
    Write a function that accepts hours, minutes, and seconds
    and converts the entire time to total seconds.
    Example: 1h 1m 1s → 3661 seconds
    """
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    return total_seconds
total = task30_convert_to_seconds(1,1,1)
print(total)

# 31
def task31_find_median(numbers):
    """
    Task 31:
    Write a function that accepts a list of numbers
    and returns the median value.
    (Hint: Sort the list first, then handle odd/even length cases.)
    """
    if not numbers:
        return None
    nums = sorted(numbers)
    n = len(nums)
    mid = n // 2
    if n % 2 == 1:
        return nums[mid]
    else:
        return (nums[mid - 1] + nums[mid]) / 2


# 32
def task32_parking_fee(hours):
    """
    Task 32:
    Write a function that calculates parking fees:
    - First 2 hours: 200 Naira flat
    - Every additional hour: 100 Naira
    Example: parking_fee(5) → 200 + 3*100 = 500
    """
    if hours <= 0:
        return 0
    if hours <= 2:
        return 200
    return 200 + (hours - 2) * 100
total = task32_parking_fee(5)
print(total)

# 33
def task33_word_count(sentence):
    """
    Task 33:
    Write a function that accepts a sentence
    and returns the number of words in it.
    Example: "I love Python" → 3
    """
    words = sentence.split()
    return len(words)
total = task33_word_count("I am a happy boy")
print(total)

# 34
def task34_capitalize_names(names):
    """
    Task 34:
    Write a function that accepts a list of names in lowercase
    and returns a new list with each name capitalized.
    Example: ["john", "mary"] → ["John", "Mary"]
    """

    return [name.capitalize() for name in names]
total = task34_capitalize_names(["nary", "john"])
print(total)


# 35
def task35_student_pass_fail(score):
    """
    Task 35:
    Write a function that accepts a student's score
    and returns "Pass" if score >= 50, otherwise "Fail".
    """
    if score >= 50:
        return "Pass"
    else:
        return "Fail"
total = task35_student_pass_fail(60)
print(total)


# 36
def task36_calculate_fine(days_late):
    """
    Task 36:
    Write a function that calculates library book fine:
    - First 5 days: 20 per day
    - 6–10 days: 50 per day
    - Beyond 10 days: 100 per day
    Example: calculate_fine(7) → 5*20 + 2*50 = 200
    """
    if days_late <= 0:
        return 0
    fine = 0
    if days_late <= 5:
        fine += days_late * 20
    elif days_late <= 10:
        fine += 5 * 20
        fine += (days_late - 5) * 50
    else:
        fine += 5 * 20
        fine += 5 * 50
        fine += (days_late - 10) * 100
    return fine
total = task36_calculate_fine(7)
print(total)

# 37
def task37_convert_currency(amount, rate):
    """
    Task 37:
    Write a function that converts money from one currency to another
    using a given conversion rate.
    Example: convert_currency(100, 1500) → 150000
    """
    convert = amount * rate
    return convert
total = task37_convert_currency(100,1500)
print(total)


# 38
def task38_gas_station_bill(liters, price_per_liter):
    """
    Task 38:
    Write a function that accepts the number of liters purchased
    and the price per liter, then returns the total cost.
    """
    total = liters * price_per_liter
    return total
total = task38_gas_station_bill(6,1500)
print(total)


# 39
def task39_is_leap_year(year):
    """
    Task 39:
    Write a function that accepts a year and returns True if it is a leap year,
    otherwise False.
    Rule: Year divisible by 4 → leap year, but divisible by 100 → not leap,
    unless divisible by 400.
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0
total = task39_is_leap_year(2020)


# 40
def task40_password_strength(password):
    """
    Task 40:
    Write a function that checks password strength:
    - Length >= 8
    - Contains at least one digit
    - Contains at least one uppercase letter
    Return "Strong" if all conditions are met, otherwise "Weak".
    """
    length = len(password)

    if length <= 6:
        return "weak"
    if length >= 6 and length <= 10:
        return "medium"
    has_letter = any(c.isalpha() for c in password)
    has_digit = any(c.isdigit() for c in password)
    
    if has_letter and has_digit:
        return "strong"
    else:
        return "medium"
total = task40_password_strength("Methysekag1")
print(total)

# 41
def task41_shirt_order(quantity, price_per_shirt, discount_threshold=10, discount_rate=0.1):
    """
    Task 41:
    Write a function to calculate the total price of a shirt order.
    - If quantity >= discount_threshold, apply discount_rate.
    Example: shirt_order(12, 2000) → discounted price
    """
    pass


# 42
def task42_find_mode(numbers):
    """
    Task 42:
    Write a function that finds the mode (most frequent number) in a list.
    If there are multiple modes, return any one of them.
    """
    pass


# 43
def task43_student_average(scores):
    """
    Task 43:
    Write a function that accepts a dictionary of subject:score
    and returns the student's average score.
    Example: {"math": 80, "english": 70} → 75.0
    """
    pass


# 44
def task44_calculate_age(current_year, birth_year):
    """
    Task 44:
    Write a function that accepts current year and birth year,
    and returns the age.
    Example: calculate_age(2025, 2000) → 25
    """
    pass


# 45
def task45_salary_after_tax(salary, tax_rate=0.15):
    """
    Task 45:
    Write a function that calculates net salary after deducting tax.
    Example: salary_after_tax(100000) → 85000
    """
    pass


# 46
def task46_water_bill(units):
    """
    Task 46:
    Write a function to calculate water bill based on units:
    - First 30 units → 50 per unit
    - Next 20 units → 75 per unit
    - Beyond 50 units → 100 per unit
    """
    pass


# 47
def task47_find_longest_word(sentence):
    """
    Task 47:
    Write a function that accepts a sentence
    and returns the longest word in it.
    Example: "I love programming" → "programming"
    """
    pass


# 48
def task48_banking_withdraw(balance, withdraw_amount):
    """
    Task 48:
    Write a function to simulate ATM withdrawal.
    - If withdraw_amount <= balance, return new balance
    - Otherwise return "Insufficient funds"
    """
    pass


# 49
def task49_calculate_grade_point(score):
    """
    Task 49:
    Write a function that converts score (0–100) into grade points:
    - 70–100 → 5
    - 60–69 → 4
    - 50–59 → 3
    - 45–49 → 2
    - 40–44 → 1
    - <40 → 0
    """
    pass


# 50
def task50_weather_advice(temperature, raining):
    """
    Task 50:
    Write a function that gives advice based on weather:
    - If raining → "Take an umbrella"
    - Else if temperature > 30 → "Wear light clothes"
    - Else if temperature < 15 → "Wear a jacket"
    - Else → "Weather is fine"
    """
    pass
