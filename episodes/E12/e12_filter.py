# %%
import pandas as pd

students = pd.read_csv("students.csv")
print(students["department"].head(3))
# %%
print(students[["student_id", "department", "exam_score"]].head(3))
# %%
print(students.loc[0:2, ["student_id", "exam_score"]])
print(students.iloc[0:2, [0, 8]])
# %%
is_cs = students["department"] == "CS"
print(is_cs.head(4))
print(is_cs.sum())
# %%
cs = students[is_cs]
print(cs.shape)
print(cs["department"].unique())
# %%
both = students[(students["department"] == "CS") & (students["passed"] == "yes")]
either = students[(students["department"] == "CS") | (students["passed"] == "yes")]
print(len(both), len(either))
# %%
small = students[students["department"].isin(["Arts", "Medicine"])]
print(len(small))
# %%
short_sleep = students["sleep_hours"] < 6
print(short_sleep.sum())
print(students["sleep_hours"].isna().sum())
# %%
print(students.query("department == 'CS' and passed == 'yes'").shape)
# %%
print(students["exam_score"].mean().round(2))
print(students.loc[is_cs, "exam_score"].mean().round(2))
print(students.loc[short_sleep, "exam_score"].mean().round(2))
# %%
top = cs.sort_values("exam_score", ascending=False)
print(top[["student_id", "year", "exam_score"]].head(3))
