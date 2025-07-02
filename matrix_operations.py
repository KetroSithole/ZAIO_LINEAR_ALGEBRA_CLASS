import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

m_add = A + B
m_sub = B - A
m_scalar = 3 * A
m_transpose = A.T
m_mul = A @ B
m_inv = np.linalg.inv(A)

print("\nMatrix Operations:")
print("Add:\n", m_add)
print("Subtract:\n", m_sub)
print("Scalar Multiply:\n", m_scalar)
print("Transpose:\n", m_transpose)
print("Matrix Multiply:\n", m_mul)
print("Inverse:\n", m_inv)
