import numpy as np

time = np.array([1, 2, 3])
humidity = np.array([40, 42, 45])
A = np.vstack([time, np.ones(len(time))]).T
y = humidity

#compute a and b (w contains [a, b])
w, _, _, _ = np.linalg.lstsq(A, y, rcond=None)

#compute predicted values Ax (which is A @ w in our notation)
y_pred = A @ w 

#compute residual r = y - Ax
r = y - y_pred

#compute squared error
squared_error = np.sum(r**2)
print(f"Predicted values (Ax): {y_pred}")
print(f"Residuals (r): {r}")
print(f"Squared Error: {squared_error:.4f}")