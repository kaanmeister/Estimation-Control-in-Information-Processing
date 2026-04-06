import numpy as np

errors = np.array([-1, 2, -2])

#compute squared error (Sum of Squared Errors)
squared_error = np.sum(errors**2)

#compute absolute error (Sum of Absolute Errors)
absolute_error = np.sum(np.abs(errors))


print(f"Errors: {errors}")
print(f"Squared Error (SSE): {squared_error}")
print(f"Absolute Error (SAE): {absolute_error}")
print("\n--- Comparison Breakdown ---")
print(f"Individual Absolute Errors: {np.abs(errors)}")
print(f"Individual Squared Errors:  {errors**2}")