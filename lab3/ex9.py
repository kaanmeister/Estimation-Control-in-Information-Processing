import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
n_samples = 10000
x = np.random.normal(0, 1, n_samples)
y = 0.7 * x + np.random.normal(0, 0.714, n_samples) # y is positively correlated with x
A = x > 0
B = y > 0
P_A = np.mean(A)
P_B = np.mean(B)

P_A_and_B = np.mean(A & B) 
P_A_given_B = P_A_and_B / P_B
print(f"P(A): {P_A:.4f}")
print(f"P(B): {P_B:.4f}")
print(f"P(A and B): {P_A_and_B:.4f}")
print(f"P(A | B): {P_A_given_B:.4f}")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
ax1.scatter(x[~(A | B)], y[~(A | B)], alpha=0.1, color='gray', label='Neither')
ax1.scatter(x[A & ~B], y[A & ~B], alpha=0.2, color='blue', label='A only (X>0)')
ax1.scatter(x[~A & B], y[~A & B], alpha=0.2, color='green', label='B only (Y>0)')
ax1.scatter(x[A & B], y[A & B], alpha=0.3, color='red', label='A and B (X>0 & Y>0)')
ax1.axvline(0, color='black', linestyle='--', linewidth=1)
ax1.axhline(0, color='black', linestyle='--', linewidth=1)

ax1.set_title('Scatter Plot of Simulated Events')
ax1.set_xlabel('Variable X')
ax1.set_ylabel('Variable Y')
ax1.legend()

# Plot 2: Bar chart comparing the estimated probabilities
labels = ['P(A)', 'P(B)', 'P(A and B)', 'P(A | B)']
values = [P_A, P_B, P_A_and_B, P_A_given_B]
colors = ['blue', 'green', 'red', 'purple']

ax2.bar(labels, values, color=colors, edgecolor='black', alpha=0.7)
for i, v in enumerate(values):
    ax2.text(i, v + 0.02, f"{v:.3f}", ha='center', fontweight='bold')

ax2.set_ylim(0, 1.1) # Scale Y-axis from 0 to 1 (probability bounds)
ax2.set_title('Estimated Probabilities')
ax2.set_ylabel('Probability')
plt.tight_layout()
plt.savefig('conditional_probability.png', dpi=300, bbox_inches='tight')
plt.show()