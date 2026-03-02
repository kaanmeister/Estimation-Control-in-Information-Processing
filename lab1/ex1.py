import matplotlib.pyplot as plt
import numpy as np

# Number of time steps
n_steps = 50

# Initialize the true state array
# We assume the initial state x(0) is 0
x = np.zeros(n_steps)
x[0] = 0 

# Simulate the system: x(t+1) = x(t) + 1
for t in range(n_steps - 1):
    x[t+1] = x[t] + 1

# Plot the evolution of the true state
plt.figure(figsize=(8, 5))
plt.plot(range(n_steps), x, marker='o', linestyle='-', color='b', label='True State', markersize=4)

# Formatting the plot
plt.xlabel('Time step (t)')
plt.ylabel('State x(t)')
plt.title('Evolution of the True State: x(t+1) = x(t) + 1')
plt.grid(True)
plt.legend()
plt.tight_layout()

# Save the plot
plt.savefig('true_state.png')