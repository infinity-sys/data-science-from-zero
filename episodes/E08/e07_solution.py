# %%
import numpy as np

exams = np.array([[72, 85, 90],    # 5 students (rows)
                  [64, 58, 71],    # x 3 exams (columns)
                  [88, 92, 79],
                  [55, 67, 62],
                  [91, 74, 86]])
exams.shape
# %%
print(exams[1])       # the 2nd student's row
print(exams[:, 2])    # the 3rd exam's column
# %%
print(exams.mean(axis=0))   # one mean per exam
# %%
centred = exams - exams.mean(axis=0)   # broadcasting
centred
