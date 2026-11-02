# %%
import pandas as pd

students = pd.read_csv("students.csv")
print(students.shape)
print(students.duplicated().sum())
# %%
print(students[students.duplicated(keep=False)][["student_id", "department", "exam_score"]])
# %%
students = students.drop_duplicates()
print(students.shape)
print(students["student_id"].is_unique)
# %%
print(students.isna().sum())
# %%
print(len(students.dropna()))
# %%
median_sleep = students["sleep_hours"].median()
print(median_sleep)
students["sleep_hours"] = students["sleep_hours"].fillna(median_sleep)
print(students["sleep_hours"].isna().sum())
# %%
print(students.dtypes)
# %%
students["passed"] = students["passed"] == "yes"
students["part_time_job"] = students["part_time_job"] == "yes"
print(students["passed"].dtype, students["passed"].sum())
print(students["passed"].mean().round(3))
# %%
students = students.reset_index(drop=True)
print(students.shape)
print(students.isna().sum().sum())
students.to_csv("students_clean.csv", index=False)
