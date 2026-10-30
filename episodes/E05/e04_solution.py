# %%
def grade(score):
    """Return the letter grade for a score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
# %%
print(grade(90), grade(89))
# %%
scores = [95, 82, 67, 74, 58, 88, 91, 70]
counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
for score in scores:
    letter = grade(score)
    counts[letter] += 1
print(counts)
