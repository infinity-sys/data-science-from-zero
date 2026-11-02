# E14: Transforming Data: New Columns, Text and Dates
Video: https://youtu.be/fbmOkAHAb1I (premieres Sat 14 Nov 2026, 20:00 Cairo)

Every file comes as a `.py` script (cells marked with `# %%`) and as a Jupyter notebook (`.ipynb`) with the real outputs. Python 3.13.5, pandas 2.3.3, NumPy 2.2.6 (see `versions.txt`).

- `e13_solution.py` / `e13_solution.ipynb`: the solution of the E13 exercise: `study_level` with `pd.cut(bins=[0, 5, 10, 100], right=False)`: high 305, medium 119, low 70, and 6 students with no study hours (NaN); `letter` with `grade()` and `.apply`: A 13, B 36, C 68, D 139, F 244.
- `e14_transform.py` / `e14_transform.ipynb`: new columns from old ones: `study_per_day` (hours / 7, rounded), `high_attendance` (29 students at 90 or above), `faculty` with `.map` and a dictionary; text with the `.str` accessor: `.str.upper()`, `.str[1:]` for the ID number, `.str.contains("ing")` (119 students); dates with a small `submissions` table: `pd.to_datetime`, `.dt.day_name()`, and days late against a deadline (-1, 2, 0, 5: 2 late). Put `students_clean.csv` (made in E13) next to it and run the cells in order.

Note: recorded with pandas 2.3.3. On pandas 3, text columns show the dtype `str` instead of `object`; all numbers are the same.
