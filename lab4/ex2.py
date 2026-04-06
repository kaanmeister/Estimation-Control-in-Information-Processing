import numpy as np

time = np.array([1, 2, 3])
humidity = np.array([40, 42, 45])

#build matrix A and vector y
# A is built with x (time) in the first column and 1s in the second column for the intercept b
A = np.vstack([time, np.ones(len(time))]).T
y = humidity

#compute a and b using least squares
# np.linalg.lstsq solves the equation Aw = y for w = [a, b]^T
w, residuals, rank, s = np.linalg.lstsq(A, y, rcond=None)
a, b = w
print("Matrix A:")
print(A)
print("\nVector y:")
print(y)
print("\nLeast Squares Solution:")
print(f"a = {a:.2f}")
print(f"b = {b:.2f}")
print(f"Model: y = {a:.2f}x + {b:.2f}")