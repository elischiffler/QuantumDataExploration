# -- Created With AI --

import numpy as np
import matplotlib.pyplot as plt

# Problem 1: Calculate H energy levels for n=1, 2, 3, 4, 5, 6 in eV.

# energy levels of a Hydrogen atom are E_n = -13.6 eV / n^2
E1 = -13.6 # ground state
n_values = np.array([1, 2, 3, 4, 5, 6])

# Calculate the quantized energy levels
energy_levels = E1 / (n_values**2)

# Print the numerical calculations
print("Hydrogen Atom Energy Levels:")
for n, E in zip(n_values, energy_levels):
    print(f"n={n}: {E:.3f} eV")