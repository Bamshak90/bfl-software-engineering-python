#user_grade = int(input("Enter your score: "))
user_grade = int(input("Enter your score: "))
def grade_student(score):
    if score >= 70 and score <= 100:
        print("A")
    elif score >= 59 and score <= 69:
        print("B")
    elif score >= 49 and score <= 58:
        print("C")
    elif score >= 44.9 and score <= 48:
        print("D")
    elif score >= 40 and score <= 44:
        print("E")
    elif score >= 0 and score <= 39:
        print("F")
    else:
        print("Invalid input")


grade_student(user_grade)
