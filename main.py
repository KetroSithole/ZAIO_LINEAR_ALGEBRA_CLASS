import pandas as pd
import numpy as np

# Define the data directly
data = [
    [1, 2, 3, None],
    [4, 5, None, None],
    [6, 7, 8, 9],
    [10, None, None, None]
]

# Create DataFrame
df = pd.DataFrame(data)

# Iterate over each row and convert to NumPy vector
for i, row in df.iterrows():
    vector = np.array(row.dropna().tolist(), dtype=float)
    print(f"{len(vector)}D Vector at row {i + 1}: {vector}")
