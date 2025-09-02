"""
Attendance Register

Task:
- Track attendance of students.
- Use a dictionary { "student_id": {"name": str, "present_days": list, "absent_days": list} }
- Functions to mark attendance, check history, and get reports.
- Use your head/logic to mark multiple students at once.
- Use **kwargs for flexible reporting (e.g., only_present=True).

// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Student class with mark_present() and mark_absent().
- AttendanceRegister class that manages records.
"""

import datetime

attendance = {}

def register_student(student_id, name):
    """Register a student in the system."""
    if student_id in attendance:
        return f"student ID {student_id} is already a registered ID"
    else:
        attendance[student_id] = {
            "name": name,
            "present_days": [],
            "absent_days" : []
        }
        print(attendance)

register_student("S1", "Mark")
register_student("S2", "Nan")
register_student("S3", "MP")

def mark_present(student_ids):
    """Mark multiple students as present for today."""
    today = str(datetime.date.today())
    # implement logic
    pass

def mark_absent(student_ids):
    """Mark multiple students as absent for today."""
    today = str(datetime.date.today())
    #implement logic
    for id_ in student_ids:
        if id_ in attendance:
            if today not in attendance[id_]["present_days"]:
                attendance[id_]["present_days"].append(today)

            if today in attendance[id_]["absent_days"]:
                attendance[id_]["absent_days"].remove(today)
                print(attendance[id_])
        else:
            print(f"Student ID {id_} not found!")
mark_present(["S1", "S2"])


def get_report(**kwargs):
    """Generate attendance report with optional filters."""
    report = {}
    today = str(datetime.date.today())
    
    for id_, data in attendance.items():
        inside = True

        if kwargs.get("student_id") and kwargs["student_id"] != id_:
            inside = False

        if kwargs.get("only_present"):
            inside = today in data["present_days"]

        elif kwargs.get("only_absent"):
            inside = today in data["absent_days"]

        if inside:
            report[id_] = data
    
    return report
print(get_report())
print(get_report(only_present = True))
print(get_report(only_absent = False))
print(get_report(student_id = "S3"))
