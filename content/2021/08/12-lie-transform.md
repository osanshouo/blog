+++
title = "[SymPy] Lie変換摂動論の方程式の導出"
date = 2021-08-12
[taxonomies]
tags = ["物理学", "解析力学", "SymPy", ]
+++

Lie 変換摂動論 (特に Hori (1966) の定式化) の基礎方程式は, Hamiltonian $H$ および Lie 変換の生成関数 $W$, 変換後の Hamiltonian $K$ に関する等式
$$K = \exp ( L_W ) H$$
です. $L_W$ は $W$ に関する Lie 微分 $L_W f = \\{ f, W \\}$ です (括弧は Poisson 括弧). ここで $H$, $W$, $K$ の摂動展開
$$H = H_0 + \epsilon H_1 + \epsilon^2 H_2 + \cdots$$
$$W = \epsilon W_1 + \epsilon^2 W_2 + \cdots$$
$$K = K_0 + \epsilon K_1 + \epsilon^2 K_2 + \cdots$$
を上式に代入し, $\epsilon$ のべきで整理することにより摂動が計算できます.

ただ右辺を $\epsilon$ のべきに展開するのは, 特に高次摂動が必要なときやや面倒です.
こういうことは SymPy でさくっと計算しましょう.
Poisson 括弧は SymPy には実装されていないようなのですが, 
量子力学の交換子 (`sympy.physics.quantum.commutator.Commutator`) で代用できます.

```python
'''Lie 変換摂動論で必要な摂動展開を計算する'''

from sympy.physics.quantum import Commutator, Operator
from sympy import symbols, factorial

# 計算する次数 #
Nmax = 5
################

e = symbols('e')
H = [Operator('H{}'.format(n)) for n in range(Nmax)]
K = [Operator('K{}'.format(n)) for n in range(Nmax)]
W = [Operator('W{}'.format(n)) for n in range(Nmax)]
W[0] = 0

def LieDeriv(W, f):
    return Commutator(f, W).expand(commutator=True)

def LieMap(W, f):
    s = 0
    for n in range(Nmax):
        e = f
        for i in range(n):
            e = LieDeriv(W, e)
        s = s + e.expand(commutator=True) / factorial(n)
    return s

def rhs_raw():
    return LieMap(
        sum(e**i * w for i, w in enumerate(W)),
        sum(e**i * w for i, w in enumerate(H)),
    ).expand(commutator=True)


rhs = rhs_raw()

for n in range(Nmax):
    print( 
        rhs.coeff(e, n)
    )
```

すくなくとも4次までは Hori (1966) に記述されているものと一致したので, おそらくこれで正しいと思います.
ただし処理がかなり遅いので注意してください.

# 参考文献
* G. Hori, _Theory of General Perturbation with Unspecified Canonical Variable_, Publications of the Astronomical Society of Japan, __18__, 287 (1966). bibcode:[1966PASJ...18..287H](https://ui.adsabs.harvard.edu/abs/1966PASJ...18..287H/abstract)
* Sylvio Ferraz-Mello, _Canonical Perturbation Theories_, Springer (2007). doi:[10.1007/978-0-387-38905-9](https:doi.org/10.1007/978-0-387-38905-9)
* [Commutator — SymPy 1.8 documentation](https://docs.sympy.org/latest/modules/physics/quantum/commutator.html)
