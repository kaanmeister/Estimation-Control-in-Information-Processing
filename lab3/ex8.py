import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42) # For reproducibility
mean = [0, 0]      # Mean of X and Y
cov_matrix = [[1.0, 0.8], 
              [0.8, 1.0]]
x, y = np.random.multivariate_normal(mean, cov_matrix, 1000).T

# 3. Compute the sample covariance matrix
computed_cov = np.cov(x, y)
print("Computed Covariance Matrix:")
print(computed_cov)

print(f"\nComputed Covariance between X and Y: {computed_cov[0, 1]:.4f}")
plt.figure(figsize=(8, 6))
plt.scatter(x, y, alpha=0.5, color='coral', edgecolor='k')
plt.title('Scatter Plot of Two Correlated Random Variables')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig('correlated_variables.png', dpi=300, bbox_inches='tight')
plt.show()