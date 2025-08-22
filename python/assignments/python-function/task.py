'''
Assignment Question 
1. Write a function check_even_odd(n) that takes an integer n and returns: "Even" if the number is even, "Odd" if the number is odd. Function 

2. with Default Arguments & Loops Write a function count_vowels(text, vowels="aeiou") that counts how many vowels appear in a given text. Example: count_vowels("Python is fun") should return 3. 

3. Function with Conditions and List Write a function count_even(numbers) that counts how many even numbers are in a list. Example: count_even([1, 2, 3, 4, 6]) →3

4. Write a function triangle_area(base, height) that calculates the area of a triangle using the formula: Area=1/2×base×height Example: triangle_area(10, 5) → 25.
0 
5. Write a function called check_password_strength that takes a password string and returns "Weak", "Medium", or "Strong" based on these criteria: Weak (less than 6 characters), Medium (6-10 characters), Strong (more than 10 characters and contains both letters and numbers).
'''


# task 1 solution 

def check_even_odd(n: int):
    if n % 2 == 0:
        print(f"{n} is even")
        return "Even"
        
    else:
        print(f"{n} is odd")
        return "Odd"
    
print(check_even_odd(9))


# task 2 solution

def count_vowels(text: str, vowels: str = "aeiou"):
    count = 0
    for character in text:
        if character.lower() in vowels:
            count += 1
    return count

print(count_vowels("Python is fun"))        
print(count_vowels("HELLO World"))          
print(count_vowels("gym", vowels="aeiouy")) 


# task 3 solution

def count_even(numbers: list[int]):

    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += 1
    return total

print(count_even([1,2,3,4,5,6,7,8,9,10,22,11,20,32,34,56,78,65]))


# task 4 solution

def triangle_area(base: float, height: float):
    area = 0.5 * base * height
    return float(area)

print(triangle_area(2,20))


# task 5 solution

def check_password_strength(password: str):
    length = len(password)

    if length < 6:
        return "Weak"

    if length >= 6 and length <= 10:
        return "Medium"

    has_letter = any(c.isalpha() for c in password)
    has_digit = any(c.isdigit() for c in password)

    if has_letter and has_digit:
        return "Strong"
    else:
        return "Medium"
    
user_password = input("Enter a password to check: ")
strength = check_password_strength(user_password)
print(f"Your password is {strength}")
