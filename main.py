import pandas as pd
import numpy as np


# Read CSV without headers
df = pd.read_csv('vectors.csv', header=None)

for index, row in df.iterrows():
    # Drop NaN values if row has fewer than 4 columns
    vector_values = row.dropna().values.astype(float)
    vector = np.array(vector_values)
    
    print(f"Vector at row {index + 1} ({len(vector)}D): {vector}")
