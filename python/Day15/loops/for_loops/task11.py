

students = {
    "S001": {"name": "John Doe", "age": 20, "score": 85},
    "S002": {"name": "Jane Smith", "age": 19, "score": 92},
    "S003": {"name": "Michael Brown", "age": 21, "score": 78}
}

target_score = int(input("Enter score to search: "))

found = False
for student_id, info in students.items():
    if info["score"] == target_score and info["score"] > 80:
        print(f"{info['name']}, {info['score']}")
        found = True

if not found:
    print("No students match the criteria.")

