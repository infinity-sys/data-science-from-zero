# %%
me = {
    "name": "Mona",
    "department": "CS",
    "year": 2,
    "study_hours": [2, 3.5, 4.3, 1.5, 2.5],
}
print(me["name"], me["department"], me["year"])
# %%
average = sum(me["study_hours"]) / len(me["study_hours"])
print(average)
print(round(average, 1))
