import numpy as np
import matplotlib.pyplot as plt

# 1. Setup Parameters
T = 30
A = 1
B = 1
C = 1
u = 1      
x0 = 0          

process_noise_std = 0.5    
measure_noise_std = 1.0   

#initialize arrays to store results
x_true = np.zeros(T)
y_measured = np.zeros(T)

#simulation Loop
current_x = x0

for t in range(T):
    # Store true state
    x_true[t] = current_x
    v_t = np.random.normal(0, measure_noise_std)
    y_measured[t] = C * current_x + v_t
    w_t = np.random.normal(0, process_noise_std)
    current_x = A * current_x + B * u + w_t

plt.figure(figsize=(10, 6))
plt.plot(range(T), x_true, label='True State (x)', color='blue', linewidth=2)
plt.scatter(range(T), y_measured, label='Measured Output (y)', color='red', alpha=0.6)

plt.title('Simple Linear Dynamic System')
plt.xlabel('Time Step (t)')
plt.ylabel('Value')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig('ex1.png')
plt.show()