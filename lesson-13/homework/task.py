import numpy as np

# 1. Create a vector with values ranging from 10 to 49.
vector = np.arange(10, 50)

# 2. Create a 3x3 matrix with values ranging from 0 to 8.
matrix_3x3 = np.arange(9).reshape(3, 3)

# 3. Create a 3x3 identity matrix.
identity_matrix = np.eye(3)

# 4. Create a 3x3x3 array with random values.
array_3x3x3 = np.random.random((3, 3, 3))

# 5. Create a 10x10 array with random values and find the minimum and maximum values.
array_10x10 = np.random.random((10, 10))
min_value = array_10x10.min()
max_value = array_10x10.max()

# 6. Create a random vector of size 30 and find the mean value.
random_vector = np.random.random(30)
mean_value = random_vector.mean()

# 7. Normalize a 5x5 random matrix.
random_matrix_5x5 = np.random.random((5, 5))
normalized_matrix = (
    random_matrix_5x5 - random_matrix_5x5.mean()
) / random_matrix_5x5.std()

# 8. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product).
matrix_5x3 = np.random.random((5, 3))
matrix_3x2 = np.random.random((3, 2))
matrix_product = np.dot(matrix_5x3, matrix_3x2)

# 9. Create two 3x3 matrices and compute their dot product.
matrix_a = np.random.random((3, 3))
matrix_b = np.random.random((3, 3))
dot_product = np.dot(matrix_a, matrix_b)

# 10. Given a 4x4 matrix, find its transpose.
matrix_4x4 = np.random.random((4, 4))
transpose_matrix = matrix_4x4.T

# 11. Create a 3x3 matrix and calculate its determinant.
matrix_3x3_det = np.random.random((3, 3))
determinant = np.linalg.det(matrix_3x3_det)

# 12. Create two matrices A (3x4) and B (4x3), and compute the matrix product A · B.
matrix_A = np.random.random((3, 4))
matrix_B = np.random.random((4, 3))
matrix_product_AB = np.dot(matrix_A, matrix_B)

# 13. Create a 3x3 random matrix and a 3-element column vector. Compute the matrix-vector product.
matrix_3x3_rand = np.random.random((3, 3))
vector_3 = np.random.random(3)
matrix_vector_product = np.dot(matrix_3x3_rand, vector_3)

# 14. Solve the linear system Ax = b where A is a 3x3 matrix, and b is a 3x1 column vector.
A = np.random.random((3, 3))
b = np.random.random(3)
solution_x = np.linalg.solve(A, b)

# 15. Given a 5x5 matrix, find the row-wise and column-wise sums.
matrix_5x5 = np.random.random((5, 5))
row_sums = matrix_5x5.sum(axis=1)
column_sums = matrix_5x5.sum(axis=0)