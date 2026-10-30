# %%
def average(values):
    """Return the mean of a list of numbers."""
    return sum(values) / len(values)

def passed(score, pass_mark=50):
    """Return True if the score reaches the pass mark."""
    return score >= pass_mark
# %%
assert passed(50)            # exactly 50 passes
assert not passed(49)        # 49 fails
assert average([2, 4]) == 3
print("All tests passed")
