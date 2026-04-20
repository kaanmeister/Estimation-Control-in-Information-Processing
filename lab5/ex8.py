import numpy as np
import matplotlib.pyplot as plt

a = 0.9
c = 1.0
q = 0.01
r = 0.04
num_steps = 50
time = np.arange(num_steps)

p_predicted = np.zeros(num_steps)
p_updated = np.zeros(num_steps)

p = 1.0 
p_updated[0] = p

for t in range(1, num_steps):
    p_pri = a * p * a + q #predict covariance
    p_predicted[t] = p_pri
    
    k = (p_pri * c) / (c * p_pri * c + r) 
    p = (1 - k * c) * p_pri #update covariance
    p_updated[t] = p

plt.figure(figsize=(10, 6))

plt.plot(time[1:], p_predicted[1:], label='$P(t|t-1)$ (predicted)', color='red', linestyle='--', linewidth=2)
plt.plot(time[1:], p_updated[1:], label='$P(t|t)$ (updated)', color='blue', linewidth=2)

plt.title('exercise 8: covariance analysis')
plt.xlabel('time step (t)')
plt.ylabel('error covariance')
plt.legend()
plt.grid(True)

plt.savefig('ex8_covariance_analysis.png', dpi=300, bbox_inches='tight') #saving figure
plt.show()