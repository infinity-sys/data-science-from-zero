# E07: NumPy Indexing, Slicing and Broadcasting
Video: https://youtu.be/psk9r4OgcRA

Every file comes as a `.py` script (cells marked with `# %%`) and as a Jupyter notebook (`.ipynb`) with the real outputs. Python 3.13, NumPy 2.5.

- `e06_solution.py` / `e06_solution.ipynb`: the solution of the E06 exercise: turn the 10 scores into a NumPy array, give everyone 5 bonus points capped at 100 with `np.minimum`, and print the mean before (74.9) and after (79.4).
- `e07_indexing_broadcasting.py` / `e07_indexing_broadcasting.ipynb`: every cell of the episode with its real output: 1-D indexing and slicing, a 6 × 3 grid of students × exams (`exams[r, c]`, `exams[r]`, `exams[:, c]` and blocks), `shape` and `reshape`, boolean masks and fancy indexing on a grid, views vs copies and `.copy()`, `axis=0` vs `axis=1` for `mean` and `sum`, broadcasting a scalar, a row and a column, centring each exam column and min-max scaling to 0–1, and a 2-D slice of the numeric columns of `students.csv` with `np.genfromtxt`. Put `students.csv` (from `data/`) next to it. Cells 10 and 23 raise `ValueError` on purpose (a shape that doesn't fit, and shapes that can't be broadcast), so "Run All" stops there: run the cells after them one by one.
