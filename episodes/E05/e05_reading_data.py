# %%
import os
print(os.path.getsize("study_log.txt"))
print(list("Sat 2\n".encode("utf-8")))
# %%
os.getcwd()
# %%
sorted(os.listdir())
# %%
print(os.path.exists("students.csv"))
print(os.path.abspath("students.csv"))
# %%
with open("study_log.txt", encoding="utf-8") as f:
    text = f.read()
print(text)
# %%
text
# %%
with open("study_log.txt", encoding="utf-8") as f:
    lines = f.readlines()
lines
# %%
hours = []
for line in lines:
    day, h = line.split()
    hours.append(float(h))
print(hours)
print("Total:", sum(hours))
# %%
with open("summary.txt", "w", encoding="utf-8") as f:
    f.write("Mona's study log\n")
    f.write(f"Days: {len(hours)}\n")
    f.write(f"Total hours: {sum(hours)}\n")
# %%
with open("summary.txt", encoding="utf-8") as f:
    print(f.read())
# %%
with open("students.csv", encoding="utf-8") as f:
    lines = f.readlines()
len(lines)
# %%
import csv
with open("students.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    first = next(reader)
print(header)
print(first)
# %%
first[8], type(first[8])
# %%
row = 'Mona,CS,"Cairo, Egypt"'
print(row.split(","))
print(next(csv.reader([row])))
# %%
with open("students.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    students = list(reader)
print(len(students))
print(students[0])
# %%
total = 0
passed = 0
for s in students:
    total += int(s["exam_score"])
    if s["passed"] == "yes":
        passed += 1
print("Rows:", len(students))
print("Average score:", round(total / len(students), 1))
print("Passed:", passed)
# %%
import json
summary = {
    "file": "students.csv",
    "rows": len(students),
    "average_score": round(total / len(students), 1),
    "passed": passed,
    "duplicates_removed": False,
}
with open("summary.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2)
# %%
with open("summary.json", encoding="utf-8") as f:
    print(f.read())
# %%
print(json.dumps(summary))
# %%
with open("summary.json", encoding="utf-8") as f:
    loaded = json.load(f)
print(type(loaded))
print(loaded["rows"], type(loaded["rows"]))
print(loaded["duplicates_removed"])
# %%
with open("student.csv", encoding="utf-8") as f:
    text = f.read()
# %%
# Like older Python on Windows (cp1252 by default)
with open("names_ar.txt", encoding="cp1252") as f:
    print(f.read())
# %%
with open("names_ar.txt", encoding="utf-8") as f:
    print(f.read())
# %%
study_hours = []
for s in students:
    study_hours.append(float(s["study_hours_per_week"]))
# %%
for s in students:
    if s["study_hours_per_week"] == "":
        print(s["student_id"], s["department"])
# %%
study_hours = []
missing = 0
for s in students:
    value = s["study_hours_per_week"]
    if value == "":
        missing += 1
        continue
    study_hours.append(float(value))
print("Missing:", missing)
print("Average hours:", round(sum(study_hours) / len(study_hours), 1))
# %%
import pandas as pd
df = pd.read_csv("students.csv")
print(df.shape)
print(round(df["exam_score"].mean(), 1))
print(round(df["study_hours_per_week"].mean(), 1))
print(df["study_hours_per_week"].isna().sum())
