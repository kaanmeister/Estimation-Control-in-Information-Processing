import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42) # For reproducibility
t = np.linspace(0, 10, 150)
true_state = np.sin(t)
noise_std_dev = 0.4
noise = np.random.normal(0, noise_std_dev, size=true_state.shape)
noisy_observations = true_state + noise

def moving_average_estimator(observations, window_size):
    """
    Computes the moving average of a 1D array.
    Using np.convolve is an efficient way to apply this filter.
    """
    weights = np.ones(window_size) / window_size
    # 'valid' mode ensures we only compute averages where the window fully overlaps
    return np.convolve(observations, weights, mode='valid')

window_size = 7
estimated_state = moving_average_estimator(noisy_observations, window_size)

# Because we used mode='valid', the estimated state array is shorter.
# We need to adjust our time array to align with the estimated points.
t_estimated = t[window_size - 1:]

#plots
plt.figure(figsize=(10, 6))
plt.plot(t, true_state, label='True State', color='green', linewidth=2)
plt.scatter(t, noisy_observations, label='Noisy Observations', color='red', alpha=0.5, marker='x')

plt.plot(t_estimated, estimated_state, label=f'Estimated State (Window={window_size})', color='blue', linewidth=2.5)

plt.title('Moving Average Estimator')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

plt.savefig('moving_average_est.png')