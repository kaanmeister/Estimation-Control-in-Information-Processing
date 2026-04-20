import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

dt = 1
a = np.array([[1, dt], [0, 1]]) #state transition matrix
c = np.array([[1, 0]]) #observation matrix
q = np.array([[0.01, 0], [0, 0.01]])
r = np.array([[1.0]])
i = np.eye(2) 

num_steps = 50
time = np.arange(num_steps)

x_true = np.zeros((2, num_steps))
y = np.zeros(num_steps)

x_true[:, 0] = [0, 2] #initial position=0, velocity=2

for t in range(1, num_steps):
    process_noise = np.random.multivariate_normal([0, 0], q)
    x_true[:, t] = a @ x_true[:, t-1] + process_noise #simulate constant velocity
    
measurement_noise = np.random.normal(0, np.sqrt(r[0,0]), num_steps)

for t in range(num_steps):
    y[t] = c @ x_true[:, t] + measurement_noise[t]

x_est = np.zeros((2, num_steps))
x_est[:, 0] = [0, 0] #initial guess with wrong velocity
p = np.array([[10, 0], [0, 10]]) 

for t in range(1, num_steps):
    x_pri = a @ x_est[:, t-1]
    p_pri = a @ p @ a.T + q
    
    k = p_pri @ c.T @ np.linalg.inv(c @ p_pri @ c.T + r) #kalman gain
    
    inn = np.array([y[t]]) - c @ x_pri
    x_est[:, t] = x_pri + k @ inn
    p = (i - k @ c) @ p_pri

plt.figure(figsize=(10, 8))

plt.subplot(2, 1, 1) #plot position
plt.plot(time, x_true[0, :], label='true position', color='blue', linewidth=2)
plt.plot(time, x_est[0, :], label='estimated position', color='red', linestyle='--', linewidth=2)
plt.scatter(time, y, label='noisy measurements', color='gray', s=15, alpha=0.5)
plt.title('exercise 9: position estimation')
plt.xlabel('time step (t)')
plt.ylabel('position')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2) #plot velocity
plt.plot(time, x_true[1, :], label='true velocity', color='green', linewidth=2)
plt.plot(time, x_est[1, :], label='estimated velocity', color='orange', linestyle='--', linewidth=2)
plt.title('exercise 9: velocity estimation')
plt.xlabel('time step (t)')
plt.ylabel('velocity')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig('ex9_pos_vel_estimation.png', dpi=300, bbox_inches='tight') #saving figure
plt.show()