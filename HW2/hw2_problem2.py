# -- Created With AI --

import numpy as np
import matplotlib.pyplot as plt

# Problem 2: Plot Coulomb Potential (U(r)) from r=0.01 nm to r=2 nm. Convert energy axis to eV.

# The constant for Coulomb potential
k_e2 = 1.44 

r = np.linspace(0.01, 2.0, 500)

# Calculate Coulomb Potential U(r) = -k*e^2 / r
U_r = -k_e2 / r

# Plot potential
plt.figure(figsize=(8, 6))
plt.plot(r, U_r, 'b-', label='U(r) = -1.44 / r')

plt.title("Hydrogen Atom Coulomb Potential")
plt.xlabel("Radius, r (nm)")
plt.ylabel("Potential Energy, U(r) (eV)")
plt.grid(True, alpha=0.6)
plt.axhline(0, color='black', linewidth=0.8)
plt.legend()
plt.savefig('HW2/hw2_problem2.png')