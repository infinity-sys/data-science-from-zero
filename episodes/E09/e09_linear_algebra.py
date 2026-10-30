# %%
import csv
import numpy as np

with open("students.csv") as f:
    rows = list(csv.DictReader(f))

cols = ["study_hours_per_week", "attendance_pct", "sleep_hours",
        "assignments_submitted", "exam_score"]
s1 = np.array([float(rows[0][c]) for c in cols])   # student S0001
print(s1)
print(s1.shape)
# %%
exam = np.array([float(r["exam_score"]) for r in rows])   # a column
print(exam.shape)
print(exam[:5])
# %%
a = np.array([3, 4])      # this week: maths, programming
b = np.array([2, 1])      # next week
print(a + b)              # add, element by element
print(2 * a)              # scale: every element times 2
# %%
s2 = np.array([float(rows[1][c]) for c in cols])   # student S0002
print(s1 + s2)
print(0.5 * (s1 + s2))    # the average of the two students
# %%
qty = np.array([2, 3, 1])        # coffee, sandwich, juice
price = np.array([15, 40, 20])   # EGP each
print(qty * price)               # multiply the pairs
print(np.dot(qty, price))        # ... and add them up
# %%
x = np.array([63, 4, 72.4])   # S0001: exam, assignments, attendance
w = np.array([0.6, 3, 0.1])   # the weights of the grade formula
print(x * w)
print(np.dot(x, w))
print(x @ w)                  # @ does the same for two vectors
# %%
a = np.array([3, 4])
print(a @ np.array([4, 3]))     # almost the same way
print(a @ np.array([-4, 3]))    # at a right angle
print(a @ np.array([-3, -4]))   # the opposite direction
# %%
print(np.sqrt(a @ a))       # the square root of a · a
print(np.linalg.norm(a))    # the norm, ready-made
# %%
def cosine(u, v):
    return (u @ v) / (np.linalg.norm(u) * np.linalg.norm(v))

A = np.array([6, 2, 2])   # weekly hours: maths, coding, stats
B = np.array([3, 1, 1])   # the same mix, half the time
C = np.array([1, 6, 3])   # a different mix
print(round(cosine(A, B), 3), round(cosine(A, C), 3))
# %%
feats = ["study_hours_per_week", "attendance_pct",
         "assignments_submitted", "exam_score"]
R = np.array([[float(r[c]) if r[c] else np.nan for c in feats]
              for r in rows])
print(round(cosine(R[0], R[7]), 3), round(cosine(R[0], R[6]), 3))
# %%
Z = (R - np.nanmean(R, axis=0)) / np.nanstd(R, axis=0)
print(Z[[0, 7, 6]].round(2))     # S0001, S0008, S0007
print(round(cosine(Z[0], Z[7]), 3), round(cosine(Z[0], Z[6]), 3))
# %%
g = ["exam_score", "assignments_submitted", "attendance_pct"]
X = np.array([[float(r[c]) for c in g] for r in rows[:5]])
print(X)
print(X.shape)
# %%
print(X @ w)        # one grade per student
# %%
X_all = np.array([[float(r[c]) if r[c] else np.nan for c in g]
                  for r in rows])
grades = X_all @ w               # 503 grades in one line
print(X_all.shape, grades.shape)
print(np.isnan(grades).sum(), round(np.nanmean(grades), 1))
# %%
print(X.shape, w.shape, (X @ w).shape)
# %%
X @ np.array([0.6, 3])      # only 2 weights for 3 columns
# %%
print(X.T)
print(X.T.shape)
print(w @ X.T)              # the same five grades
# %%
W = np.array([[0.6, 0.5],    # exam
              [3,   4  ],    # assignments
              [0.1, 0.1]])   # attendance
print(X @ W)                 # 5 students x 2 formulas
print((X @ W).shape)
# %%
I = np.eye(3)
print(I)
print(I @ w)                     # w comes back unchanged
print(np.array_equal(X @ I, X))
