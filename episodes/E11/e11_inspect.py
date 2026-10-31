# %%
import pandas as pd

students = pd.read_csv("students.csv")
print(students.shape)
# %%
print(students.head())
# %%
print(students.tail(3))
# %%
students.info()
# %%
print(students.isna().sum())
# %%
print(students.isna().sum().sum())
print(students.isna().any(axis=1).sum())
# %%
print(students.duplicated().sum())
print(students["student_id"].nunique())
# %%
dups = students[students.duplicated(keep=False)]
print(dups[["student_id", "department", "exam_score"]])
# %%
print(students.describe().round(1).T[["count", "mean", "min", "50%", "max"]])
# %%
print(students["department"].value_counts())
print(students["passed"].value_counts(normalize=True).round(3))
# %%
print(students["exam_score"].mean().round(2))
print(students["study_hours_per_week"].mean().round(2))
