import numpy as np
from scipy.special import airy
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "DejaVu Serif"
plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["font.size"] = 14

### パラメータ ###
e = 1./128.
end = 24.
##################

t = np.arange(0, end*2.*np.pi, 1./32.)
z = - 1. / np.cbrt(e**2) * ( 1. + e*t )

def coeff(q0, p0):
    ai, aip, bi, bip = airy(z[0])
    return [
        + (bip * q0 + bi * p0 / np.cbrt(e)) * np.pi,
        - (aip * q0 + ai * p0 / np.cbrt(e)) * np.pi,
    ]

def solution(q0, p0):
    a, b = coeff(q0, p0)
    ai, aip, bi, bip = airy(z)
    return [
        a * ai + b * bi,
        - np.cbrt(e) * (a * aip + b * bip)
    ]

def hamiltonian(q, p):
    return p*p*0.5 + (1. + e*t)*q*q*0.5

fig = plt.figure(figsize=(8, 14))
plt.subplots_adjust(left=0.13, right=0.87, bottom=0.07, top=0.95)
ax = [
    fig.add_subplot(311),
    fig.add_subplot(312),
    fig.add_subplot(313),
]

q, p = solution(1., 0.)
ax[0].plot( t/2./np.pi, q, ls="-", )
ax[1].plot( t/2./np.pi, p, ls="-", )
h = hamiltonian(q, p)
ax[2].plot( t/2./np.pi, h, ls="-")
ax[2].plot( t/2./np.pi, h/np.sqrt(1. + e*t), ls="-")

q, p = solution(0., 1.)
ax[0].plot( t/2./np.pi, q, ls=":", )
ax[1].plot( t/2./np.pi, p, ls=":", )
h = hamiltonian(q, p)
ax[2].plot( t/2./np.pi, h, ls=":")
ax[2].plot( t/2./np.pi, h/np.sqrt(1. + e*t), ls=":")

for a in ax:
    a.set_xlim([0, end])
    a.set_xlabel("time $t / 2 \pi$")
    a.grid()
ax[0].set_ylabel("coordinate $q$")
ax[1].set_ylabel("momentum $p$")
ax[2].set_ylabel("Hamiltonian $H$")
ax2 = ax[2].twinx()
ax2.set_ylabel("action variable $I$")
ax2.set_yticks([])


plt.savefig("./content/2021/06/12-adiabatic-invariant/exact.svg")
#plt.show()
plt.close()
