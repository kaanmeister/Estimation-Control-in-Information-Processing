import numpy as np
import matplotlib.pyplot as plt

t_steps = 50
t = np.arange(t_steps)

r_stable = 2.8   #stable growth rate
r_chaotic = 3.8  #highly chaotic growth rate

pop_stable = np.zeros(t_steps)
pop_chaotic = np.zeros(t_steps)
pop_stable[0] = 0.05
pop_chaotic[0] = 0.05

#the discrete logistic map: x_{n+1} = r * x_n * (1 - x_n)
for i in range(1, t_steps):
    pop_stable[i] = r_stable * pop_stable[i-1] * (1 - pop_stable[i-1])
    pop_chaotic[i] = r_chaotic * pop_chaotic[i-1] * (1 - pop_chaotic[i-1])

plt.figure(figsize=(10, 5))
plt.plot(t, pop_stable, 'b-o', label=f'Stable (r = {r_stable})', alpha=0.7)
plt.plot(t, pop_chaotic, 'r-x', label=f'Chaotic (r = {r_chaotic})', alpha=0.7)

plt.title('Discrete Logistic Growth: Stable vs Chaotic Population Fate', fontsize=14)
plt.xlabel('Time Step / Generation (n)', fontsize=12)
plt.ylabel('Population Ratio (x)', fontsize=12)
plt.legend(loc='upper right')
plt.grid(True, linestyle=':', alpha=0.7)
plt.savefig('logistic_chaos_timeseries.png', dpi=300, bbox_inches='tight')
plt.close()
print("Saved 'logistic_chaos_timeseries.png'")

# ==========================================
# BIFURCATION DIAGRAM (Onset of Chaos)
# ==========================================
n_points = 10000
r_values = np.linspace(2.5, 4.0, n_points)
iterations = 1000
last_points = 100  # Only plot the last 100 points to see where it settles

# Initialize x with a tiny starting population
x = 1e-5 * np.ones(n_points)

plt.figure(figsize=(10, 6))

for i in range(iterations):
    x = r_values * x * (1 - x)
    # Plot only after the system has stabilized
    if i >= (iterations - last_points):
        plt.plot(r_values, x, ',k', alpha=0.25)

plt.xlim(2.5, 4.0)
plt.title("Bifurcation Diagram: Finding the Edge of Chaos", fontsize=14)
plt.xlabel("Growth Rate (r)", fontsize=12)
plt.ylabel("Steady-State Population Ratio (x)", fontsize=12)

onset_of_chaos = 3.56995
plt.axvline(x=onset_of_chaos, color='red', linestyle='--', label=f'Onset of Chaos (r ≈ {onset_of_chaos})')
plt.legend(loc='upper left')
plt.savefig('chaos_bifurcation.png', dpi=300, bbox_inches='tight')
plt.close()
print("Saved 'chaos_bifurcation.png'")