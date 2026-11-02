# %%
import pandas as pd

students = pd.read_csv("students_clean.csv")
print(students.shape)
# %%
hours = students["study_hours_per_week"]
students["study_per_day"] = (hours / 7).round(1)
cols = ["student_id", "study_hours_per_week", "study_per_day"]
print(students[cols].head(3))
# %%
students["high_attendance"] = students["attendance_pct"] >= 90
print(students["high_attendance"].sum())
# %%
faculty = {"CS": "Computing", "Engineering": "Engineering",
           "Business": "Commerce", "Arts": "Arts",
           "Medicine": "Medicine"}
students["faculty"] = students["department"].map(faculty)
print(students["faculty"].value_counts())
# %%
students["dept_upper"] = students["department"].str.upper()
students["id_number"] = students["student_id"].str[1:].astype(int)
cols = ["student_id", "id_number", "dept_upper"]
print(students[cols].head(3))
print(students["department"].str.contains("ing").sum())
# %%
submissions = pd.DataFrame({
    "student_id": ["S0001", "S0002", "S0003", "S0004"],
    "submitted": ["2026-10-14", "2026-10-17",
                  "2026-10-15", "2026-10-20"]})
submissions["submitted"] = pd.to_datetime(submissions["submitted"])
print(submissions["submitted"].dtype)
# %%
deadline = pd.Timestamp("2026-10-15")
submissions["weekday"] = submissions["submitted"].dt.day_name()
late = submissions["submitted"] - deadline
submissions["days_late"] = late.dt.days
print(submissions)
print((submissions["days_late"] > 0).sum())
