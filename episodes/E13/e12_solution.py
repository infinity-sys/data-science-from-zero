# %%
import pandas as pd

students = pd.read_csv("students.csv")
mask = ((students["department"] == "CS")
        & (students["year"] == 4)
        & (students["attendance_pct"] > 90))
picked = students[mask]
print(len(picked))
print(picked["exam_score"].mean().round(2))
# %%
print(picked[["student_id", "attendance_pct", "exam_score"]])
