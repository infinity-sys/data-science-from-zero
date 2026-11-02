# %%
import pandas as pd

students = pd.read_csv("students_clean.csv")
students["study_level"] = pd.cut(students["study_hours_per_week"],
                                 bins=[0, 5, 10, 100],
                                 labels=["low", "medium", "high"],
                                 right=False)
print(students["study_level"].value_counts(dropna=False))
# %%
def grade(score):
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

students["letter"] = students["exam_score"].apply(grade)
print(students[["student_id", "exam_score", "letter"]].head(3))
print(students["letter"].value_counts().sort_index())
