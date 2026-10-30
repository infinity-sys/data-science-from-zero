# %%
import numpy as np

rng = np.random.default_rng(42)
rolls = rng.integers(1, 7, size=(10_000, 2))   # 10,000 rolls x 2 dice
print(rolls[:5])
# %%
sums = rolls.sum(axis=1)       # one total per roll
print(sums[:5])
print((sums == 7).sum())       # how many sevens
# %%
print((sums == 7).mean())      # the fraction: True counts as 1
print(round(6 / 36, 4))        # the exact answer
