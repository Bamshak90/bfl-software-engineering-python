# class Dog:
#   def __init__(self, name):
#     self.name = name
#     print(name)

#   def bark(self):
#     print("bark")

# d = Dog("Mark")

class Person:
  def __init__(self,name, age):
    self.name = name 
    self.age = age

  def sing(self):
    print(f"Hi my name is {self.name} and i am {self.age} years old")

p1 = Person("Mark", 23)
p2 = Person("mp",60)
p1.sing()
p2.sing()

print(p1.name)

