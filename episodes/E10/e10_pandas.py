# %%
import pandas as pd
import numpy as np
print(pd.__version__)
# %%
scores = pd.Series([63, 34, 78])
print(scores)
# %%
scores = pd.Series([63, 34, 78], index=["Mona", "Omar", "Sara"])
print(scores)
print(scores["Omar"])
# %%
print(scores + 5)
print(scores.mean())
print(scores.to_numpy())
# %%
print(scores[scores > 50])
# %%
quiz = pd.Series({"Sara": 9, "Mona": 7, "Ali": 10})
print(scores + quiz)
# %%
df = pd.DataFrame({
    "name": ["Mona", "Omar", "Sara", "Ali"],
    "dept": ["CS", "Business", "CS", "Engineering"],
    "hours": [17.2, 1.6, 12.5, 8.0],
    "exam": [63, 34, 78, 55],
})
print(df)
# %%
print(df.shape)
print(list(df.columns))
print(df.index)
print(df.dtypes)
# %%
print(type(df["exam"]))
print(df["exam"])
# %%
print(df[["name", "exam"]])
# %%
df["points_per_hour"] = (df["exam"] / df["hours"]).round(1)
print(df)
# %%
print(df.sort_values("exam", ascending=False))
# %%
print(df.loc[2, "name"])
print(df.iloc[0])
# %%
students = pd.read_csv("students.csv")
print(students.shape)
print(students[["student_id", "department", "study_hours_per_week", "exam_score"]].head(3))
# %%
print(students["exam_score"].mean().round(2))
print(students["department"].value_counts())
