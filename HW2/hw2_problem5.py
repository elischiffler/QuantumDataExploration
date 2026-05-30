# -- Created With AI --

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import sph_harm_y

# Problem 5: Use spherical harmonics to visualize s, p, and d orbitals.
# We will use 3D surface plots showing the probability density

# Create an angular grid
# theta: azimuthal angle
# phi: polar angle
theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(0, np.pi, 100)
theta, phi = np.meshgrid(theta, phi)

def plot_orbital(ax, l, m, title):
    """Calculates and plots the 3D surface of a spherical harmonic."""
    # Calculate the spherical harmonic
    Y = sph_harm_y(l, m, phi, theta)
    
    # Use probability density for the radius to show orbital lobes
    R = np.abs(Y)**2
    
    # Convert spherical to Cartesian coordinates for 3D plotting
    X = R * np.sin(phi) * np.cos(theta)
    Y_cart = R * np.sin(phi) * np.sin(theta)
    Z = R * np.cos(phi)
    
    # Plot the 3D surface
    ax.plot_surface(X, Y_cart, Z, cmap='viridis', edgecolor='none', alpha=0.8)
    
    # Formatting
    ax.set_title(title, pad=10)
    ax.set_box_aspect([1, 1, 1])
    ax.axis('off')

# Create a figure with 3 subplots for s, p, and d orbitals
fig = plt.figure(figsize=(15, 5))

# Plot l=0, m=0
plot_orbital(fig.add_subplot(131, projection='3d'), 0, 0, "s-orbital ($l=0, m=0$)")

# Plot l=1, m=0
plot_orbital(fig.add_subplot(132, projection='3d'), 1, 0, "$p_z$-orbital ($l=1, m=0$)")

# Plot l=2, m=0
plot_orbital(fig.add_subplot(133, projection='3d'), 2, 0, "$d_{z^2}$-orbital ($l=2, m=0$)")

plt.suptitle("Spherical Harmonics: s, p, and d Orbitals", fontsize=16)
plt.tight_layout()
plt.savefig('HW2/hw2_problem5.png')