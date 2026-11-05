# E15: GroupBy and Aggregation
Video: link coming soon (premieres Wed 18 Nov 2026, 20:00 Cairo)

Every file comes as a `.py` script (cells marked with `# %%`) and as a Jupyter notebook (`.ipynb`) with the real outputs. Python 3.13.5, pandas 2.3.3, NumPy 2.2.6 (see `versions.txt`).

- `e14_solution.py` / `e14_solution.ipynb`: the solution of the E14 exercise: `dept_code` with `.str[:3].str.upper()` (CS, BUS, ENG); `study_per_day` (hours / 7, 1 decimal): the top student is S0160 with 3.9 hours a day (27.6 a week); 1 January 2027 is a Friday, 48 days after 14 November 2026.
- `e15_groupby.py` / `e15_groupby.ipynb`: split, apply, combine with `groupby`: the mean exam score by year (59.2, 61.3, 60.6, 58.2); the mean of a True/False column as a rate (pass rate 0.826 without a part-time job, 0.533 with one); several summaries with `.agg(["mean", "min", "max", "count"])`; `size()` (110, 123, 135, 132) versus `count()` (109, 122, 130, 130) on `attendance_pct`, which has 9 missing values; named aggregation (`students`, `mean_score`, `pass_rate`); and grouping by two columns, `["year", "part_time_job"]` (8 groups). Put `students_clean.csv` (made in E13) next to it and run the cells in order.

Note: recorded with pandas 2.3.3. On pandas 3, text columns show the dtype `str` instead of `object`; all numbers are the same.
