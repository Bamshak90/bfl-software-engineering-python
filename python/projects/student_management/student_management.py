import json
import time

print('''
=========================================
Welcome to the student management section
=========================================
''')



DB_FILENAME = "student_db.json"

def save_student(student):
  with open( DB_FILENAME, "w") as file:
    json.dump(student, file, indent= 4)


def load_student():
  try:
    with open(DB_FILENAME, "r") as file:
      return json.load(file) 
  except FileNotFoundError:
    return {}


  
    
def add_student(student, student_id, name, age, score,):
  if student_id in student:
    print(f"Student with ID {student_id} already exists.")
  else:
    student[student_id] = {"name": name, "age": age, "score": score}
    print("student added successfully")


def update_student(student, student_id, name = None, age = None, score = None):
  if student_id in student:
    if name is not None:
      student[student_id]["name"] = name
    if age is not None:
      student[student_id]["name"] = age
    if score is not None:
      student[student_id]["score"] = score
    save_student(student)
    print(f"student id {student_id} updated")
  else:
    print(f"student id {student_id} does not exist")

def delete_student(student, student_id):
  if student_id in student:
    del student[student_id]
    print(f"student id {student_id} successfully deleted.")
    save_student(student)
  else:
    print(f"Student id {student_id} does not exist.")

def display_students(students):
    if not students:
        print("No students in the system yet.")
    else:
      for sid, info in students.items():
        print(f"{sid} -> Name: {info['name']}, Age: {info['age']}, Score: {info['score']}")


student = load_student()

def start():
  while True:
        print("\n==== Student Management ====")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Display Students")
        print("0. Exit")

        user_choice = int(input("Enter choice: "))

        if user_choice == 1:
          student_id = input("Enter id: ")
          name = input("Enter name: ")
          age = int(input("Enter age: "))
          score = int(input("Enter score: "))
          add_student(student, student_id, name, age, score)
          save_student(student)

        elif user_choice == 2:
          student_id = input("Enter id: ")
          name = input("Enter name: ")
          age = int(input("Enter age: "))
          score = int(input("Enter score: "))
          update_student(student, student_id, name, age, score)
          save_student(student)

        elif user_choice == 3:
          student_id = input("Enter student id to delete: ")
          delete_student(student, student_id)
          save_student(student)

        elif user_choice == 4:
          display_students(student)
        
        elif user_choice == 0:
          print("Exiting...")
          break
        else:
          print("Invalid choice!")



start()