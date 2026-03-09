import numpy as np
import matplotlib.pyplot as plt

# Define parameters
r = 4.0
initial_populations = [0.1, 0.5, 1.0, 2.0]
iterations = 15

print("\n" + "="*60)
print(f" EXPERIMENT REPORT: DISCRETE LOGISTIC MAP (r = {r})")
print("="*60)

# Initialize plot
plt.figure(figsize=(10, 6))

for x0 in initial_populations:
    x = x0
    history = [x]
    
    # Run the logistic map equation: x_next = r * x * (1 - x)
    for i in range(1, iterations + 1):
        x = r * x * (1 - x)
        history.append(x)
        
    print(f"\n>>> EXPERIMENT 1: Initial Population Ratio (x0) = {x0}")
    print(f"First 4 generations: {[round(val, 4) for val in history[:4]]} ...")
    
    # Print the specific observation for each case
    if x0 == 0.1:
        print("OBSERVATION: The population survives but enters a state of completely deterministic chaos. It fluctuates wildly between 0 and 1 without ever settling into a repeating sequence.")
    elif x0 == 0.5:
        print("OBSERVATION: The population instantly multiplies to the absolute maximum carrying capacity (1.0) in the very first generation. Because the environment is completely exhausted, the population crashes to exactly 0 (extinction) in the second generation.")
    elif x0 == 1.0:
        print("OBSERVATION: The population starts already at the maximum carrying capacity. With no room for growth and maximum environmental pressure, it immediately crashes to 0 (extinction) in the very next generation.")
    elif x0 == 2.0:
        print("OBSERVATION: Starting at double the carrying capacity breaks the physical logic of the model (a ratio > 1.0). The mathematics rapidly diverge to negative infinity. Biologically, this represents an instant, catastrophic collapse due to massive overpopulation.")
        
    # For plotting x0=2.0, we clamp the negative infinity values so it doesn't ruin the graph scale
    if x0 == 2.0:
        plot_history = [max(min(val, 1.2), -0.2) for val in history]
        plt.plot(range(iterations + 1), plot_history, '--', color='purple', label=f'x0 = {x0} (Diverges to -∞)')
    else:
        plt.plot(range(iterations + 1), history, '-o', label=f'x0 = {x0}')


plt.title(f'Logistic Map Experiments at Full Chaos (r = {r})', fontsize=14)
plt.xlabel('Generation (n)', fontsize=12)
plt.ylabel('Population Ratio (x)', fontsize=12)
plt.ylim(-0.25, 1.25)
plt.axhline(0, color='black', linewidth=1)
plt.axhline(1, color='red', linestyle=':', label='Carrying Capacity (1.0)')
plt.legend(loc='upper right')
plt.grid(True, linestyle=':', alpha=0.7)

output_file = 'r4_experiments.png'
plt.savefig(output_file, dpi=300, bbox_inches='tight')
plt.close()

print("\n" + "="*60)
print(f"[SUCCESS] Visual plot saved to your folder as '{output_file}'")
print("="*60 + "\n")