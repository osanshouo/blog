+++
title = "平面の線型変換と複素数の線型変換"
date = 2024-08-22
[extra]
toc = true
[taxonomies]
tags = [ "数学", "線型代数", "複素解析", ]
+++

2次元平面 $\mathbb{R}^2$ は複素平面 $\mathbb{C}$ と等価です. 従って平面の線型変換
$$\begin{pmatrix} x \\\\ y \end{pmatrix} \mapsto A \begin{pmatrix} x \\\\ y \end{pmatrix} = \begin{pmatrix} ax+by \\\\ cx+dy \end{pmatrix}$$
は複素数 $z \in \mathbb{Z}$ の変換に焼き直すことができるはずです.


# 線型変換の一般形

実行列 $A = \begin{pmatrix} a & b \\\\ c & d \end{pmatrix}$ が表す線型変換について考えます.
点 $\begin{pmatrix} x \\\\ y \end{pmatrix} \in \mathbb{R}^2$ と複素数 $z = x + i y$ を同一視すると, 変換 $A$ は複素数 $z$ に対する変換とみなせて
$$Az = a x + b y + i ( c x + d y )$$
を与えます. $x = \frac12 ( z + z^* )$, $y = \frac{1}{2i} ( z - z^* )$ を代入すると
$$Az = \frac{ a -i b + i c + d }{ 2 } z + \frac{ a + i b + i c - d }{ 2 } z^\*$$
です. そこで
$$\alpha = \frac{ a + d - i ( b - c ) }{ 2 } , \ \ \beta = \frac{ a - d + i ( b + c ) }{ 2 }$$
とおけば
$$Az = \alpha z + \beta z^*$$
とまとめられます. これは4つの実数 $a$, $b$, $c$, $d$ がふたつの複素数 $\alpha$, $\beta$ に集約できるということを示しています.
このような複素数の線型変換の全体を $\mathbb{F}$ と書くことにしましょう. これは集合として $\mathbb{C}^2$ と等価です.

変換 $f, g \in \mathbb{F}$ の和 $f+g$ およびスカラー倍 $\lambda f$ ($\lambda \in \mathbb{C}$) を
$$(f+g) (z) = f(z) + g(z)$$
$$(\lambda f) (z) = \lambda \cdot f(z)$$
により定めれば, $\mathbb{F}$ は複素ベクトル空間になります. 
これは実平面 $\mathbb{R}^2$ の線型変換の全体 $\mathbb{M}_2(\mathbb{R})$ が実ベクトル空間であったことに対応します.
上で述べたことから, 恒等変換 $1: z \mapsto z$ および複素共役 $\sigma: z \mapsto  z^*$ は$\mathbb{F}$ の基底をなします.


# 変換の合成

複素数の線型変換 $A_{\alpha, \beta}: z \mapsto \alpha z + \beta z^\*$,
$A_{\mu, \nu} : z \mapsto \mu z + \nu z^\*$ の合成変換 $A_{\mu, \nu} A_{\alpha, \beta}$ は
$$A_{\mu, \nu} A_{\alpha, \beta} z = ( \mu \alpha + \nu \beta^* ) z + ( \mu \beta + \nu \alpha^* ) z^*$$
と書けますから, これは変換 $A_{\mu \alpha + \nu \beta^\* , \mu \beta + \nu \alpha^\*}$ に一致します. 
特に変換 $A_{\alpha, \beta}$ と複素共役 $\sigma = A_{0, 1}$ との合成は
$$\sigma A_{\alpha, \beta} = A_{\beta^\*, \alpha^\*}$$
$$A_{\alpha, \beta} \sigma = A_{\beta, \mu}$$
です. また実数倍 $r = A_{r, 0}$ ($r \in \mathbb{R}$) との合成については
$$A_{r,0} A_{\alpha,\beta} = A_{\alpha,\beta} A_{r,0} = A_{r \alpha, r \beta}$$
であり任意の変換 $A_{\alpha,\beta}$ と可換です (これはそもそも実線型変換を考えていたことの帰結です).


# 可逆な変換

行列 $A = \begin{pmatrix} a & b \\\\ c & d \end{pmatrix}$ が表す線型変換が可逆であるかは, その行列式
$$\mathrm{det} A = a d - b c$$
がゼロであるかによって判定できます. $\alpha$, $\beta$ の定義から
$$\alpha + \beta = a + i c , \ \ \alpha - \beta = d - i b$$
であることを用いると
$$(\alpha + \beta)(\alpha - \beta)^* = ad - bc + i ( ab + c d )$$
ですから, 左辺の実部が行列式 $\mathrm{det} A$ に一致します. 左辺を展開すると
$$(\alpha + \beta)(\alpha - \beta)^* = | \alpha |^2 + | \beta |^2 + \alpha^* \beta - \alpha \beta^*$$
となりますが, 右辺第3項および第4項は複素共役の関係にある2数の差ですから純虚数です. よって
$$\mathrm{det} A = | \alpha |^2 - | \beta |^2$$
という結論を得ます.


# 回転行列と相似変換

平面の (鏡映を許さない) 回転を表す行列の一般形は, $\theta$ を回転角として
$$R_\theta = \begin{pmatrix}
    \cos \theta & - \sin \theta \\\\
    \sin \theta & \cos \theta
\end{pmatrix}$$
です. この行列に対応する複素数の変換は $\alpha = e^{i \theta}$, $\beta = 0$, つまり
$$z \mapsto e^{i \theta} z$$
です. 

もう少し条件を緩くして, 任意のふたつのベクトルがなす角が不変であるような線型変換 $A$ はどのようなものでしょうか.
このとき, ふたつの直交するベクトル $\begin{pmatrix} x \\\\ y \end{pmatrix}$, $\begin{pmatrix} y \\\\ -x \end{pmatrix}$ は変換後も直交しなければならないので
$$\begin{pmatrix} ax + by \\\\ cx + dy \end{pmatrix} \cdot \begin{pmatrix} ay - bx \\\\ cy - dx \end{pmatrix} = 0$$
です. 整理すると
$$( a^2 - b^2 + c^2 - d^2 ) xy + ( ab + cd ) ( y^2 - x^2 ) = 0$$
が得られますから, これが $x$, $y$ について恒等的に成り立つためには
$$a^2 + c^2 = b^2 + d^2$$
$$ab + cd = 0$$
が成り立つ必要があります. $a^2 + c^2 = k$ とおくと
$$a = k \cos \theta , \ \ c = k \sin \theta , \ \ b = - k \sin \phi , \ \ d = k \cos \phi$$
と表示できます. これを第2式に代入すると
$$k^2 \sin ( \theta - \phi ) = 0$$
が導かれるので, 結局 $k = 0$, $\phi = \theta$, $\phi = \theta + \pi$ のいずれかが成立します.
$k = 0$ はゼロ写像 $z \mapsto 0$ を表し, 残る $\phi = \theta$ または $\phi = \theta + \pi$ については,
前者は回転行列 $R_\theta$ にスケール変換 $\begin{pmatrix} k & \\\\ & k \end{pmatrix}$ を乗じたもの, 
後者はそこにさらに鏡映 $\begin{pmatrix} 1 & \\\\ & -1 \end{pmatrix}$ を乗じたものです.
複素数の変換の観点では, 結局, このような変換は実数倍 $k$, 回転 $e^{i \theta}$, 複素共役 $\sigma$ の合成変換だということになります.
