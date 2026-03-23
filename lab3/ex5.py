import numpy as np
import matplotlib.pyplot as plt

mean = 0
variances = [1, 4, 9]  # Using variances 1, 4, and 9 (Standard deviations: 1, 2, and 3)
colors = ['blue', 'orange', 'green']
labels = [f'Variance = {v} ($\sigma$ = {np.sqrt(v):.1f})' for v in variances]

plt.figure(figsize=(10, 6))
for variance, color, label in zip(variances, colors, labels):
    std_dev = np.sqrt(variance)
    noise = np.random.normal(mean, std_dev, 10000)
    plt.hist(noise, bins=100, density=True, alpha=0.5, color=color, label=label)

plt.title('Gaussian Noise Distributions with Different Variances', fontsize=14)
plt.xlabel('Noise Value', fontsize=12)
plt.ylabel('Probability Density', fontsize=12)
plt.xlim(-12, 12)
plt.legend(fontsize=12)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('gaussian_variances.png', dpi=300)
