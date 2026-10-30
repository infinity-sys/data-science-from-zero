# %%
import csv

counts = {}
with open("students.csv") as f:
    for row in csv.DictReader(f):
        dept = row["department"]
        counts[dept] = counts.get(dept, 0) + 1

print(counts)
print("Total rows:", sum(counts.values()))
# %%
import json

with open("department_counts.json", "w") as f:
    json.dump(counts, f, indent=2)
