import numpy as np
import matplotlib.pyplot as plt

true_x = 10
n_measurements = 1000

np.random.seed(42) # For reproducibility
# Generating Gaussian (normal) noise with mean=0 and standard deviation=1
noise = np.random.normal(loc=0.0, scale=1.0, size=n_measurements) 
y = true_x + noise
plt.figure(figsize=(10, 5)) # Making the plot a bit wider for better visibility
plt.plot(y, marker='o', linestyle='', markersize=4, alpha=0.5, color='purple', label='Noisy Measurements (y)')

plt.axhline(true_x, color='red', linewidth=3, label=f'True Value (x={true_x})')
plt.title('Simulation of Noisy Measurements over Time')
plt.xlabel('Measurement Index (e.g., Time step)')
plt.ylabel('Measured Value')
plt.legend()
plt.savefig('measurements_with_noise.png', dpi=300, bbox_inches='tight')
plt.show()