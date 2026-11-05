# %%
import pandas as pd

students = pd.read_csv("students_clean.csv")
print(students.shape)
# %%
by_year = students.groupby("year")
print(by_year["exam_score"].mean().round(1))
# %%
by_job = students.groupby("part_time_job")
print(by_job["exam_score"].mean().round(1))
print(by_job["passed"].mean().round(3))
# %%
scores = students.groupby("year")["exam_score"]
print(scores.agg(["mean", "min", "max", "count"]).round(1))
# %%
att = students.groupby("year")["attendance_pct"]
print(att.size())
print(att.count())
# %%
summary = students.groupby("part_time_job").agg(
    students=("student_id", "count"),
    mean_score=("exam_score", "mean"),
    pass_rate=("passed", "mean"))
print(summary.round(2))
# %%
two = students.groupby(["year", "part_time_job"])["exam_score"]
means = two.mean().round(1)
print(means)
