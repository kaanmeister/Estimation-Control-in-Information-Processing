import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 0. Setup: Simulate a System to get Data
# ==========================================
# We define a generic 1D system to have data to work with.
A = np.array([[0.9]])  # State transition matrix
B = np.array([[0.5]])  # Control input matrix
C = np.array([[1.0]])  # Observation matrix

num_steps = 50
time = np.arange(num_steps)
u = np.sin(0.2 * time) 
process_noise = np.random.normal(0, 0.1, num_steps)
measurement_noise = np.random.normal(0, 0.2, num_steps)
x_true = np.zeros(num_steps)
y = np.zeros(num_steps)
x_true[0] = 2.0
y[0] = C[0,0] * x_true[0] + measurement_noise[0]

for t in range(1, num_steps):
    x_true[t] = A[0,0] * x_true[t-1] + B[0,0] * u[t] + process_noise[t]
    y[t] = C[0,0] * x_true[t] + measurement_noise[t]

#ex2
#equation: x_hat(t|t-1) = A * x_hat(t-1|t-1) + B * u(t)
x_pred = np.zeros(num_steps)
#initial condition
x_pred[0] = 0.0 

#predicted state
for t in range(1, num_steps):
    x_pred[t] = A[0,0] * x_pred[t-1] + B[0,0] * u[t]

#ex3
#equation: innovation = y(t) - C * x_hat(t|t-1)

innovation = np.zeros(num_steps)

#compute innovation at each time step
for t in range(num_steps):
    innovation[t] = y[t] - C[0,0] * x_pred[t]

plt.figure(figsize=(10, 8))
#plot for ex2
plt.subplot(2, 1, 1)
plt.plot(time, x_true, label='True State', color='blue', linewidth=2)
plt.plot(time, x_pred, label='Predicted State (Open-Loop)', color='red', linestyle='--', linewidth=2)
plt.title('Exercise 2: Prediction Step')
plt.xlabel('Time step (t)')
plt.ylabel('State Value')
plt.legend()
plt.grid(True)

#plot for ex3
plt.subplot(2, 1, 2)
plt.plot(time, innovation, label='Innovation', color='green', linewidth=2)
plt.axhline(0, color='black', linestyle='--', linewidth=1) # Zero reference line
plt.title('Exercise 3: Innovation')
plt.xlabel('Time step (t)')
plt.ylabel('Innovation Value')
plt.legend()
plt.grid(True)

plt.tight_layout()

# --- NEW CODE ADDED HERE ---
# Save the figure to your current working directory
plt.savefig('ex2_3.png', dpi=300, bbox_inches='tight')

plt.show()