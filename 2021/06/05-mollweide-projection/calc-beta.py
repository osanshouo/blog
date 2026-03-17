import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Latin Modern Math"
plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["font.size"] = 14
labelsize = 16

fig = plt.figure( figsize=(6, 9) )
plt.subplots_adjust(left=0.14, right=0.86, bottom=0.07, top=0.96)
ax = [fig.add_subplot(211), fig.add_subplot(212)]
for a in ax:
    a.grid()
    a.set_xlabel(r"latitude $\theta$", fontsize=labelsize)
    a.set_xlim([0, np.pi/2.])
    a.set_xticks(np.linspace(0, np.pi/2., 5))
    a.set_xticklabels(["$0$", r"$\pi/8$", r"$\pi/4$", r"$3\pi/8$", r"$\pi/2$"])


n = 1024
theta = np.linspace(0, np.pi/2., n)[:-1]

def error(beta):
    return np.abs( 2.*beta + np.sin(2.*beta) - np.pi*np.sin(theta) )

def beta_exact(theta):
    exact = theta
    for i in range(128):
        exact = exact - (2.*exact + np.sin(2.*exact) - np.pi*np.sin(theta))/(2. + 2.*np.cos(2.*exact))
    return exact
exact = beta_exact(theta)

def mollweide_scalar(theta, err=1e-5):
    if np.abs(2.*theta) == np.pi:
        return theta

    beta = theta
    while np.abs( 2.*beta + np.sin(2.*beta) - np.pi*np.sin(theta) ) > err:
        beta -= (2.*beta + np.sin(2.*beta) - np.pi*np.sin(theta))/(2. + 2.*np.cos(2.*beta))
    return beta

mollweide = np.vectorize(mollweide_scalar)

beta = theta
for i in range(9):
    ax[0].plot(theta, beta, lw=1, label="i={}".format(i))
    ax[1].plot(theta, error(beta), lw=1, label="i={}".format(i))
    #ax[1].plot(theta, np.abs(beta - exact), lw=1, label="i={}".format(i))
    beta = beta - (2.*beta + np.sin(2.*beta) - np.pi*np.sin(theta))/(2. + 2.*np.cos(2.*beta))
ax[0].plot(theta, mollweide(theta), c="black", ls=":")
ax[1].plot(theta, error(mollweide(theta)), c="black", ls=":")
#ax[1].plot(theta, np.abs(mollweide(theta) - exact), c="black", ls=":")

for a in ax:
    a.legend()
ax[0].set_ylim([0, np.pi/2.])
ax[0].set_yticks(np.linspace(0, np.pi/2., 5))
ax[0].set_yticklabels(["$0$", r"$\pi/8$", r"$\pi/4$", r"$3\pi/8$", r"$\pi/2$"])
ax[0].set_ylabel(r"$\beta$", fontsize=labelsize)
ax[1].set_yscale("log")
ax[1].set_ylim([1e-7, 1])
ax[1].set_ylabel("error", fontsize=labelsize)

# ax[0].plot(theta, np.pi*theta/4)
# ax[0].plot(theta, np.pi/2. - np.cbrt(8./3.*(np.pi/2. - theta)**2))

#plt.show()
plt.savefig("./content/2021/06/05-mollweide-projection/calc-beta.svg")
plt.close()
