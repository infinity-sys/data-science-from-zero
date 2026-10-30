"""Student-performance dataset for "Data Science: From Zero to Hero" (Infinity Systems).

Generated once with a fixed seed and reused across the course. The numbers are
synthetic but the relationships are realistic and a little noisy:
  - more study hours, higher attendance, more assignments and enough sleep -> higher exam score
  - a part-time job means fewer study hours, a bit less sleep and lower attendance
  - Medicine students study the most, Arts and Business the least (on average)
  - very short sleep hurts the score
Deliberate problems for the cleaning episodes (E12):
  - a few missing values (NaN) in study_hours_per_week, attendance_pct and sleep_hours
  - 3 exact duplicate rows (so 500 students give 503 rows)

Usage: python3 make_students.py            -> writes students.csv next to this script
Needs: numpy, pandas
"""
import os

import numpy as np
import pandas as pd

SEED = 2026
N = 500
rng = np.random.default_rng(SEED)

# who the students are
departments = np.array(["CS", "Engineering", "Business", "Medicine", "Arts"])
dept = rng.choice(departments, size=N, p=[0.30, 0.22, 0.20, 0.13, 0.15])
year = rng.integers(1, 5, size=N)                                  # 1..4
job = rng.random(N) < (0.15 + 0.07 * (year - 1))                   # seniors work more often

# study habits
base_hours = pd.Series(dept).map({"CS": 13, "Engineering": 14, "Business": 10, "Medicine": 18, "Arts": 9}).to_numpy()
study = base_hours + rng.normal(0, 5, N) - 3.5 * job
study = np.clip(study, 0.5, 35).round(1)

attendance = 58 + 1.3 * study + rng.normal(0, 9, N) - 6 * job
attendance = np.clip(attendance, 25, 100).round(1)

sleep = 7.4 - 0.03 * study - 0.7 * job + rng.normal(0, 0.8, N)
sleep = np.clip(sleep, 4, 10).round(1)

p_submit = np.clip(0.30 + 0.022 * study + 0.004 * (attendance - 70), 0.05, 0.98)
assignments = rng.binomial(10, p_submit)                           # out of 10

# the exam
score = (33 + 1.2 * study + 0.22 * (attendance - 60) + 2.0 * assignments
         + 3.0 * (sleep - 7) - 5.0 * (sleep < 5.5) + rng.normal(0, 8.5, N))
score = np.clip(score, 0, 100).round().astype(int)
passed = np.where(score >= 50, "yes", "no")

df = pd.DataFrame({
    "student_id": [f"S{k:04d}" for k in range(1, N + 1)],
    "department": dept,
    "year": year,
    "study_hours_per_week": study,
    "attendance_pct": attendance,
    "sleep_hours": sleep,
    "assignments_submitted": assignments,
    "part_time_job": np.where(job, "yes", "no"),
    "exam_score": score,
    "passed": passed,
})

# a few missing values (never in the first rows, so the first look stays readable)
for col, n in [("study_hours_per_week", 6), ("attendance_pct", 9), ("sleep_hours", 12)]:
    idx = rng.choice(np.arange(10, N), size=n, replace=False)
    df.loc[idx, col] = np.nan

# a couple of exact duplicates, inserted right after the original row
dups = np.sort(rng.choice(np.arange(10, N), size=3, replace=False))
parts, last = [], 0
for d in dups:
    parts += [df.iloc[last:d + 1], df.iloc[[d]]]
    last = d + 1
parts.append(df.iloc[last:])
out = pd.concat(parts, ignore_index=True)

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.csv")
out.to_csv(path, index=False)
print("wrote", path, out.shape)
