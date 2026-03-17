import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "DejaVu Serif"
plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["font.size"] = 12

from scipy.special import ellipk, ellipe

fig = plt.figure( figsize=(6,6) )
ax = fig.add_subplot(111, aspect=1)

ax.grid()

lim = 4
r = np.linspace(-lim, lim, 16)
z = np.linspace(-lim, lim, 16)
R, z = np.meshgrid(r, z)
r = np.abs(r)

Delta2 = (r - 1.)*(r - 1.) + z*z
m = - 4.*r/Delta2
Br = z*((1. + r*r + z*z)*ellipe(m) - ((r + 1.)*(r + 1.) + z*z)*ellipk(m))/R/np.sqrt((r - 1.)*(r - 1.) + z*z)/((r + 1.)*(r + 1.) + z*z)
Bz = ((1. - r*r - z*z) * ellipe(m) + ((r + 1.)*(r + 1.) + z*z)*ellipk(m))/np.sqrt((r - 1.)*(r - 1.) + z*z)/((r + 1.)*(r + 1.) + z*z)
B = np.sqrt(Br*Br + Bz*Bz)

ax.quiver(R, z, Br/B, Bz/B, np.log10(B), cmap="cividis_r")

ax.plot( [1, -1], [0, 0], "o", c="black", markersize=8)
ax.plot( [1, -1], [0, 0], ".", c="white", markersize=8)
ax.plot( [+1], [0], "x", c="black", markersize=4)
ax.plot( [-1], [0], ".", c="black", markersize=4)

ax.set_xlabel("$x/a$", fontsize=24)
ax.set_ylabel("$z/a$", fontsize=24)

plt.savefig("./content/2021/02/20-circular-current/magnetic-field.svg")
plt.show()
plt.close()
