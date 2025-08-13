students = {
    "John": 60,
    "Mimi": 50,
    "Sarah": 30
}
'''
student = 0

while student < len(students):
    for student_name, student_score in students.keys():
        print(student_name, student_score)
        student += 1
'''

student_keys = list(students.keys())
student_values = list(students.values())

count = 0

while count < len(student_keys):
    print(student_values[count], student_keys[count])
    count += 1
    
