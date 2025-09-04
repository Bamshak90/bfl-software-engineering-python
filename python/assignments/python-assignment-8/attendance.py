"""
TASK: Create an AttendanceRegister class.

Requirements:
1. The class should allow marking a student as present or absent.
2. Store attendance records in a dictionary where the student's name is the key.
3. Provide a method to check if a student was present or absent.
4. Provide a method to display the full register.

Example Usage:
    register = AttendanceRegister()
    register.mark_present("John")
    register.mark_absent("Mary")
    print(register.get_status("John"))   # "Present"
    print(register.show_register())      # {"John": "Present", "Mary": "Absent"}
"""


class AttendanceRegister:
    def __init__(self):
        self.attendance = {} 

    def register_student(self, name):
        if name in self.attendance:
            print(f"{name} is already registered")
        else:
            self.attendance[name] = "Not Marked"
            print(f"{name} registered successfully")
    
    def mark_present(self, name):
        if name in self.attendance:
            self.attendance[name] = "Present"
            print(f"{name} marked as Present")
        else:
            print(f"{name} is not registered")
    
    def mark_absent(self, name):
        if name in self.attendance:
            self.attendance[name] = "Absent"
            print(f"{name} marked as Absent")
        else:
            print(f"{name} is not registered")
    
    def get_status(self, name):
        return self.attendance.get(name, f"{name} is not registered")
    
    def show_register(self):
        return self.attendance

register = AttendanceRegister()
register.register_student("Mark")
register.register_student("Mary")
register.register_student("mp")

register.mark_present("Mark")
register.mark_absent("Mary")

print(register.get_status("Mark"))  
print(register.get_status("mp"))   
print(register.get_status("Mary")) 
print(register.show_register())      