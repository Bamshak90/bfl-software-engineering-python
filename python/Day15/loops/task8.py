'''

students = {
    "name": "",
    "gender": "",
    "score": ""
}

count = 3
records = []

for student in range(count):
    name = input("Enter your name: ")
    students["name"] = name
    gender = input("Enter your gender: ")
    students["gender"] = gender
    score = input("Enter your score: ")
    students["score"] = score
    records.append(students)
    count -= 1

    

print(records)

'''

student_list = []

for student in range(3):
    student_name = input("Enter your name: ")
    student_gender = input("Enter your gender: ")
    student_score = input("Enter your socre: ")

    student_record = {
        "name": student_name,
        "gender": student_gender,
        "socre": student_score
    }
    student_list.append(student_record)
print(student_list)

