import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 0, 1
gaussian_data = np.random.normal(mu, sigma, 10000)
uniform_data = np.random.uniform(-np.sqrt(3), np.sqrt(3), 10000)

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.hist(gaussian_data, bins=50, density=True, alpha=0.7, color='blue', edgecolor='black')
plt.title('Gaussian (Normal) Distribution\nMean = 0, Std = 1')
plt.xlabel('Value')
plt.ylabel('Density')
plt.grid(axis='y', alpha=0.5)

plt.subplot(1, 2, 2)
plt.hist(uniform_data, bins=50, density=True, alpha=0.7, color='green', edgecolor='black')
plt.title('Uniform Distribution\nMean = 0, Std = 1')
plt.xlabel('Value')
plt.ylabel('Density')
plt.grid(axis='y', alpha=0.5)

plt.tight_layout()
plt.savefig('gaussian_vs_uniform.png')
