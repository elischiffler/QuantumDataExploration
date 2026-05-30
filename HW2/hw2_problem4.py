# -- Created With AI --

import numpy as np
import matplotlib.pyplot as plt

# Problem 4: Plot H atom radial probability distributions for 1s, 2s, and 3s states.

# Create an array of r values from 0 to 25 a_0
r = np.linspace(0, 25, 1000)

# R_1s (ground state): peaks at r = a_0
R_1s = 2 * np.exp(-r)

# R_2s (excited state): one node
R_2s = (1 / np.sqrt(2)) * (1 - r/2) * np.exp(-r/2)

# R_3s (excited state): two nodes
R_3s = (2 / (3 * np.sqrt(3))) * (1 - 2*r/3 + 2*r**2/27) * np.exp(-r/3)

# Calculate radial probability distributions P(r) = r^2 * R(r)^2
P_1s = (r**2) * (R_1s**2)
P_2s = (r**2) * (R_2s**2)
P_3s = (r**2) * (R_3s**2)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(r, P_1s, label='1s state', color='blue')
plt.plot(r, P_2s, label='2s state', color='orange')
plt.plot(r, P_3s, label='3s state', color='green')

plt.title("Hydrogen Atom Radial Probability Distributions")
plt.xlabel("Radius, r ($a_0$)")
plt.ylabel("Probability Density, P(r) (unitless)")
plt.grid(True, alpha=0.6)
plt.legend()
plt.xlim(0, 25)
plt.savefig('HW2/hw2_problem4.png')