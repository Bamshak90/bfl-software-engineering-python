
students = {
    "S001": {"name": "John Doe", "age": 20, "score": 85},
    "S002": {"name": "Jane Smith", "age": 19, "score": 92},
    "S003": {"name": "Michael Brown", "age": 21, "score": 78}
}

target_score = int(input("Enter score to search: "))

# TODO: loop with .items() to check each student's score
# If match → print their name
# If no matches → print message
#
for student_id, info in students.items():
    if target_score == info["score"] > 80:
        print(f"{student_id['name']}, {info['score']}")
