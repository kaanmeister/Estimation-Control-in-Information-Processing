import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42) # Set seed for reproducible random noise

A = 0.9  # State transition scalar 
B = 0.5  # Control input scalar
C = 1.0  # Observation scalar
Q = 0.01 # Process noise variance (standard deviation = 0.1)
R = 0.04 # Measurement noise variance (standard deviation = 0.2)

num_steps = 50
time = np.arange(num_steps)

u = np.sin(0.2 * time) 
process_noise = np.random.normal(0, np.sqrt(Q), num_steps)
measurement_noise = np.random.normal(0, np.sqrt(R), num_steps)

x_true = np.zeros(num_steps)
y = np.zeros(num_steps)

# Start true state at 2.0 to create an initial error for the filter to handle
x_true[0] = 2.0 
y[0] = C * x_true[0] + measurement_noise[0]

for t in range(1, num_steps):
    x_true[t] = A * x_true[t-1] + B * u[t] + process_noise[t]
    y[t] = C * x_true[t] + measurement_noise[t]

x_pred_only = np.zeros(num_steps)
x_pred_only[0] = 0.0 # Initial flawed guess

for t in range(1, num_steps):
    # Only the prediction equation (no measurement updates)
    x_pred_only[t] = A * x_pred_only[t-1] + B * u[t]

x_kf = np.zeros(num_steps)
x_kf[0] = 0.0 # Initial flawed guess
P = 1.0       # Initial error covariance (uncertainty)

for t in range(1, num_steps):
    x_priori = A * x_kf[t-1] + B * u[t]
    P_priori = A * P * A + Q
    
    # --- UPDATE STEP (a posteriori) ---
    # 1. Compute Kalman Gain
    K = (P_priori * C) / (C * P_priori * C + R) 
    
    #update estimate with measurement y[t]
    x_kf[t] = x_priori + K * (y[t] - C * x_priori)
    
    #update error covariance
    P = (1 - K * C) * P_priori

# np.mean neatly handles the 1/N * Summation formula
mse_pred_only = np.mean((x_true - x_pred_only)**2)
mse_kf = np.mean((x_true - x_kf)**2)

print(f"MSE - Prediction Only:    {mse_pred_only:.4f}")
print(f"MSE - Full Kalman Filter: {mse_kf:.4f}")
#plots
plt.figure(figsize=(10, 6))

plt.plot(time, x_true, label='True State $x(t)$', color='blue', linewidth=2)
plt.plot(time, x_pred_only, label='Prediction Only (Case 1)', color='red', linestyle='--', linewidth=2)
plt.plot(time, x_kf, label='Full Kalman Filter (Case 2)', color='green', linestyle='-.', linewidth=2)
plt.scatter(time, y, label='Noisy Measurements $y(t)$', color='gray', s=15, alpha=0.5)

plt.title('Exercise 5: Prediction Only vs Full Kalman Filter')
plt.xlabel('Time step ($t$)')
plt.ylabel('State Value')
plt.legend()
plt.grid(True)
plt.savefig('ex5_kalman_comparison.png', dpi=300, bbox_inches='tight')
plt.show()