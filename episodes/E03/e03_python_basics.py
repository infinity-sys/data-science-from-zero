# %%
department = "CS"
year = 2
exam_score = 63
print(department, year, exam_score)
# %%
exam_score = exam_score + 5
exam_score
# %%
student_id = "S0001"    # str
year = 2                # int
study_hours = 17.2      # float
passed = True           # bool
# %%
print(type(student_id))
print(type(year))
print(type(study_hours))
print(type(passed))
# %%
exam_score = 63
exam_score >= 50
# %%
print(type(63))
print(type("63"))
# %%
total = 78 + 85 + 91
average = total / 3
print(total)
print(average)
# %%
round(average, 1)
# %%
round(average)
# %%
print(f"Average score: {round(average, 1)}")
# %%
scores = [72, 85, 90, 64, 88, 95]
# %%
scores[0]
# %%
scores[2]
# %%
scores[-1]
# %%
scores[-2]
# %%
scores[1:4]
# %%
scores[:3]
# %%
len(scores)
# %%
sum(scores)
# %%
min(scores)
# %%
max(scores)
# %%
round(sum(scores) / len(scores), 1)
# %%
scores.append(79)
scores
# %%
sorted(scores)
# %%
student = {
    "id": "S0001",
    "department": "CS",
    "year": 2,
    "exam_score": 63,
}
student["department"]
# %%
student["year"] = 3          # update a value
student["passed"] = True     # add a new key
print(student)
# %%
print(student.keys())
print(student.values())
print(student.items())
# %%
students = [
    {"id": "S0001", "department": "CS", "exam_score": 63},
    {"id": "S0002", "department": "Business", "exam_score": 34},
    {"id": "S0003", "department": "Engineering", "exam_score": 69},
]
len(students)
# %%
students[1]["department"]
# %%
students[2]["exam_score"]
# %%
import pandas as pd
pd.DataFrame(students)
# %%
scores[10]
# %%
student["name"]
# %%
"Score: " + 63
# %%
scores[-1]
# %%
print(student.get("name"))
# %%
"Score: " + str(63)
# %%
f"Score: {63}"
