import numpy as np
import matplotlib.pyplot as plt

# Define the experiment function
def experiment1(num_samples, true_mean, true_std):
    # Generating
    samples = np.random.normal(true_mean, true_std, num_samples)
    
    sample_mean = np.mean(samples)
    sample_std = np.std(samples)
    
    return samples, sample_mean, sample_std

# Parameters
num_samples = 500
true_mean = 10
true_std = 2

# experiment
samples, sample_mean, sample_std = experiment1(num_samples, true_mean, true_std)

# results
print("True mean:", true_mean)
print("True standard deviation:", true_std)
print("Sample mean:", sample_mean)
print("Sample standard deviation:", sample_std)

#  histogram 
plt.hist(samples, bins=30, density=True, alpha=0.5, color='b')
plt.xlabel('Value')
plt.ylabel('Probability')
plt.title('Histogram of Samples')
plt.grid(True)
plt.show()


