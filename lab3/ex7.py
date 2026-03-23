import numpy as np
import matplotlib.pyplot as plt

true_x = 10
n_measurements = 1000

np.random.seed(42)
noise = np.random.normal(loc=0.0, scale=1.0, size=n_measurements)
y = true_x + noise

estimated_x = np.mean(y)
estimation_error = estimated_x - true_x
print(f"True Value:       {true_x:.4f}")
print(f"Estimated Value:  {estimated_x:.4f}")
print(f"Estimation Error: {estimation_error:.4f}")
plt.figure(figsize=(8, 5))
plt.hist(y, bins=30, color='thistle', edgecolor='black', alpha=0.7, label='Noisy Measurements')
plt.axvline(true_x, color='red', linestyle='solid', linewidth=3, 
            label=f'True Value ({true_x})')
plt.axvline(estimated_x, color='blue', linestyle='dashed', linewidth=3, 
            label=f'Estimate ({estimated_x:.4f})')

plt.title('Distribution of Noisy Measurements vs. Estimate')
plt.xlabel('Measured Value')
plt.ylabel('Frequency')
plt.legend()
plt.savefig('estimation_comparison.png', dpi=300, bbox_inches='tight')
plt.show()