+++
title = "Levi-Civita記号と逆行列"
date = 2021-06-22
[extra]
toc = true
[taxonomies]
tags = ["数学", "線型代数", "SymPy", ]
+++

Levi-Civita 記号を用いると, 行列式や逆行列を陽に表示することができます.
$\mathcal{O} ( n! )$ の計算時間が必要なので数値的にはあまり有用ではないのですが, 解析的な計算にこの表式が必要になることがあります.

本記事では $n$ 次元空間を扱い, 添え字 $i$, $j$, ... は 1 から $n$ を走るものとします.
また, 重複添え字については和を取る [Einstein の規約](https://ja.wikipedia.org/wiki/%E3%82%A2%E3%82%A4%E3%83%B3%E3%82%B7%E3%83%A5%E3%82%BF%E3%82%A4%E3%83%B3%E3%81%AE%E7%B8%AE%E7%B4%84%E8%A8%98%E6%B3%95)
を採用します.


# Levi-Civita 記号

Levi-Civita 記号$\epsilon_{i j \cdots k}$ を, 添え字 $i$, $j$, ..., $k$ が 1, 2, ..., $n$ の偶置換ならば $+1$, 
奇置換ならば $-1$, それ以外ならば $0$ を表す記号として定義します.


# 行列式

本節の目標は, 任意の $n$ 次正方行列 $A$ について, その行列式 $\mathrm{det} ( A )$ は
$$\epsilon_{i j \cdots k} \mathrm{det} ( A ) = \epsilon_{p q \cdots r} A_{i p} A_{j q} \cdots A_{k r} \tag{1}$$
$$\mathrm{det} ( A ) = \frac{ 1 }{ n! } \epsilon_{i j \cdots k} \epsilon_{p q \cdots r} A_{i p} A_{j q} \cdots A_{k r} \tag{2}$$
を満足することを証明することです. 第1式が証明できれば, 第2式は第1式の両辺に $\epsilon_{i j \cdots k}$ を作用させて
$$\epsilon_{i j \cdots k} \epsilon_{i j \cdots k} = n!$$
(これは 1, 2, ..., $n$ の並び替えが $n!$ 個あることと等価です) を用いて整理しただけなのでただちに従います. 

第1式の右辺は $i$, $j$, ..., $k$ について完全反対称ですから, これは Levi-Civita 記号 $\epsilon_{i j \cdots, k}$ に比例します
(外積代数の一般論から, $n$ 次元ベクトル空間 $V$ の $n$ 次の外積 $\bigwedge^n V$ は1次元ベクトル空間です).
従って問題はその比例係数を求めることですが, $i=1$, $j=2$, ..., $k=n$ のとき, 右辺は行列式の定義 
([Leibniz の公式](https://ja.wikipedia.org/wiki/%E8%A1%8C%E5%88%97%E5%BC%8F%E3%81%AB%E5%AF%BE%E3%81%99%E3%82%8B%E3%83%A9%E3%82%A4%E3%83%97%E3%83%8B%E3%83%83%E3%83%84%E3%81%AE%E6%98%8E%E7%A4%BA%E5%85%AC%E5%BC%8F)) 
そのものです.


# 逆行列

行列 $A$ の行列式 $\mathrm{det} ( A )$ について, それが行列 $A$ の $n^2$ 個の成分 $A_{i j}$ の関数であることに注意して, 
変分 $A + \delta A$ に関する行列式を計算します. 行列式の性質から
$$\mathrm{det} ( A + \delta A ) = \mathrm{det} A ( I + A^{-1} \delta A ) = \mathrm{det} ( A ) \mathrm{det} ( I + A^{-1} \delta A)$$
となりますが, 
$$\mathrm{det} ( I + A^{-1} \delta A ) = \mathrm{tr} ( A^{-1} \delta A ) + \mathcal{O} ( \delta A^2 )$$
により
$$\mathrm{det} ( A + \delta A ) = \mathrm{det} ( A ) \mathrm{tr} ( B \delta A )$$
が従います. 特に $\delta A$ を $e_{i j}$ に比例するように選べば
$$\frac{ \partial \mathrm{det} ( A ) }{ \partial A_{i j} } = \mathrm{det} ( A ) [ A^{-1} ]_{j i} \tag{*}$$
という等式が結論されます ($A^{-1}$ の添え字に注意してください).

前節の行列式の表式 (1) を $A_{i j}$ で微分します.
$$\frac{ \partial \mathrm{det} ( A ) }{ \partial A_{i j} } = \frac{ 1 }{ n! } \epsilon_{a b \cdots c} \epsilon_{p q \cdots r} \frac{ \partial }{ \partial A_{i j} } \left( A_{a p} A_{b q} \cdots A_{c r} \right)$$
右辺の微分が $A_{a p}$ を叩くと $\delta_{a i} \delta_{p j}$ となり, その項は全体としては
$$\frac{ 1 }{ n! } \epsilon_{i b \cdots c} \epsilon_{j q \cdots r} A_{b q} \cdots A_{c r}$$
となります. 一方, 微分が $A_{b q}$ を叩くと $\delta_{b i} \delta_{ q j}$ となりますが, この Kronecker デルタは Levi-Civita 記号にぶつけて消去し,
Levi-Civita 記号の残った添え字 $a$ を $b$ に, 添え字 $p$ を添え字 $q$ に書き直すと, 上と同一の項を与えます.
同様に $n$ 項すべてが同じ上の形に帰着されますから, 結局
$$\frac{ \partial \mathrm{det} ( A ) }{ \partial A_{i j} } = \frac{ 1 }{ (n - 1)! } \epsilon_{i b \cdots c} \epsilon_{j q \cdots r} A_{b q} \cdots A_{c r}$$
が結論されます. これを行列式の微分と逆行列の関係式 (*) に代入すると, 逆行列の陽な表式
$$\left[ A^{-1} \right]\_{j i} = \frac{ 1 }{ (n - 1)! \mathrm{det} ( A ) } \epsilon_{i b \cdots c} \epsilon_{j q \cdots r} A_{b q} \cdots A_{c r} \tag{3}$$
に到達します.


# SymPy

本記事の結果が正しいか SymPy で検証してみます (注: 最適化していないのでとてもとても遅いです).

```python
from operator import mul
from functools import reduce
from sympy import symbols, factorial, simplify, Matrix
from sympy.combinatorics import Permutation

def levicivita(p):
    '''添え字のリストを受け取り Levi-Civita 記号を計算する'''
    try:
        p = Permutation(p)
        return 1 if p.is_even else -1
    except:
        return 0

    
def matrix(n):
    '''一般の行列を生成'''
    a = []
    for i in range(n):
        ai = []
        for j in range(n):
            aij = symbols("a{}".format(n*i + j))
            ai.append(aij)
        a.append(ai)
    return Matrix(a)


def det(A, n):
    '''行列式を計算'''
    d = 0
    p = Permutation([i for i in range(n)])
    d += levicivita(p) * reduce(mul, [A[i, p.apply(i)] for i in range(n)], 1)

    while (p := p.next_lex()) is not None:
        d += levicivita(p) * reduce(mul, [A[i, p.apply(i)] for i in range(n)], 1)
        
    return d

def inverse(A, n):
    '''逆行列を計算'''
    d = det(A, n)
    f = 1/factorial(n-1)/d

    def loop_q(bij, b, i, j):
        q = Permutation([k for k in range(n)])
        if b.apply(0) == j and q.apply(0) == i:
            bij += levicivita(b) * levicivita(q) * reduce(mul, [A[b.apply(k), q.apply(k)] for k in range(1, n)], 1)
        while (q := q.next_lex()) is not None:
            if b.apply(0) == j and q.apply(0) == i:
                bij += levicivita(b) * levicivita(q) * reduce(mul, [A[b.apply(k), q.apply(k)] for k in range(1, n)], 1)
        return bij
    
    B = []
    for i in range(n):
        bi = []
        for j in range(n):
            bij = 0
            
            b = Permutation([i for i in range(n)])
            bij = loop_q(bij, b, i, j)
            while (b := b.next_lex()) is not None:
                bij = loop_q(bij, b, i, j)
            
            bi.append(f * bij)
        B.append(bi)
    return Matrix(B)
            

# テスト

### 次元を設定する ###
n = 4
######################

A = matrix(n)
assert det(A, n) == A.det()
B = inverse(A, n)
assert simplify(B * A) == Matrix.eye(n)
assert simplify(A * B) == Matrix.eye(n)
```
