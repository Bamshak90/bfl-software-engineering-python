# for keyword and variable initialization iterable:
#  body of the code


student = {
    "results": {
        "maths": "a",
        "engs": "b"
    }
}

numbers = [1,2,3,4,5]

for number in numbers:
    print(number)

for grades,results in student["results"].items():
    print(f"{grades:<20}: {results}")

for i in range(1, 10):
    print(f"Number {i}")


names = ["Tom", "Jerry", "mimi", "Val", "John"]

for name in names:
    print(name)

for name in range(len(names)):
    print(name)

for i in range(0,len(names),2):
    print(names[i])



vip = ["Tom", "Jerry", "mimi", "Val", "John"]

for names in vip:
    name= input("enter your name: ").capitalize()
    if name in vip:
        print(f"your are a vip {name}")
        break
    else:
        print(f"you are a regular {name}")
        break


# multiplication table with for loop
#
for i in range(100):
    print(f"{i}*{i} = ", i*i)


students = {
    "SOOL1": {"name":"mark", "age": 12,"score": "34"},
    "SOOL2": {"name":"mark", "age": 12,"score": "34"}

}

for student in students:
    print(students)
