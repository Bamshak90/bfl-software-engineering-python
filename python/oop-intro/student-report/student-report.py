'''
A student should have:

Name

ID (or roll number)

Subjects with marks (like Math → 80, English → 70, etc.)

The class should allow:

Adding a new subject with marks.

Updating marks for a subject.

Calculating the average (or total).

Getting the grade (e.g., A, B, C, F based on score).

Displaying the full report card.

'''


class Student:
  def __init__(self, name, student_id):
    self.name = name
    self.student_id = student_id
    self.subject = {}
  
  def add_subject(self, subject, marks):
     if subject not in self.subject:
       self.subject[subject] = marks
     else:
       print("subject already exist")

  def update_marks(self, subject, marks):
    if subject in self.subject:
      self.subject[subject] = marks
    else:
      print("This subject does not exist")

  def calculate_average(self):
    if  len(self.subject) == 0:
      return 0
    else:
      return sum(self.subject.values()) / len(self.subject)

  def display_report(self):
    for subject, marks in self.subject.items():
      print(f"{subject:>} {marks}")

  def get_grade(self):
    avg = self.calculate_average()
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


student1 = Student("Mark", "S101")

student1.add_subject("Math", 85)
student1.add_subject("English", 70)
student1.add_subject("Science", 92)
student1.add_subject("History", 65)

student1.update_marks("English", 80)   
student1.update_marks("Art", 50)     


print(student1.calculate_average())    


print(student1.get_grade())          

student1.display_report()