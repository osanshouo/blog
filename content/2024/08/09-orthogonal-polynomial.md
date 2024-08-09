+++
title = "[SymPy] 直交多項式"
date = 2024-08-09
[taxonomies]
tags = [ "数学", "SymPy", ]
+++

SymPy で直交多項式系を生成してグラフにプロットするコード例です.
単に Gram-Schmidt 法で多項式系
$$1, \ \ x, \ \ x^2 , \ \ x^3 , \ \ \cdots$$
を内積
$$\braket{ f, g } = \int_I f(x) g(x) w(x) dx$$
に関して正規直交化しているだけです.
コードの冒頭で重み関数 `w` と定義域 `I`, それから生成する次数の上限 `N` を指定します
($\phi_0(x)$ から $\phi_{N-1}(x)$ までを生成します).
このコードの場合は Hermite 多項式に関するものです.

グラフを生成する部分では最初にプロットする範囲 `xmax`, `xmin`, `ymax` を手で指定しています.
また SymPy の多項式を [Lambdify](https://docs.sympy.org/latest/modules/utilities/lambdify.html) 
を通じて NumPy array を処理できる関数に変換しています.


```python
from sympy import symbols, integrate, exp, oo, sqrt, simplify, lambdify
import numpy as np
import matplotlib.pyplot as plt


N = 6
x = symbols("x")


w = exp(-x*x)
I = [ -oo, oo ]

def braket(f, g):
    return integrate( f*g*w, (x, I[0], I[1]) )

phi = [ 1 ]
phi[0] = phi[0] / sqrt(braket(phi[0], phi[0]))

for n in range(1, N):
    pn = x**n
    for k in range(n):
        pn = pn - braket(x**n, phi[k])*phi[k]
    pn = simplify(pn)
    pn = pn / sqrt(braket(pn, pn))
    phi.append(pn)



# グラフのプロット
xmax = 3
ymax = 2.5
xmin = - xmax
X = np.linspace(xmin, xmax, 128)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(X, phi[0]*np.ones(len(X)))
for i in range(1,N):
    pn = phi[i]
    print("p[{}] = ".format(i), pn)
    
    pn = lambdify(x, pn, "numpy")

    ax.plot(X, pn(X))


ax.set_xlim([xmin, xmax])
ax.set_ylim([-ymax, ymax])
ax.set_aspect('equal')
ax.grid(ls="dotted")
ax.axvline(x=0, c="black", lw=0.5)
ax.axhline(y=0, c="black", lw=0.5)
plt.show()
plt.close()
```    


