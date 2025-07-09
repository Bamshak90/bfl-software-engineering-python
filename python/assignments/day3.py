'''
Question 1*
1. Create two variables:
      -  A  variable  called my_age and set it to  your actual age.
     -  A  variable  called pi and assign it the value 3.14159.
*Step 2*
       Create a new variable called magic_number that is the result of:
       Your my_age multiplied by 3, then add the  pi, and finally take the modulus (%) with 7.
Step 3
        Print the value of magic_number and its type.

*Question 2*
2. Create a variable called secret_word and set it to "PythonIsAmazing".
* Print the following using slicing and indexing:*
     - The first 6 characters of the string.
     - The last 7 characters using negative indexing.
     - The middle word "Is" using slicing.
     - The string reversed using slicing.
     - Every second character in the string (using step slicing ::2).

*Question 3 *
Using the same secret_word:
   - Convert only the first word ("Python") to uppercase and print it.
   - Convert the rest of the string ("IsAmazing") to lowercase and print it.
   - Combine the uppercase and lowercase parts into one new string and print it.

'''

#Question 1
my_age = 20  # Replace with your actual age
pi = 3.14159
magic_number = (my_age * 3 + pi) % 7
print("Magic Number:", magic_number)
print("Type of magic_number:", type(magic_number))

#question 2
secret_word = "PythonIsAmazing"

print("First 6 characters:", secret_word[:6])

#negative indexing

print( secret_word[-7])
print( secret_word[-6])
print(secret_word[-5])
print(secret_word[-4])
print(secret_word[-3])
print(secret_word[-2])
print(secret_word[-1])


print("Middle word:", secret_word[6:8])

print("Reversed string:", secret_word[::-1])

print("Every second character:", secret_word[::2])

#Question 3

secret_word = "PythonIsAmazing"
first_part = secret_word[:6].upper()
second_part = secret_word[6:].lower()
combined = first_part + second_part
print("Uppercase first part:", first_part)
print("Lowercase second part:", second_part)
print("Combined string:", combined)

