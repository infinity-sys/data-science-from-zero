# %%
import numpy as np
np.__version__
# %%
import time
numbers = list(range(1_000_000))   # a plain Python list
arr = np.arange(1_000_000)         # the same numbers, as an array
# %%
start = time.perf_counter()
doubled = []
for x in numbers:
    doubled.append(x * 2)
list_time = time.perf_counter() - start
# %%
start = time.perf_counter()
doubled_arr = arr * 2
numpy_time = time.perf_counter() - start
# %%
print(f"List loop: {list_time * 1000:.1f} ms")
print(f"NumPy:     {numpy_time * 1000:.1f} ms")
print(f"NumPy was about {list_time / numpy_time:.0f} times faster")
# %%
scores = np.array([63, 34, 69, 57, 64, 65, 55, 61, 58, 87])
scores
# %%
np.arange(0, 10, 2)
# %%
np.zeros(5)
# %%
np.ones(3)
# %%
np.linspace(0, 1, 5)
# %%
scores.dtype
# %%
np.array([1, 2.5, 3])
# %%
np.array([1, 2.5, 3]).dtype
# %%
scores.nbytes
# %%
scores.shape, scores.ndim, scores.size
# %%
quizzes = np.array([[7, 9, 6, 8],
                    [5, 6, 7, 4],
                    [9, 10, 8, 9]])
quizzes.shape, quizzes.ndim, quizzes.size
# %%
scores + 5
# %%
scores * 1.1
# %%
quiz1 = np.array([7, 5, 9])
quiz2 = np.array([8, 6, 10])
quiz1 + quiz2
# %%
scores >= 50
# %%
print((scores >= 50).sum())
# %%
scores[scores >= 50]
# %%
scores.mean()
# %%
print(scores.mean())
print(scores.min(), scores.max())
print(scores.sum())
# %%
import csv
with open("students.csv") as f:
    rows = list(csv.DictReader(f))

exam = np.array([int(row["exam_score"]) for row in rows])
exam.shape, exam.dtype
# %%
print(exam[:10])
print("Mean:", round(exam.mean(), 1))
print("Min:", exam.min(), "Max:", exam.max())
# %%
passed = exam >= 50
print("Passed:", passed.sum(), "of", exam.size)
print("Pass rate:", round(passed.mean() * 100, 1), "%")
print("Mean of those who passed:", round(exam[passed].mean(), 1))
# %%
a_list = [1, 2, 3]
an_array = np.array([1, 2, 3])
# %%
a_list + a_list
# %%
an_array + an_array
# %%
a_list * 2
# %%
an_array * 2
# %%
a_list + 5
# %%
an_array + 5
# %%
mixed = np.array([72, 85, "absent", 90])
mixed
# %%
mixed + 5
# %%
as_text = np.array([row["exam_score"] for row in rows])
as_text[:5]
# %%
as_text[:5].astype(int)
# %%
np.array([72, 85, np.nan, 90])
