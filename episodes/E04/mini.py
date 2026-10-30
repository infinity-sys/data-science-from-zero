# %%
# The first 10 students of students.csv
students = [
    {"id": "S0001", "department": "CS",          "score": 63},
    {"id": "S0002", "department": "Business",    "score": 34},
    {"id": "S0003", "department": "Engineering", "score": 69},
    {"id": "S0004", "department": "Engineering", "score": 57},
    {"id": "S0005", "department": "Engineering", "score": 64},
    {"id": "S0006", "department": "Medicine",    "score": 65},
    {"id": "S0007", "department": "Arts",        "score": 55},
    {"id": "S0008", "department": "CS",          "score": 61},
    {"id": "S0009", "department": "Business",    "score": 58},
    {"id": "S0010", "department": "CS",          "score": 87},
]
len(students)
# %%
def count_passes(students, pass_mark=50):
    """Count the students who reached the pass mark."""
    count = 0
    for s in students:
        if s["score"] >= pass_mark:
            count += 1
    return count

def top_student(students):
    """Return the student with the highest score."""
    best = students[0]
    for s in students:
        if s["score"] > best["score"]:
            best = s
    return best
# %%
passes = count_passes(students)
best = top_student(students)
print("Passed:", passes, "of", len(students))
print("Top student:", best["id"], best["department"], best["score"])
# %%
count_passes(students, pass_mark=60)
