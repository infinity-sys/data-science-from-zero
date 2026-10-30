# %% [markdown]
# # Setup check
# Episode 2: Python, Jupyter and our dataset

# %%
import sys, numpy, pandas
print("Python", sys.version.split()[0])
print("numpy", numpy.__version__)
print("pandas", pandas.__version__)

# %%
# Study hours per week and exam scores of 8 students
hours  = [2, 4, 5, 7, 9, 10, 12, 15]
scores = [48, 58, 55, 66, 70, 74, 85, 82]

average = sum(scores) / len(scores)
print("Average score:", average)

low  = scores[:4]    # the 4 who studied least
high = scores[4:]    # the 4 who studied most
print("Less study:", sum(low) / len(low))
print("More study:", sum(high) / len(high))

# %%
average

# %%
import pandas as pd
df = pd.read_csv("students.csv")
df.shape

# %%
df.head()
