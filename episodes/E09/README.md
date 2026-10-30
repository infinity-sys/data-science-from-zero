# E09: Linear Algebra for Data Science: Vectors, Dot Products and Matrices
Video: https://youtu.be/9zlXUvJjyfI

Every file comes as a `.py` script (cells marked with `# %%`) and as a Jupyter notebook (`.ipynb`) with the real outputs. Python 3.13, NumPy 2.5.

- `e08_solution.py` / `e08_solution.ipynb`: the solution of the E08 exercise: 10,000 rolls of two dice with `rng = np.random.default_rng(42)`, one total per roll with `rolls.sum(axis=1)`, the share of 7s with `(sums == 7).mean()` (0.1645) and the exact 6/36 (0.1667).
- `e09_linear_algebra.py` / `e09_linear_algebra.ipynb`: every cell of the episode with its real output: a row of `students.csv` as a vector and a column as a feature vector, adding and scaling vectors (the average of two students), the dot product as a weighted sum with `np.dot` and `@` (a receipt and a grade formula), the sign of a dot product, the norm with `np.linalg.norm`, cosine similarity (by hand, on raw rows and on standardized features with `np.nanmean` / `np.nanstd`), a 5 × 3 matrix `X`, `X @ w` for every student and for all 503 rows, the shape rule and the `ValueError` when it breaks, the transpose `X.T`, `X @ W` with two grade formulas, and the identity `np.eye(3)`. Put `students.csv` (from `data/`) next to it and run the cells in order.
