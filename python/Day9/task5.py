# Your are helping your teacher arrange student in a classroom. The classroom starts empty. Follow the instructions carefully to build the arrangement.
#
# Task for students:
#
# 1. Starts with an empty list called desks.
#
# 2. Ask the user to enter the name of the three students, one by one, and place them in the list.
# 3. A student sitting in the second seat wants to be replaced, Ask for the new name and replace the old one.
# 4. Another student walks in and wants to sit between the first and second students. Add them to the correct position.
#
# Print the final list showing how the desks are arrange


desk = []

desk.append(input("Enter first name of student: "))
desk.append(input("Enter second name of student: "))
desk.append(input("Enter third student name of student: "))


print(desk)

new_student= input("Enter the name to replace student 2: ")
desk[1] = new_student
print(desk)

last_student = input("Enter the name: ")

desk.insert(1, last_student)

print(desk)
