# %%
import pandas as pd

friends = pd.DataFrame({
    "name": ["Laila", "Karim", "Nour", "Youssef", "Hana"],
    "age": [21, 22, 20, 23, 21],
    "city": ["Cairo", "Alexandria", "Giza", "Cairo", "Mansoura"],
    "hours_online": [3.5, 6.0, 2.5, 4.0, 5.5],
})
print(friends)
# %%
friends["hours_per_week"] = friends["hours_online"] * 7
print(friends.shape)
# %%
print(friends.sort_values("hours_per_week", ascending=False))
