# E12: Selecting and Filtering Data
Video: VIDEO_LINK_PLACEHOLDER

Every file comes as a `.py` script (cells marked with `# %%`) and as a Jupyter notebook (`.ipynb`) with the real outputs. Python 3.10, pandas 2.3.3, NumPy 2.2.6 (see `versions.txt`).

- `e11_solution.py` / `e11_solution.ipynb`: the solution of the E11 exercise: `shape` (503, 10); the columns with missing values, `missing[missing > 0]` (study_hours_per_week 6, attendance_pct 9, sleep_hours 12); and the mean `exam_score`, 59.81.
- `e12_filter.py` / `e12_filter.ipynb`: selecting and filtering `students.csv`: one column (a Series) and a list of columns (a DataFrame), `loc[0:2]` (3 rows, end included) vs `iloc[0:2]` (2 rows), the mask `department == "CS"` (143 rows), `&` and `|` (115 and 408 rows), `isin(["Arts", "Medicine"])` (137), `sleep_hours < 6` (66; the 12 missing values never pass), `query(...)` (115), group means with `loc[mask, "exam_score"]` (all 59.81, CS 60.31, sleep under 6 hours 57.26), and the top three CS students with `sort_values`. Put `students.csv` (from `data/`) next to it and run the cells in order.

Note: recorded with pandas 2.3.3. On pandas 3, text columns show the dtype `str` instead of `object`; all numbers are the same.
