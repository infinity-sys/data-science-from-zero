# %%
import numpy as np

scores = np.array([63, 34, 69, 57, 64, 65, 55, 61, 58, 87])
print(scores.sum(), scores.mean(), scores.min(), scores.max())
# %%
print(np.sort(scores))
print(np.median(scores))
# %%
typo = scores.copy()
typo[9] = 870              # a typo: 870 instead of 87
print(typo.mean(), np.median(typo))
# %%
calm = np.array([58, 60, 61, 59, 62])
wild = np.array([35, 90, 48, 82, 45])
print(calm.mean(), wild.mean())
print(round(calm.std(), 1), round(wild.std(), 1))
print(calm.var(), wild.var())
# %%
exams = np.array([[72, 85, 90],    # Mona
                  [64, 58, 71],    # Omar
                  [88, 92, 79],    # Sara
                  [55, 67, 62],    # Karim
                  [91, 74, 86]])   # Laila
print(exams.sum())                 # all 15 scores
print(exams.mean(axis=0))          # down: one mean per exam
print(exams.mean(axis=1).round(1)) # across: one per student
# %%
print(exams.max(axis=0))           # best score in each exam
print(exams.min(axis=1))           # each student's worst exam
# %%
names = np.array(["Mona", "Omar", "Sara", "Karim", "Laila"])
avg = exams.mean(axis=1)
print(avg.argmax(), names[avg.argmax()])
print(avg.argmin(), names[avg.argmin()])
# %%
print(exams.argmax(axis=0))         # who topped each exam
print(names[exams.argmax(axis=0)])
# %%
import csv
with open("students.csv") as f:
    rows = list(csv.DictReader(f))

exam = np.array([int(r["exam_score"]) for r in rows])
print(exam.size, round(exam.mean(), 1), np.median(exam))
# %%
print(np.percentile(exam, [25, 50, 75]))
print(np.quantile(exam, 0.9))
# %%
# my study hours this week, Saturday to Friday
week = np.array([2, 3.5, 0, 4, 1.5, 5, 2])
print(week.sum())
print(week.cumsum())
# %%
dept = np.array([r["department"] for r in rows])
values, counts = np.unique(dept, return_counts=True)
print(values)
print(counts)
# %%
raw = [r["study_hours_per_week"] for r in rows]
hours = np.array([float(h) if h != "" else np.nan for h in raw])
print(hours[12:19])        # a few rows around the first gap
print(hours.mean())
# %%
print(np.nan + 1, np.nan > 3)
# %%
missing = np.isnan(hours)
print(missing.sum())
print(np.where(missing)[0])
# %%
print(round(np.nanmean(hours), 1))
print(np.nanmedian(hours), np.nanmax(hours))
print(round(hours[~missing].mean(), 1))
# %%
rng = np.random.default_rng(42)
print(rng.integers(1, 7, size=10))
rng = np.random.default_rng(42)
print(rng.integers(1, 7, size=10))
rng = np.random.default_rng(7)
print(rng.integers(1, 7, size=10))
# %%
rng = np.random.default_rng(2026)
print(rng.integers(1, 7, size=5))    # whole numbers 1-6
print(rng.random(3).round(3))        # decimals in [0, 1)
print(rng.normal(60, 15, size=4).round(1))  # mean 60, std 15
print(rng.choice(["CS", "Arts", "Medicine"], size=4))
# %%
rng = np.random.default_rng(2026)
flips = rng.integers(0, 2, size=10_000)  # 1 = heads
print(flips[:20])
print(flips.mean())
# %%
running = flips.cumsum() / np.arange(1, 10_001)
print(running[[9, 99, 999, 9999]])
# %%
rng = np.random.default_rng(2026)
rolls = rng.integers(1, 7, size=(10_000, 2))  # 2 dice
sums = rolls.sum(axis=1)
print(rolls[:3])
print(sums[:3])
# %%
values, counts = np.unique(sums, return_counts=True)
print(values)
print(counts)
print(values[counts.argmax()])
# %%
rng = np.random.default_rng(2026)
sample = rng.choice(exam, size=50, replace=False)
print(sample.mean(), round(exam.mean(), 1))
# %%
means = np.array([
    rng.choice(exam, size=50, replace=False).mean()
    for _ in range(1000)])
print(round(means.mean(), 1), round(means.std(), 1))
print(means.min(), means.max())
print(np.percentile(means, [2.5, 97.5]).round(1))
