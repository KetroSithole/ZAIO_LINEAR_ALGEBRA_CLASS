import numpy as np

v1 = np.array([3, 6, 9])
v2 = np.array([1, 2, 3])

# 1. Element-wise subtraction
subtraction = v1 - v2
print("Subtraction:", subtraction)  # [2, 4, 6]

# 2. Element-wise multiplication
elementwise_mul = v1 * v2
print("Element-wise Multiplication:", elementwise_mul)  # [3, 12, 27]

# 3. Element-wise division (covered earlier)
division = v1 / v2
print("Element-wise Division:", division)  # [3., 3., 3.]

# 4. Vector comparison (returns boolean array)
comparison = v1 > v2
print("Comparison (v1 > v2):", comparison)  # [True, True, True]

# 5. Summation of vector elements
sum_v1 = np.sum(v1)
print("Sum of v1 elements:", sum_v1)  # 18

# 6. Cumulative sum
cumsum_v1 = np.cumsum(v1)
print("Cumulative Sum:", cumsum_v1)  # [3, 9, 18]

# 7. Cross product (only for 3D vectors)
cross_prod = np.cross(v1, v2)
print("Cross Product:", cross_prod)  # [0, 0, 0] (parallel vectors)

# 8. Outer product
outer_prod = np.outer(v1, v2)
print("Outer Product:\n", outer_prod)

# 9. Vector projection of v1 onto v2
proj_v1_on_v2 = (np.dot(v1, v2) / np.dot(v2, v2)) * v2
print("Projection of v1 onto v2:", proj_v1_on_v2)

# 10. Checking orthogonality (dot product == 0)
v3 = np.array([1, 0, 0])
v4 = np.array([0, 1, 0])
print("Are v3 and v4 orthogonal?", np.dot(v3, v4) == 0)