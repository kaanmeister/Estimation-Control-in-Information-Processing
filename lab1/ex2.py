import matplotlib.pyplot as plt
import numpy as np

# Number of time steps
n_steps = 50

# Re-create the true state
x = np.zeros(n_steps)
for t in range(n_steps - 1):
    x[t+1] = x[t] + 1

# Generate Gaussian noise with mean 0 and standard deviation 2
np.random.seed(42) # Setting a seed for reproducible results
noise = np.random.normal(0, 2, n_steps)

# Generate noisy observations: y(t) = x(t) + noise
y = x + noise

# Plot true state and observations on the same graph
plt.figure(figsize=(8, 5))
plt.plot(range(n_steps), x, marker='o', linestyle='-', color='b', label='True State x(t)', markersize=4)
plt.scatter(range(n_steps), y, color='r', label='Noisy Observations y(t)', marker='x', zorder=5)

# Formatting the plot
plt.xlabel('Time step (t)')
plt.ylabel('Value')
plt.title('True State vs. Noisy Observations')
plt.grid(True)
plt.legend()
plt.tight_layout()

# Save the plot
plt.savefig('true_vs_noisy.png')