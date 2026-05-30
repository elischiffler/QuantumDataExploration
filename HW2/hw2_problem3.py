# -- Created With AI --

import numpy as np

# Problem 3: Calculate Bohr radius in Angstroms.

# Constants
hbar = 1.055e-34 
m_e = 9.11e-31       
e = 1.602e-19
epsilon_0 = 8.854e-12

# The Bohr radius formula is: a_0 = (4 * pi * epsilon_0 * hbar^2) / (m_e * e^2)
numerator = 4 * np.pi * epsilon_0 * (hbar**2)
denominator = m_e * (e**2)

a_0_meters = numerator / denominator

# Convert meters to Angstroms (1 Angstrom = 10^-10 meters)
a_0_angstroms = a_0_meters * 1e10

# Output
print("--- Problem 3: Bohr Radius Calculation ---")
print(f"Calculated Bohr Radius (a_0) in meters: {a_0_meters:.4e} m")
print(f"Calculated Bohr Radius (a_0) in Angstroms: {a_0_angstroms:.4f} Å")