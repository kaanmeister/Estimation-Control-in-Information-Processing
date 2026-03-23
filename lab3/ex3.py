import numpy as np
import matplotlib.pyplot as plt

# 1. Generate the data
np.random.seed(42) # Keeping the seed for reproducibility
x = np.random.uniform(0, 1, 1000)

# 2. Compute means
sample_mean = np.mean(x)
theoretical_mean = 0.5

# Print the comparison to the console
print(f"Sample Mean: {sample_mean:.4f}")
print(f"Theoretical Mean: {theoretical_mean:.4f}")
print(f"Difference: {abs(sample_mean - theoretical_mean):.4f}")

# 3. Create the Plot
plt.hist(x, bins=20, color='lightgreen', edgecolor='black')

# Add vertical lines to visually compare the means
plt.axvline(sample_mean, color='red', linestyle='dashed', linewidth=2, 
            label=f'Sample Mean ({sample_mean:.4f})')
plt.axvline(theoretical_mean, color='blue', linestyle='solid', linewidth=2, 
            label=f'Theoretical Mean ({theoretical_mean})')

# Labels and Title
plt.title('Histogram of X ~ Uniform(0, 1)')
plt.xlabel('Value of X')
plt.ylabel('Frequency')
plt.legend()

# Save and show
plt.savefig('output2_with_means.png', dpi=300, bbox_inches='tight')
plt.show()