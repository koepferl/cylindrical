import numpy as np
import matplotlib.pyplot as plt

from hyperion.model import ModelOutput
from hyperion.util.constants import pc, au

# Read in the model
m = ModelOutput('test_disc.rtout')

# Extract the quantities
g = m.get_quantities()

# Get the wall positions for r and z
rw, zw = g.w_wall / au, g.z_wall / au

print rw, zw

# Make a 2-d grid of the wall positions (used by pcolormesh)
R, Z = np.meshgrid(rw, zw)

# Make a plot in (r, theta) space
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
c = ax.pcolormesh(R, Z, g['temperature'][0].array[0, :, :],vmin=0, vmax=100)
ax.set_xscale('log')
ax.set_xlim(rw[1], rw[-1])
ax.set_ylim(zw[0], zw[-1])
ax.set_xlabel('r (au)')
ax.set_ylabel('z (au)')
ax.set_yticks([-300, -200, -100, 0, 100, 200, 300])
ax.set_yticklabels(['-300', '-200','-100','0', '100', '200','300'])
cb = fig.colorbar(c)
cb.set_label('Temperature (K)')
fig.savefig('temperature_spherical_rt.png', bbox_inches='tight')

# Calculate the position of the cell walls in cartesian coordinates
#R, T = np.meshgrid(rw, tw)
#X, Z = R * np.sin(T), R * np.cos(T)
X=R

# Make a plot in (x, z) space for different zooms
fig = plt.figure(figsize=(16, 8))

ax = fig.add_axes([0.1, 0.1, 0.2, 0.8])
c = ax.pcolormesh(X, Z, g['temperature'][0].array[0, :, :],vmin=0, vmax=100)
ax.set_xlim(X.min(), X.max())
ax.set_ylim(Z.min(), Z.max())
ax.set_xlabel('x (au)')
ax.set_ylabel('z (au)')

ax = fig.add_axes([0.32, 0.1, 0.2, 0.8])
c = ax.pcolormesh(X, Z, g['temperature'][0].array[0, :, :],vmin=0, vmax=100)
ax.set_xlim(X.min() / 10., X.max() / 10.)
ax.set_ylim(Z.min() / 10., Z.max() / 10.)
ax.set_xlabel('x (au)')
ax.set_yticklabels('')
ax.text(0.1, 0.95, 'Zoom 10x', ha='left', va='center', transform=ax.transAxes, color='white')

ax = fig.add_axes([0.54, 0.1, 0.2, 0.8])
c = ax.pcolormesh(X, Z, g['temperature'][0].array[0, :, :],vmin=0, vmax=100)
ax.set_xlim(X.min() / 100., X.max() / 100)
ax.set_ylim(Z.min() / 100, Z.max() / 100)
ax.set_xlabel('x (au)')
ax.set_yticklabels('')
ax.text(0.1, 0.95, 'Zoom 100x', ha='left', va='center', transform=ax.transAxes, color='white')

ax = fig.add_axes([0.75, 0.1, 0.03, 0.8])
cb = fig.colorbar(c, cax=ax)
cb.set_label('Temperature (K)')

fig.savefig('temperature_spherical_xz.png', bbox_inches='tight')