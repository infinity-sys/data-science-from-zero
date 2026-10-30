# In Colab (or any computer that is online): read students.csv straight from the course repo
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/infinity-sys/data-science-from-zero/main/data/students.csv")
df.shape
