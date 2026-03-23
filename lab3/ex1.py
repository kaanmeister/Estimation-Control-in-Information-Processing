import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
random_numbers = np.random.rand(1000)

plt.hist(random_numbers, bins=30, color='skyblue', edgecolor='black')

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of 1000 Random Numbers')
plt.savefig('output1.png', dpi=300, bbox_inches='tight')
plt.show()