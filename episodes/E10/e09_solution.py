# %%
import numpy as np
import pandas as pd

students = pd.read_csv("students.csv").head(5)
hours = students["study_hours_per_week"].to_numpy()
exam = students["exam_score"].to_numpy()
print(hours)
print(exam)
# %%
# by hand: multiply the pairs, then add
print([float(round(h * e, 1)) for h, e in zip(hours, exam)])
print(np.dot(hours, exam))
# %%
print(0.1 + 0.2)
print(round(0.1 + 0.2, 2))
print(round(np.dot(hours, exam), 2))
# %%
att = students["attendance_pct"].to_numpy()
M = np.array([hours, att]).T      # 5 x 2: [hours, attendance]
print(M.shape)
print(M @ np.array([2, 0.5]))
