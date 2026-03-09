import numpy as np 
import numpy as np
import matplotlib.pyplot as plt

#the model parameters
r = 0.9       
K = 100       
P0 = 5        

#time steps
# This creates 100 evenly spaced time points between 0 and 10
t = np.linspace(0, 10, 100)

#calculate the population at each time step using the logistic equation
# P(t) = K / (1 + ((K - P0) / P0) * e^(-r*t))
P = K / (1 + ((K - P0) / P0) * np.exp(-r * t))

plt.figure(figsize=(8, 5))
plt.plot(t, P, color='blue', linewidth=2.5, label=f'Growth Rate (r) = {r}')
plt.axhline(y=K, color='red', linestyle='--', label=f'Carrying Capacity (K) = {K}')
plt.title('Logistic Population Growth Simulation', fontsize=14)
plt.xlabel('Time (t)', fontsize=12)
plt.ylabel('Population Size (P)', fontsize=12)
plt.legend(loc='lower right')
plt.grid(True, linestyle=':', alpha=0.7)
output_filename = 'logistic_growth_simulation.png'
plt.savefig(output_filename, dpi=300, bbox_inches='tight')

print(f"Simulation complete! The plot has been saved as '{output_filename}' in your current folder.")
plt.show()