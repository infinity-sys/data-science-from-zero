# E13: Cleaning Data: Missing Values, Duplicates and Types
Video: https://youtu.be/alRTtbabQGo (premieres Wed 11 Nov 2026, 20:00 Cairo)

Every file comes as a `.py` script (cells marked with `# %%`) and as a Jupyter notebook (`.ipynb`) with the real outputs. Python 3.13.5, pandas 2.3.3, NumPy 2.2.6 (see `versions.txt`).

- `e12_solution.py` / `e12_solution.ipynb`: the solution of the E12 exercise: CS students in year 4 with attendance above 90, combined with `&` in parentheses: 2 students (S0266 with 70, S0500 with 86), mean `exam_score` 78.0.
- `e13_clean.py` / `e13_clean.ipynb`: cleaning `students.csv`: 503 rows, `duplicated().sum()` finds 3 repeated rows (S0035, S0098, S0398); `drop_duplicates()` leaves 500 rows and `student_id` is unique; `isna().sum()` gives 6, 9 and 12 missing values (study hours, attendance, sleep hours); `dropna()` would keep only 474 rows; `sleep_hours` filled with its median, 6.8; `dtypes`; `passed` and `part_time_job` turned from "yes"/"no" text into True/False (378 passed, mean 0.756); `reset_index(drop=True)` and `to_csv("students_clean.csv", index=False)`, (500, 10) with 15 missing values left on purpose. Put `students.csv` (from `data/`) next to it and run the cells in order.

Note: recorded with pandas 2.3.3. On pandas 3, text columns show the dtype `str` instead of `object`; all numbers are the same.
