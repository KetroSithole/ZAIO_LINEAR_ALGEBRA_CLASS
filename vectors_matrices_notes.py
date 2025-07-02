"""
📘 Vectors and Matrices – Python Notes with Examples
This file contains well-commented, simple explanations and code for vector & matrix operations
used in data science and machine learning.
"""

import numpy as np

# -----------------------------------
# 🔹 VECTOR BASICS
# -----------------------------------

# A vector is just a list of numbers (1D array)
vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])

# ➕ Addition
vector_add = vector_a + vector_b  # Element-wise addition
print("Vector Addition:", vector_add)

# ➖ Subtraction
vector_sub = vector_b - vector_a
print("Vector Subtraction:", vector_sub)

# ✖️ Scalar multiplication
vector_scaled = 3 * vector_a
print("Scalar Multiplication:", vector_scaled)

# 🔘 Dot product (used in ML to calculate similarity, projections, etc.)
dot_product = np.dot(vector_a, vector_b)
print("Dot Product:", dot_product)

# 📏 Norm (length of the vector, also called magnitude)
vector_norm = np.linalg.norm(vector_a)
print("Vector Norm (Length):", vector_norm)

# -----------------------------------
# 🔹 MATRIX BASICS
# -----------------------------------

# A matrix is a 2D array of numbers
matrix_A = np.array([[1, 2], [3, 4]])
matrix_B = np.array([[5, 6], [7, 8]])

# ➕ Matrix addition
matrix_add = matrix_A + matrix_B
print("\nMatrix Addition:\n", matrix_add)

# ➖ Matrix subtraction
matrix_sub = matrix_B - matrix_A
print("Matrix Subtraction:\n", matrix_sub)

# ✖️ Scalar multiplication
matrix_scaled = 2 * matrix_A
print("Scalar Matrix Multiplication:\n", matrix_scaled)

# 🔁 Transpose: Flip rows and columns
matrix_transpose = matrix_A.T
print("Transpose:\n", matrix_transpose)

# 🧮 Matrix multiplication (not element-wise!)
matrix_mult = np.dot(matrix_A, matrix_B)  # or matrix_A @ matrix_B
print("Matrix Multiplication:\n", matrix_mult)

# ❌ Inverse of a matrix (if square and invertible)
matrix_inverse = np.linalg.inv(matrix_A)
print("Matrix Inverse:\n", matrix_inverse)

# -----------------------------------
# 🔹 REAL-WORLD EXAMPLE: LINEAR REGRESSION
# -----------------------------------

# Suppose we want to fit: y = β0 + β1 * x
# Data: 3 samples, 1 feature (x), 1 constant (bias)
X = np.array([[1, 1], [1, 2], [1, 3]])  # shape: (3 samples x 2 features)
y = np.array([5, 7, 9])                # output values

# Step 1: Compute transpose of X
X_T = X.T

# Step 2: Calculate beta using: β = (XᵀX)^(-1) Xᵀy
beta = np.linalg.inv(X_T @ X) @ X_T @ y
print("\nLinear Regression Coefficients:", beta)

# Expected model: y ≈ 3x + 2 → beta ≈ [2, 3]
# That means:
# β0 = 2 (intercept), β1 = 3 (slope)
