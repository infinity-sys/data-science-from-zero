# %%
import pandas as pd

students = pd.read_csv("students_clean.csv")
students["dept_code"] = students["department"].str[:3].str.upper()
cols = ["student_id", "department", "dept_code"]
print(students[cols].head(3))
# %%
hours = students["study_hours_per_week"]
students["study_per_day"] = (hours / 7).round(1)
top = students.sort_values("study_per_day", ascending=False)
cols = ["student_id", "study_hours_per_week", "study_per_day"]
print(top[cols].head(1))
# %%
new_year = pd.to_datetime("2027-01-01")
today = pd.to_datetime("2026-11-14")
print(new_year.day_name())
print((new_year - today).days)
