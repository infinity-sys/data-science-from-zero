# Data Science: From Zero to Hero

A free course by **Infinity Systems** on YouTube, made for **computer science students** and **anyone curious about data**. No background is needed: we start from zero.

- Playlist: https://www.youtube.com/playlist?list=PLDy7xS_6LZus
- New episodes every Wednesday and Saturday at 20:00 Cairo time.
- Website: https://www.infinitysys.org

## Episodes
| # | Episode | Video | Code |
|---|---|---|---|
| E01 | What Is Data Science | https://youtu.be/g5jMB3q0VAk | [`episodes/E01`](episodes/E01) |
| E02 | Setting Up Python, Jupyter and Colab | https://youtu.be/QbUAjlUAg84 | [`episodes/E02`](episodes/E02) |
| E03 | Python Variables, Types, Lists and Dictionaries | https://youtu.be/kZuEcJhIdcA | [`episodes/E03`](episodes/E03) |
| E04 | Python Loops, Conditions and Functions | https://youtu.be/MN39wEHRl0o | [`episodes/E04`](episodes/E04) |
| E05 | Reading Data Files: CSV and JSON | https://youtu.be/ctgqrIEx7gw | [`episodes/E05`](episodes/E05) |
| E06 | NumPy Arrays | https://youtu.be/sRSDN2E7Yvk | [`episodes/E06`](episodes/E06) |
| E07 | NumPy Indexing, Slicing and Broadcasting | https://youtu.be/psk9r4OgcRA | [`episodes/E07`](episodes/E07) |
| E08 | NumPy Aggregations and Random Simulation | https://youtu.be/dLxzKRXBckY | [`episodes/E08`](episodes/E08) |
| E09 | Linear Algebra for Data Science | https://youtu.be/9zlXUvJjyfI | [`episodes/E09`](episodes/E09) |
| E10 | pandas Series and DataFrames | https://youtu.be/hNQJ0ddCgDA | [`episodes/E10`](episodes/E10) |
| E11 | Loading and Inspecting a Real Dataset | https://youtu.be/Z5ySU7tbVoE (public Wed 4 Nov 2026) | [`episodes/E11`](episodes/E11) |
| E12 | Selecting and Filtering Data | https://youtu.be/nJzoXRaOF7U (premieres Sat 7 Nov 2026, 20:00 Cairo) | [`episodes/E12`](episodes/E12) |

## pandas versions
E01 to E09 ran on pandas 3.x (E02 installs the latest pandas). E10, E11 and E12 were recorded with pandas 2.3.3 (see each `versions.txt`).
On pandas 3, text columns show the dtype `str` where those episodes show `object` (for example in `df.info()` and `df.dtypes`).
Every number is the same on both versions; only that dtype label differs.

## What's here
| Folder | What it holds |
|---|---|
| `data/students.csv` | The course dataset: 500 university students (study hours, attendance, sleep, assignments, part-time job, exam score). We use it in almost every episode. |
| `data/make_students.py` | The script that generated the dataset (synthetic data, fixed seed 2026). |
| `episodes/E01`, `E02`, … | The code shown in each episode, exactly as it ran on screen. |

## Load the dataset
On your computer, after downloading `students.csv` next to your notebook:
```python
import pandas as pd
df = pd.read_csv("students.csv")
```
In Google Colab, or anywhere online, read it straight from this repository:
```python
import pandas as pd
url = "https://raw.githubusercontent.com/infinity-sys/data-science-from-zero/main/data/students.csv"
df = pd.read_csv(url)
```

## About the data
`students.csv` is **synthetic**: no real students are in it. It was built to behave like real data:
- the columns are related to each other in realistic ways
- a few values are missing
- a few rows are duplicated

That gives us real cleaning work to do in the course.

| column | meaning |
|---|---|
| `student_id` | S0001 to S0500 |
| `department` | CS, Engineering, Business, Medicine, Arts |
| `year` | year of study, 1 to 4 |
| `study_hours_per_week` | self-study hours per week |
| `attendance_pct` | share of lectures attended, % |
| `sleep_hours` | average hours of sleep per night |
| `assignments_submitted` | assignments handed in, out of 10 |
| `part_time_job` | yes / no |
| `exam_score` | final exam, 0 to 100 |
| `passed` | yes if exam_score is 50 or more |

## License
- Code: MIT License.
- Dataset: CC BY 4.0 (free to use and share, with credit to Infinity Systems).

Prepared by Infinity Systems · www.infinitysys.org
