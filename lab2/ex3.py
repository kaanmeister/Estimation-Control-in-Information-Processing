import numpy as np
import matplotlib.pyplot as plt

# The given parameters
r_values = [2, 2.5, 1, 1.2, 3.1, 0.5, 4, 4.4, 3, 2, 9, 2.8, 1.9, 1.5, 1.4, 7, 3.8, 8]
K = 100  # Carrying Capacity
P0 = 5   # Initial Population

# Create a 6x3 grid for the 18 plots
fig, axes = plt.subplots(6, 3, figsize=(15, 20))
axes = axes.flatten()
t_eval = np.linspace(0, 10, 100)

for idx, r in enumerate(r_values):
    # Calculate population using the continuous logistic model
    P = K / (1 + ((K - P0) / P0) * np.exp(-r * t_eval))
    
    # Plotting each simulation
    axes[idx].plot(t_eval, P, color='blue', linewidth=2)
    axes[idx].axhline(K, color='red', linestyle='--', alpha=0.7) # Carrying capacity line
    axes[idx].set_title(f'Simulation with r = {r}', fontsize=12)
    axes[idx].set_xlabel('Time (t)')
    axes[idx].set_ylabel('Population Size (P)')
    axes[idx].grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.savefig('all_r_simulations.png', dpi=150)
plt.close()
print("Exercise 1 Complete: Saved 'all_r_simulations.png'")

# ==========================================
# EXERCISE 2: Population across 17 years
# ==========================================
years = np.arange(len(r_values) + 1)
P_yearly = [P0]

for i in range(len(r_values)):
    r = r_values[i]
    P_prev = P_yearly[-1]
    # Calculate next year's population 
    P_next = K / (1 + ((K - P_prev) / P_prev) * np.exp(-r * 1))
    P_yearly.append(P_next)


growth_yearly = np.diff(P_yearly)
plt.figure(figsize=(10, 5))
plt.plot(years, P_yearly, 'g-o', linewidth=2, label='Total Population Size')
plt.bar(years[1:], growth_yearly, color='orange', alpha=0.6, label='Yearly Growth (New Additions)')
plt.axhline(K, color='red', linestyle='--', label='Carrying Capacity (K=100)')

plt.title('Population Fate Over 17 Years with Variable r Factors', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Population / Growth Size', fontsize=12)
plt.xticks(years)
plt.legend(loc='center right')
plt.grid(True, linestyle=':', alpha=0.7)

plt.savefig('variable_r_simulation.png', dpi=300, bbox_inches='tight')
plt.close()
print("Exercise 2 Complete: Saved 'variable_r_simulation.png'")
print(f"\n--- ANSWER TO EXERCISE 2 ---")
print(f"By the 17th year, the total population size is: {P_yearly[17]:.2f}")
print(f"Therefore, the growth DURING the 17th year is: {growth_yearly[16]:.2f}")