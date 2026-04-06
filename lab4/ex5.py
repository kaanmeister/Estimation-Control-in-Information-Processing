import numpy as np
import matplotlib.pyplot as plt

# time in hours, energy in kWh
time = np.array([1, 2, 3, 4, 5])
energy = np.array([12, 23, 34, 46, 55]) 

#fit linear model (Energy = slope * time + intercept)
A = np.vstack([time, np.ones(len(time))]).T
w, _, _, _ = np.linalg.lstsq(A, energy, rcond=None)
slope, intercept = w

print(f"Fitted Model: Energy = {slope:.2f} * Time + {intercept:.2f}")
print(f"Interpretation: The slope ({slope:.2f}) represents the energy consumption rate.")
print(f"This means the smart home consumes approximately {slope:.2f} units of energy per unit of time (e.g., kWh per hour).")

plt.scatter(time, energy, color='blue', label='Actual Energy Data')
plt.plot(time, slope * time + intercept, color='red', label=f'Linear Fit (y = {slope:.2f}x + {intercept:.2f})')

plt.title("Smart Home Energy Consumption Over Time")
plt.xlabel("Time (Hours)")
plt.ylabel("Energy (kWh)")
plt.legend()
plt.grid(True)
plt.savefig('energy_model.png')