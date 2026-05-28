#  -- Created with AI --

import numpy as np

# Constants
h = 6.626e-34     
hbar = 1.055e-34    
m_e = 9.11e-31      
eV_to_J = 1.602e-19 
c = 3.00e8         
L = 1.0e-9   

def calc_energy_joules(n):
    # Formula: E_n = (n^2 * pi^2 * hbar^2) / (2 * m * L^2)
    return (n**2 * np.pi**2 * hbar**2) / (2 * m_e * L**2)

# 1. Calculate the first three allowed energy levels in eV
print("--- First Three Allowed Energy Levels ---")
energies_joules = [calc_energy_joules(n) for n in [1, 2, 3]]
energies_eV = [e / eV_to_J for e in energies_joules]

for n, energy in zip([1, 2, 3], energies_eV):
    print(f"E_{n} = {energy:.4f} eV")

# 2. Determine the wavelength of the photon emitted during the transition n = 3 -> n = 1
print("\n--- Wavelength for Transition (n=3 -> n=1) ---")
delta_E_J = energies_joules[2] - energies_joules[0]

wavelength_m = (h * c) / delta_E_J
wavelength_nm = wavelength_m * 1e9 # meters -> nanometers

print(f"Wavelength (\u03BB) = {wavelength_nm:.2f} nm")