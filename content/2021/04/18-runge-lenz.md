+++
title = "[SymPy] Laplace-Runge-LenzベクトルのPoisson括弧"
date = 2021-04-18
[taxonomies]
tags = ["物理学", "天体力学", "解析力学", "SymPy"]
+++

Kepler 問題の Hamiltonian は次式により与えられます.
$$H = \frac{ \boldsymbol{p}^2 }{ 2 m } - \frac{ k }{ | \boldsymbol{r} | }$$
この系には Hamiltonian $H$, 角運動量 $\boldsymbol{L} = \boldsymbol{x} \times \boldsymbol{p}$ に加えて,
[Laplace-Runge-Lenz ベクトル](https://ja.wikipedia.org/wiki/%E3%83%AB%E3%83%B3%E3%82%B2%EF%BC%9D%E3%83%AC%E3%83%B3%E3%83%84%E3%83%99%E3%82%AF%E3%83%88%E3%83%AB)
として知られる運動の積分
$$\boldsymbol{A} = \boldsymbol{p} \times \boldsymbol{L} - m k \frac{ \boldsymbol{x} }{ | \boldsymbol{x} }$$
が存在します. 角運動量および Laplace-Runge-Lenz ベクトルの Poisson 括弧は
$$[ L_i, L_j ] = \epsilon_{i j k} L_k$$
$$[ L_i, A_j ] = \epsilon_{i j k} A_k$$
$$[ A_i, A_j ] = - 2 m H \epsilon_{i j k} L_k$$
を満足し, $\mathfrak{so}(4)$ (あるいは $\mathfrak{so} ( 3, 1 )$) との対応関係が見て取れます.
この Poisson 括弧を手計算でチェックすることはすこし面倒なのですが, SymPy を使えば数秒で終わります.


```python
from sympy import symbols, sqrt, simplify
from sympy.combinatorics.permutations import Permutation

x, y, z, u, v, w, m, k = symbols("x, y, z, u, v, w, m, k")

def pb(f, g):
    X = f.diff(x) * g.diff(u) - f.diff(u) * g.diff(x)
    Y = f.diff(y) * g.diff(v) - f.diff(v) * g.diff(y)
    Z = f.diff(z) * g.diff(w) - f.diff(w) * g.diff(z)
    return X + Y + Z

X = [ x, y, z ]
P = [ u, v, w ]

def dot(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def cross(a, b):
    return [
        a[1]*b[2] - a[2]*b[1],
        a[2]*b[0] - a[0]*b[2],
        a[0]*b[1] - a[1]*b[0],
    ]

def epsilon(i, j, k):
    if {i, j, k} != {0, 1, 2}:
        return 0
    elif Permutation([i, j, k]).is_even:
        return 1
    else:
        return -1

def hodge(i, j, a):
    return sum(list(epsilon(i,j,k)*a[k] for k in range(3)))

r = sqrt(x*x + y*y + z*z)
L = cross(X, P)

A = cross(P, L)
for i in range(3):
    A[i] = A[i] - m*k*X[i]/r

H = dot(P,P)/(2*m) - k/r


for i in range(3):
    assert simplify(pb(H, A[i])) == 0
    
    for j in range(3):
        rhs = -2*m*H*hodge(i, j, L)
        assert simplify(pb(A[i], A[j]) - rhs) == 0

        rhs = hodge(i, j, A)
        assert simplify(pb(L[i], A[j]) - rhs) == 0
```
