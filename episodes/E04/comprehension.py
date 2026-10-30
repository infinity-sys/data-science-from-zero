# %%
scores = [63, 34, 69, 57, 64]
curved = []
for s in scores:
    curved.append(s + 5)
print(curved)
# %%
curved = [s + 5 for s in scores]
print(curved)
# %%
passed = [s for s in scores if s >= 50]
print(passed)
