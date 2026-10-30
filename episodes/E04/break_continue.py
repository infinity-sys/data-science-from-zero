# %%
scores = [63, None, 69, 34, 57]
for score in scores:
    if score is None:
        continue
    if score < 50:
        print("First fail:", score)
        break
    print("OK:", score)
