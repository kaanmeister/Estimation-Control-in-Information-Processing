import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

a = 0.9
b = 0.5
c = 1.0
num_steps = 50
time = np.arange(num_steps)

u = np.sin(0.2 * time)
process_noise = np.random.normal(0, 0.1, num_steps)
measurement_noise = np.random.normal(0, 0.2, num_steps)

x_true = np.zeros(num_steps)
y = np.zeros(num_steps)

x_true[0] = 2.0
y[0] = c * x_true[0] + measurement_noise[0]

for t in range(1, num_steps): #generate true data
    x_true[t] = a * x_true[t-1] + b * u[t] + process_noise[t]
    y[t] = c * x_true[t] + measurement_noise[t]

def run_kalman(q_val, r_val): #kalman filter function
    x_kf = np.zeros(num_steps)
    p = 1.0
    for t in range(1, num_steps):
        x_pri = a * x_kf[t-1] + b * u[t]
        p_pri = a * p * a + q_val
        k = (p_pri * c) / (c * p_pri * c + r_val)
        x_kf[t] = x_pri + k * (y[t] - c * x_pri)
        p = (1 - k * c) * p_pri
    return x_kf

q_values = [0.0001, 0.01, 1]
r_fixed = 0.04

plt.figure(figsize=(10, 10))

plt.subplot(2, 1, 1) #plots for exercise 6
plt.plot(time, x_true, label='true state', color='black', linewidth=2)
plt.scatter(time, y, label='measurements', color='gray', s=10)
for q in q_values:
    x_est = run_kalman(q, r_fixed)
    plt.plot(time, x_est, label=f'q={q}')
plt.title('exercise 6: effect of process noise covariance q')
plt.legend()

q_fixed = 0.01
r_values = [0.01, 0.5, 5]

plt.subplot(2, 1, 2) #plots for exercise 7
plt.plot(time, x_true, label='true state', color='black', linewidth=2)
plt.scatter(time, y, label='measurements', color='gray', s=10)
for r in r_values:
    x_est = run_kalman(q_fixed, r)
    plt.plot(time, x_est, label=f'r={r}')
plt.title('exercise 7: effect of measurement noise covariance r')
plt.legend()

plt.tight_layout()
plt.savefig('ex6_ex7_covariance_effects.png', dpi=300, bbox_inches='tight') #saving figure
plt.show()