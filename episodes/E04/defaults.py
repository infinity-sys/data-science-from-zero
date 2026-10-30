# %%
def passed(score, pass_mark=50):
    """Return True if the score reaches the pass mark."""
    return score >= pass_mark
# %%
print(passed(57))
print(passed(57, pass_mark=60))
# %%
help(passed)
