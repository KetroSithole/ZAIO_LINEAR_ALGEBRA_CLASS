import numpy as np

X = np.array([[1, 1], [1, 2], [1, 3]])
y = np.array([2, 4, 6])

X_T = X.T
beta = np.linalg.inv(X_T @ X) @ X_T @ y

print("\nLinear Regression Coefficients:", beta)
