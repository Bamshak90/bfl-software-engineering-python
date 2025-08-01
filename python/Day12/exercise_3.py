grade = [("Godiya", "A"), ("Tanko", "B"), ("Panshak", "C"), ("Bella", "B" )]

scores = dict(grade)
print(grade)

print(scores["Godiya"])

gradings = {
    grade[0][0]: grade[0][1],  
    grade[1][0]: grade[1][1]
}

print(gradings)
