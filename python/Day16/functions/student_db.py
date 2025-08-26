students_db = {}
#student_id = 1

#function to start our program
def start():
    while True:
        print("""
        1. Add student
        2. Delete student
        3. Update student record
        4. Get student record
        5. Display all students
        6. Seach by Student name
        7. Count Students
        8. Filter by Age
              """)
        user_choice = int(input("Enter command : "))
        if user_choice == 1:
            add_student()#Calling the add student function to begin the add student function
        elif user_choice == 2:
            delete_student()# Caling the delete student function
        elif user_choice == 3:
            update_record()# Calling the update record function
        elif user_choice == 4:
            get_student()# Calling the get student function
        elif user_choice == 5:
            display_students()# Calling the display students function
        elif user_choice == 6:
            search_by_student_name() # calling the search name function
        elif user_choice == 7:
            count_students() # calling function to count number of student in the database
        elif user_choice == 8:
            filter_by_age() # calling function to filter by age
# Function to add student
def add_student():
    name = input("Student name : ")
    age = int(input("Age : "))
    department = input("Department : ")
    key = len(students_db) + 1
    students_db[key] = {"name": name, "age":age, "dept": department}
    print(students_db)

# function to delete student
def delete_student():
    student_id = int(input("Student ID to delete : "))
    if student_id in students_db:
        del students_db[student_id]
        print("Student with ID {student_id} deleted successfully")
        print(students_db)
    else:
        print("student not found")

# Function to update student record
def update_record():
    id_to_update = int(input("Enter ID of student to update : "))
    if id_to_update in students_db:
        update_choice = int(input("""1. Enter \"1\" to update name\n2. Enter \"2\" to update age\n3. Enter \"3\" to update department : """))
        if update_choice == 1:
            new_name = input("Enter the name of the student : ")
            students_db[id_to_update]["name"] = new_name
            print(students_db)
        elif update_choice == 2:
            new_age = input("Enter the new age of the student : ")
            students_db[id_to_update]["age"] = new_age
            print(students_db)
        if update_choice == 3:
            new_dept = input("Enter the new depart name : ")
            students_db[id_to_update]["dept"] = new_dept
            print(students_db)

# Function to get student
def get_student():
    student_to_get = int(input("Enter ID of student to get : "))
    if student_to_get in students_db:
        print(students_db[student_to_get])

# Function to display students
def display_students():
    for key, value in students_db.items():
        print(key)
        for  key, value in value.items():
            print(key, value)

# function to search by student name

def search_by_student_name():
    search_name = input("Enter Name to search: ")
    for student in students_db:
        if search_name == students_db[student]["name"]:
            #print(f"{student}, {students_db[student]["name"]}")
            for key, value in students_db.items():
                print(f"ID: {key}, Name: {students_db[student]['name']}, Age: {students_db[student]['age']}")

# function to count students  
def count_students():
    print(f"The total students in the student database is: {len(students_db)}")

# function to filter students by add

def filter_by_age():
    age_search = int(input("Enter age to search: "))
    for student in students_db:
          if age_search > students_db[student]['age']:
            print(f"ID: {student}, Name: {students_db[student]['name']}, Age: {students_db[student]['age']}")
# start program
start()
