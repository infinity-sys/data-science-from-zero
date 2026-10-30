# %%
scores = [63, 34, 69, 57, 64]
total = 0
passed = 0
for score in scores:
    total = total + score
    if score >= 50:
        passed += 1
print("Total:", total)
print("Average:", total / len(scores))
print("Passed:", passed, "of", len(scores))
