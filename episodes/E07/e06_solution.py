# %%
import numpy as np

scores = np.array([55, 72, 88, 96, 61, 79, 84, 99, 47, 68])
print(scores + 5)
# %%
bonus = np.minimum(scores + 5, 100)   # cap at 100
print(bonus)
# %%
print("Mean before:", scores.mean())
print("Mean after: ", bonus.mean())
