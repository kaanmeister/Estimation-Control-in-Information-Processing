import numpy as np

#sensor data
sensor1 = [1, 2]
sensor2 = [2, 4]
A = np.column_stack([sensor1, sensor2])
num_columns = A.shape[1]
rank = np.linalg.matrix_rank(A)
is_independent = (rank == num_columns)

print("Matrix A:")
print(A)
print(f"\nMatrix Rank: {rank}")
print(f"Number of Columns: {num_columns}")
print(f"Are the columns linearly independent? {is_independent}")

#why it fails
print("\n--- Why the system fails ---")
print("The system fails because the columns of Matrix A are linearly dependent.")
print("Sensor 2 is simply a scalar multiple of Sensor 1 (Sensor2 = 2 * Sensor1).")
print("Because they provide redundant information, the matrix is singular (rank 1 instead of 2).")
print("In linear algebra terms, A^T A is not invertible, meaning standard least squares cannot find a unique solution.")