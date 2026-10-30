import pandas as pd

df = pd.read_csv("students.csv").drop_duplicates()

# average exam score by weekly study hours
groups = pd.cut(df["study_hours_per_week"], [0, 5, 10, 15, 20, 40], right=False)
print(df.groupby(groups, observed=True)["exam_score"].mean().round(1))

# average exam score with and without a part-time job
print(df.groupby("part_time_job")["exam_score"].mean().round(1))
