# %%
import pandas as pd

students = pd.read_csv("students.csv")
print(students.shape)
# %%
missing = students.isna().sum()
print(missing[missing > 0])
# %%
print(students["exam_score"].mean().round(2))
