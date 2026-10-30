# Data Science: From Zero to Hero

A free course by **Infinity Systems** on YouTube, made for **computer science students** and **anyone curious about data**. No background is needed: we start from zero.

- Playlist: https://www.youtube.com/playlist?list=PLDy7xS_6LZus
- A new episode every day.
- Website: https://www.infinitysys.org

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
