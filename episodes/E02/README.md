# E02: Setting Up: Python, Jupyter Notebook and Google Colab
Video: https://youtu.be/QbUAjlUAg84

- `setup_check.ipynb` / `setup_check.py`: the notebook from the episode: a version check, Episode 1's code run for real, the kernel's memory (`average`), and a first look at `students.csv` (`df.shape`, `df.head()`). Put `students.csv` (from `data/`) next to it.
- `colab_load.py`: in Google Colab, read `students.csv` straight from this repo with `pd.read_csv("https://raw.githubusercontent.com/...")`, no upload needed.

Setup commands (macOS / Linux; on Windows type `python` instead of `python3`):

```
python3 --version
python3 -m venv dsenv
source dsenv/bin/activate          # Windows PowerShell: dsenv\Scripts\Activate.ps1
pip install numpy pandas matplotlib seaborn jupyterlab notebook
cd ds-course                       # the folder with students.csv
jupyter lab                        # or: jupyter notebook
```
