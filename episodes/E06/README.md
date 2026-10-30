# E06: NumPy Arrays: Why Data Scientists Don't Use Plain Lists
Video: https://youtu.be/sRSDN2E7Yvk

Every file comes as a `.py` script (cells marked with `# %%`) and as a Jupyter notebook (`.ipynb`) with the real outputs. Python 3.13, NumPy 2.5.

- `e05_solution.py` / `e05_solution.ipynb`: the solution of the E05 exercise: read `students.csv` with the `csv` module, count the students in each department, and save the counts to `department_counts.json`. The counts include the 3 duplicate rows of the file (503 rows); we clean them in E12. Put `students.csv` (from `data/`) next to it.
- `e06_numpy_arrays.py` / `e06_numpy_arrays.ipynb`: every cell of the episode with its real output: the speed test (a list loop vs NumPy on 1,000,000 numbers; your times will differ from ours), creating arrays (`np.array`, `arange`, `zeros`, `ones`, `linspace`), `dtype` and `nbytes`, `shape`, `ndim` and `size`, element-wise arithmetic, comparisons and a first boolean mask, `mean`, `min`, `max` and `sum`, the `exam_score` column of `students.csv` as an array, lists vs arrays side by side, and the mixed-types error (`dtype='<U21'`). Put `students.csv` next to it. Cells 33 and 36 raise `TypeError` and `UFuncTypeError` on purpose, so "Run All" stops there: run the cells after them one by one.
