import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(5.12, 5.12))
plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
ax = fig.add_subplot(111, aspect=1)

### パラメータ ##########
top = 5./7.*np.pi
bottom = -np.pi/2.*1.2
nose = [ -0.75, 0.15 ]
amp = 0.12
color = "#bb6655"
#########################

def hedgehog(theta):
    r = 0.
    for n in range(1, 32):
        r -= amp*np.sin(n*(theta - 1.2*top)) / n**(1./4.)
    return r

### 背中 ###
theta = np.linspace(bottom, top, 256)
r = 0.5 + hedgehog(theta)

head = [ (r*np.cos(theta))[-1], (r*np.sin(theta))[-1] ]
tail = [ (r*np.cos(theta))[0], (r*np.sin(theta))[0] ]

# ax.plot( r*np.cos(theta), r*np.sin(theta), c=color )
X = r*np.cos(theta)
Y = r*np.sin(theta)

### 頭 ###
x = np.linspace(nose[0], head[0], 32)
fnose = lambda x: ((x - nose[0])/(head[0] - nose[0]))**2
y = fnose(x) * (head[1]*0.9 - nose[1]) + nose[1]
# ax.plot( x, y, c=color)
X = np.concatenate([X, x[1:][::-1]])
Y = np.concatenate([Y, y[1:][::-1]])


### お腹 ###
x = np.linspace(nose[0], tail[0], 32)
y = nose[1] + ((x - nose[0])/(tail[0] - nose[0]))**3 * (tail[1] - nose[1])
# ax.plot( x, y, c=color )

X = np.concatenate([X, x[1:]]) 
Y = np.concatenate([Y, y[1:]]) 

ax.fill(X, Y, fc=color)
#ax.fill(FX, FY, fc="white", ec=color)
#ax.plot( FX, FY)

### 鼻 ###
ax.plot( x[1], y[1], "o", c=color, markersize=4)

### 目 ###
ax.plot( -0.45, 0.3, "o", c="white", markersize=10)

### 足 ###
ax.plot( -0.365, -0.01, "o", c=color, markersize=15)

### 背中のライン ###
end = [x[24], y[24]]
x = np.linspace(head[0], end[0])
y = head[1]*0.9 + ((x - head[0])/(end[0] - head[0]))**5 * (end[1] - head[1]*0.9)
ax.plot( x, y, c="white", lw=4)


lim = 0.68
ax.set_xlim([-lim - 0.1, +lim - 0.1])
ax.set_ylim([-lim + 0.1, +lim + 0.1])
# ax.grid()

ax.patch.set_alpha(0.)

plt.savefig("./static/favicon.svg", transparent=True)
plt.show()
plt.close()
