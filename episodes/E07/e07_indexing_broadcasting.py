# %%
import numpy as np

scores = np.array([63, 34, 69, 57, 64, 65, 55, 61, 58, 87])
print(scores[0], scores[1], scores[-1])
# %%
print(scores[2:5])    # positions 2, 3, 4
print(scores[:3])     # the first three
print(scores[-3:])    # the last three
print(scores[::2])    # every second one
# %%
exams = np.array([[78, 85, 92],    # Mona
                  [45, 52, 68],    # Omar
                  [91, 88, 97],    # Sara
                  [60, 47, 73],    # Karim
                  [83, 76, 84],    # Laila
                  [63, 42, 54]])   # Youssef
exams.shape
# %%
print(exams[1, 2])    # row 1, column 2
print(exams[1])       # row 1: Omar
print(exams[:, 2])    # column 2: Exam 3
# %%
exams[0:2, 1:3]       # rows 0-1, columns 1-2
# %%
exams[-2:, :2]        # last 2 rows, first 2 columns
# %%
nums = np.arange(12)
nums
# %%
nums.reshape(3, 4)
# %%
nums.reshape(4, 3)
# %%
nums.reshape(5, 3)
# %%
exams >= 90
# %%
exams[exams >= 90]
# %%
exams[exams[:, 2] >= 80]    # 80+ in Exam 3
# %%
exams[[0, 2, 4]]            # rows 0, 2 and 4
# %%
exams[:, [0, 2]]            # Exam 1 and Exam 3
# %%
a = np.array([10, 20, 30, 40, 50])
part = a[1:4]          # a slice
part[0] = 99
print(part)
print(a)
# %%
b = np.array([10, 20, 30, 40, 50])
safe = b[1:4].copy()   # a real copy
safe[0] = 99
print(safe)
print(b)
# %%
exams.mean(axis=0)     # one mean per exam
# %%
exams.mean(axis=1)     # one mean per student
# %%
exams.sum(axis=0)      # one total per exam
# %%
exams + 5
# %%
curve = np.array([5, 10, 0])          # per exam
exams + curve
# %%
extra = np.array([2, 0, 3, 1, 0, 2])  # per student
exams + extra
# %%
extra.reshape(6, 1)
# %%
exams + extra.reshape(6, 1)
# %%
centred = exams - exams.mean(axis=0)
centred
# %%
centred.mean(axis=0)
# %%
lo = exams.min(axis=0)
hi = exams.max(axis=0)
print(lo, hi)
# %%
scaled = (exams - lo) / (hi - lo)
scaled.round(2)
# %%
# columns 3, 4, 8: study hours, attendance, exam score
data = np.genfromtxt("students.csv", delimiter=",",
                     skip_header=1, usecols=(3, 4, 8))
data.shape
# %%
data[:5]
# %%
np.isnan(data).sum(axis=0)    # missing per column
# %%
heavy = data[:, 0] >= 20      # 20+ hours a week
print(heavy.sum())
print(round(data[heavy, 2].mean(), 1))
print(round(data[:, 2].mean(), 1))
