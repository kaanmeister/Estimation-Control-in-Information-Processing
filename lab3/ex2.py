import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0, 1, 1000)

plt.hist(x, bins=20, color='lightgreen', edgecolor='black')
plt.title('Histogram of X ~ Uniform(0, 1)')
plt.xlabel('Value of X')
plt.ylabel('Frequency')
plt.savefig('output2.png', dpi=300, bbox_inches='tight')
plt.show()