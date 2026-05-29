#  -- Created with AI --

import numpy as np
import matplotlib.pyplot as plt

# constants
L = 1.0  # Width of the well in nm

# Define the normalized wave function
def psi(n, x, L):
    return np.sqrt(2 / L) * np.sin(n * np.pi * x / L)

# Generate an array of x values from 0 to L
x = np.linspace(0, L, 1000)

# Calculate wave functions for n=1, 2, 3
psi_1 = psi(1, x, L)
psi_2 = psi(2, x, L)
psi_3 = psi(3, x, L)

# Create a figure with two subplots stacked vertically
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

# 1. Plot the wave functions
ax1.plot(x, psi_1, label=r'$\psi_1(x)$ (n=1)')
ax1.plot(x, psi_2, label=r'$\psi_2(x)$ (n=2)')
ax1.plot(x, psi_3, label=r'$\psi_3(x)$ (n=3)')
ax1.set_title('Wave Functions for an Infinite Square Well')
ax1.set_xlabel('Position x (nm)')
ax1.set_ylabel(r'$\psi_n(x)$')
ax1.axhline(0, color='black', linewidth=0.8, linestyle='--')
ax1.legend()
ax1.grid(True)

# 2. Plot the probability densities
ax2.plot(x, np.abs(psi_1)**2, label=r'$|\psi_1(x)|^2$ (n=1)')
ax2.plot(x, np.abs(psi_2)**2, label=r'$|\psi_2(x)|^2$ (n=2)')
ax2.plot(x, np.abs(psi_3)**2, label=r'$|\psi_3(x)|^2$ (n=3)')
ax2.set_title('Probability Densities for an Infinite Square Well')
ax2.set_xlabel('Position x (nm)')
ax2.set_ylabel(r'$|\psi_n(x)|^2$')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.savefig('HW1/problem1_plots.pdf')
