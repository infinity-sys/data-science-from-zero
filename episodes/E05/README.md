# E05: Reading Data: Files, CSV and JSON
Video: https://youtu.be/ctgqrIEx7gw

Every file comes as a `.py` script (cells marked with `# %%`) and as a Jupyter notebook (`.ipynb`) with the real outputs. Python 3.13, pandas 3.0.

- `e04_solution.py` / `e04_solution.ipynb`: the solution of the E04 exercise, the `grade()` function and counting the grades of `[95, 82, 67, 74, 58, 88, 91, 70]`
- `e05_reading_data.py` / `e05_reading_data.ipynb`: every cell of the episode with its real output: file size and bytes, the working folder (`os.getcwd`, `os.listdir`, `os.path.exists`, `os.path.abspath`), `open()` with `with` and `encoding="utf-8"`, `read()`, `readlines()`, writing `summary.txt`, the raw lines of `students.csv`, `csv.reader` and `csv.DictReader`, `json.dump` / `json.load` (`summary.json`), three errors on purpose, the missing study hours, and a first taste of pandas. Put `students.csv` (from `data/`), `study_log.txt` and `names_ar.txt` next to the notebook. Cells 21, 22 and 24 raise `FileNotFoundError`, `UnicodeDecodeError` and `ValueError` on purpose, so "Run All" stops there: run the cells after them one by one.
- `study_log.txt`: Mona's study hours for five days (the text file read in the episode)
- `names_ar.txt`: three Arabic names saved as UTF-8 (for the encoding error)
