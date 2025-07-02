import numpy as np

v1 = np.array([1, 2])
v2 = np.array([3, 4])

v_add = v1 + v2
v_sub = v2 - v1
v_mul = 2 * v1
v_dot = np.dot(v1, v2)
v_norm = np.linalg.norm(v1)

print("Vector Operations:")
print("Add:", v_add)
print("Subtract:", v_sub)
print("Scalar Multiply:", v_mul)
print("Dot Product:", v_dot)
print("Norm:", v_norm)
