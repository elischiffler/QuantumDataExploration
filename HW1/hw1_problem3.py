#  -- Created with AI -- 

import numpy as np
import matplotlib.pyplot as plt

# Constants
hbar = 1.055e-34
m_e = 9.11e-31    
eV_to_J = 1.602e-19
a = 0.5        
U0 = 10.0       

# Calculate the kinetic energy coefficient (hbar^2 / 2m) in eV * nm^2
const = (hbar**2) / (2 * m_e) / eV_to_J * 1e18

# Set up the spatial grid (from -2 nm to 2 nm to see outside the well)
N = 1000
L_max = 2.0  
x = np.linspace(-L_max, L_max, N)
dx = x[1] - x[0]

# Define the potential V(x)
V = np.where(np.abs(x) < a, -U0, 0.0)

# Construct the Hamiltonian matrix (H = T + V) using finite difference
H = np.zeros((N, N))
for i in range(N):
    H[i, i] = const * (2.0 / dx**2) + V[i]
    if i > 0:
        H[i, i-1] = -const / dx**2
    if i < N - 1:
        H[i, i+1] = -const / dx**2

# Solve for eigenvalues and eigenvectors
energies, wavefunctions = np.linalg.eigh(H)

# Extract and properly normalize the first two bound states
E1, E2 = energies[0], energies[1]
psi1 = wavefunctions[:, 0] / np.sqrt(dx)
psi2 = wavefunctions[:, 1] / np.sqrt(dx)

print(f"First bound-state energy: {E1:.4f} eV")
print(f"Second bound-state energy: {E2:.4f} eV")

# Plotting Wave functions and Probability Densities
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

# 1. Wave functions
ax1.plot(x, psi1, label=rf"$\psi_1(x)$ (E1 = {E1:.2f} eV)")
ax1.plot(x, psi2, label=rf"$\psi_2(x)$ (E2 = {E2:.2f} eV)")
ax1.axvline(-a, color='gray', linestyle='--', label='Well Boundaries')
ax1.axvline(a, color='gray', linestyle='--')
ax1.axhline(0, color='black', linewidth=0.8)
ax1.set_title("Finite Well Wave Functions")
ax1.set_ylabel(r"$\psi(x)$")
ax1.legend()
ax1.grid(True)

# 2. Probability Densities
ax2.plot(x, np.abs(psi1)**2, label=r"$|\psi_1(x)|^2$")
ax2.plot(x, np.abs(psi2)**2, label=r"$|\psi_2(x)|^2$")
ax2.axvline(-a, color='gray', linestyle='--')
ax2.axvline(a, color='gray', linestyle='--')
ax2.set_title("Finite Well Probability Densities")
ax2.set_xlabel("Position x (nm)")
ax2.set_ylabel(r"$|\psi(x)|^2$")
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.savefig('HW1/problem3_finite_well_states.png', dpi=300)
