import numpy as np
vector_1 = np.array([1, 2, 3, 4, 5, 6]) # You can only add vectors that have the same size
vector_2 = np.array([2, 4, 6, 8, 10, 11])
print(vector_1)
print(vector_2)

print("Addition:", vector_1 + vector_2) # Vector Addition
print("Multiplication:", vector_1 * vector_2) # Scalar Multiplication
print("Multiplication by 3:", vector_1 * 3)  # Scalar Multiplication
print("Divide:", vector_2/vector_1)
print("Divide by 2:", vector_2/2)
dot_product = np.dot(vector_1, vector_2)
print("Dot product:", dot_product)
magnitude = np.linalg.norm(vector_1)
print("Length:", magnitude)
unit_vector = vector_1/magnitude
print("Normalizing the vector:", unit_vector)

