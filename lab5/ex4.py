import numpy as np
import matplotlib.pyplot as plt

T = 30
A, B, C = 1, 1, 1
u = 1
x0 = 0

#noise parameters 
Q = 0.01  
R = 0.5   
#init arrays
x_true = np.zeros(T)
y_measured = np.zeros(T)
x_hat = np.zeros(T)    # Kalman estimate
P_history = np.zeros(T) # Covariance history
K_history = np.zeros(T) # Kalman Gain history

curr_x_true = x0
curr_x_hat = 0         # x_hat(0|0)
curr_P = 1             # P(0|0) = 1

#kalman filter loop
for t in range(T):
    # --- REALITY (Simulation) ---
    x_true[t] = curr_x_true
    v_t = np.random.normal(0, np.sqrt(R))
    y_measured[t] = C * curr_x_true + v_t
    
    #update true state for next step
    w_t = np.random.normal(0, np.sqrt(Q))
    curr_x_true = A * curr_x_true + B * u + w_t    
    x_pred = A * curr_x_hat + B * u
    P_pred = A * curr_P * A + Q

    #kalman gain: K = P_pred * C / (C * P_pred * C + R)
    K = P_pred * C * (1.0 / (C * P_pred * C + R))
    
    #update estimate with measurement: x_hat = x_pred + K*(y - C*x_pred)
    curr_x_hat = x_pred + K * (y_measured[t] - C * x_pred)
    
    #update covariance: P = (1 - K*C) * P_pred
    curr_P = (1 - K * C) * P_pred
    
    x_hat[t] = curr_x_hat
    P_history[t] = curr_P
    K_history[t] = K

plt.figure(figsize=(12, 10))

#plot 1: States
plt.subplot(3, 1, 1)
plt.plot(x_true, label='True State', color='blue', linewidth=2)
plt.scatter(range(T), y_measured, label='Noisy Measurement', color='red', alpha=0.3, s=20)
plt.plot(x_hat, label='Kalman Estimate', color='green', linestyle='--', marker='o', markersize=4)
plt.title('Full Kalman Filter: State Estimation')
plt.legend()
plt.grid(True)

#plot 2: Kalman Gain
plt.subplot(3, 1, 2)
plt.plot(K_history, label='Kalman Gain (K)', color='purple')
plt.title('Kalman Gain over Time')
plt.ylabel('Gain Value')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(P_history, label='Error Covariance (P)', color='orange')
plt.title('Estimation Covariance (Certainty)')
plt.xlabel('Time Step')
plt.ylabel('P value')
plt.grid(True)

plt.tight_layout()
plt.show()
plt.savefig('ex4.png')