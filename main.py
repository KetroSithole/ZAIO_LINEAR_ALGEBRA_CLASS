import pandas as pd
import numpy as np

# Read the CSV file (no headers)
df = pd.read_csv('vectors.csv', header=None)

# Iterate over each row and convert to NumPy vector
for i, row in df.iterrows():
    vector = np.array(row.dropna().tolist(), dtype=float)
    print(f"{len(vector)}D Vector at row {i + 1}: {vector}")
