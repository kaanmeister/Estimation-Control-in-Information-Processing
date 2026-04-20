import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# exercise 10 setup
num_steps = 50
time = np.arange(num_steps)
a = 0.9
b = 0.5
c = 1.0
q = 0.01
r = 0.04
l_gain = 0.5 #control law gain

x_true = np.zeros(num_steps)
x_est = np.zeros(num_steps) 
u_ctrl = np.zeros(num_steps)

x_true[0] = 2.0
x_est_prior = 0.0 
p = 1.0

for t in range(num_steps):
    v = np.random.normal(0, np.sqrt(r))
    y = c * x_true[t] + v #measurement
    
    k = (p * c) / (c * p * c + r) #kalman gain
    x_est[t] = x_est_prior + k * (y - c * x_est_prior) #update state
    p = (1 - k * c) * p #update covariance
    
    u_ctrl[t] = -l_gain * x_est[t] #control law
    
    if t < num_steps - 1:
        w = np.random.normal(0, np.sqrt(q))
        x_true[t+1] = a * x_true[t] + b * u_ctrl[t] + w #simulate next state
        x_est_prior = a * x_est[t] + b * u_ctrl[t] #predict next state
        p = a * p * a + q #predict covariance

# exercise 11 setup
time_nl = np.arange(30)
x_nl = np.zeros(30)
x_nl[0] = 0.5
u_nl = 0.2 * np.sin(time_nl) 

for t in range(29):
    x_nl[t+1] = x_nl[t] + 0.1 * (x_nl[t]**2) + u_nl[t] #nonlinear update

# plotting everything
plt.figure(figsize=(10, 10))

plt.subplot(3, 1, 1) #ex 10 state plot
plt.plot(time, x_true, label='true state', color='blue', linewidth=2)
plt.plot(time, x_est, label='estimated state', color='red', linestyle='--', linewidth=2)
plt.title('exercise 10: closed loop state feedback')
plt.ylabel('state')
plt.legend()
plt.grid(True)

plt.subplot(3, 1, 2) #ex 10 control plot
plt.step(time, u_ctrl, label='control signal u(t)', color='purple', linewidth=2)
plt.ylabel('control input')
plt.legend()
plt.grid(True)

plt.subplot(3, 1, 3) #ex 11 nonlinear plot
plt.plot(time_nl, x_nl, label='nonlinear state', color='green', linewidth=2)
plt.title('exercise 11: nonlinear system simulation')
plt.xlabel('time step (t)')
plt.ylabel('state')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig('ex10_ex11_control_nonlinear.png', dpi=300, bbox_inches='tight') #saving figure
plt.show()