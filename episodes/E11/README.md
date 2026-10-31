# E11: Loading and Inspecting a Real Dataset
Video: VIDEO_LINK_PLACEHOLDER

Every file comes as a `.py` script (cells marked with `# %%`) and as a Jupyter notebook (`.ipynb`) with the real outputs. Python 3.10, pandas 2.3.3, NumPy 2.2.6 (see `versions.txt`). In pandas 3, text columns show the dtype `str` instead of `object`.

- `e10_solution.py` / `e10_solution.ipynb`: the solution of the E10 exercise: a DataFrame of five friends (`name`, `age`, `city`, `hours_online`), the new column `hours_per_week = hours_online * 7` (shape (5, 5)), and `sort_values("hours_per_week", ascending=False)`: Karim first with 42.0, Nour last with 17.5.
- `e11_inspect.py` / `e11_inspect.ipynb`: a first look at `students.csv`: `pd.read_csv` and `shape` (503, 10), `head()` and `tail(3)`, `info()` (non-null counts 497, 494, 491), `isna().sum()` (27 missing cells in 26 rows), `duplicated().sum()` (3 exact copies) and `nunique()` of `student_id` (500), the duplicate pairs with `keep=False`, `describe()` rounded and transposed, `value_counts()` of the departments and of `passed` (`normalize=True`), and the mean exam score (59.81) and study hours (11.52). Put `students.csv` (from `data/`) next to it and run the cells in order.
