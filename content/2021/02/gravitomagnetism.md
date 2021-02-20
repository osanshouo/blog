+++
title = "重力磁気効果"
date = 2021-02-18
draft = true
[extra]
toc = true
[taxonomies]
tags = ["物理学", "重力"]
+++

1740年代末の Clairaut, Euler, d'Alembert による月の運動に関する論争の中で, 
d'Alembert は磁力のような作用が存在する可能性を検討していた.
Einstein の一般相対性理論によると実際にそのような作用は存在する.
歴史の妙.

# 静磁気学

話を簡単にするために本記事では静的な場に議論を限定する.
磁場 $\mathbf{B}$ は
$$\mathbf{\nabla} \cdot \mathbf{B} = 0$$
$$\mathbf{\nabla} \times \mathbf{B} = \mu_0 \mathbf{J}$$
を満足する. 第2式を閉曲線 $C$ により囲まれる任意の面 $S$ について面積分すると, Stokes の定理により,
Ampère の法則
$$\oint_C \mathbf{B} \cdot d\mathbf{r} = \mu_0 \int_S \mathbf{j} \cdot d\mathbf{S}$$
を得る.

実際の計算は $\mathbf{B} = \mathbf{\nabla} \times \mathbf{A}$ により定義されるベクトルポテンシャル $\mathbf{A}$
を用いる方が容易である. ゲージ条件 $\mathbf{\nabla} \cdot \mathbf{A} = 0$ のもとでは $\mathbf{A}$ は
$$\nabla^2 \mathbf{A} = \mu_0 \mathbf{j}$$
を満足する. 故に
$$\mathbf{A} \left( \mathbf{x} \right) = \frac{ \mu_0 }{ 4 \pi } \int \frac{ \mathbf{j} ( \mathbf{x}' ) }{ | \mathbf{x} - \mathbf{x}' | } d^3 x' .$$

## 直線電流

例として $z$ 軸上を正の向きに流れる線電流 $\mathbf{j} = I \delta(x) \delta(y) \mathbf{e}_z$ がつくる磁場 $\mathbf{B}$ について考える.

円柱座標 $( r, \theta, z )$ を用いるとき, 対称性から磁場 $\mathbf{B}$ は動径 $r$ だけに依存する.
そこで半径 $r$ の円 $C$ に Ampère の法則を適用すると $2 \pi r B_\theta = \mu_0 I$, すなわち
$$B_\theta = \frac{ \mu_0 I }{ 2 \pi r }$$
が結論される. また発散 $\mathbf{\nabla} \cdot \mathbf{B}$ は, $B_r$, $B_\theta$, $B_z$ が $r$ にしか依存しないことから
$$\mathbf{\nabla} \cdot \mathbf{B} = \frac{ 1 }{ r } \frac{ \partial }{ \partial r } ( r B_r )$$
と計算でき, これがゼロであることから $B_r$ は定数である. 
しかし無限遠 $r \to \infty$ で磁場はゼロにならなければならないから $B_r = 0$ が結論される.
最後に $B_z$ について, $(r, z)$-平面内の任意の閉曲線に Ampère の法則を適用することによりゼロであることが導かれる.
すなわち
$$\mathbf{B} = \frac{ \mu_0 I }{ 2 \pi r } \mathbf{e}_\theta$$
である.

## 円電流

次に $z = 0$ 平面内の半径 $a$ の円 $x^2 + y^2 = a^2$ 上を流れる電流 $\mathbf{j} = I \delta( r - a ) \delta ( z ) \mathbf{e}_\theta$ 
が同一平面上につくる磁場を求める.

対称性から点 $( x, 0, 0 )$ のベクトルポテンシャル $\mathbf{A} ( x )$ を求めれば十分であり, しかもそれは $y$ 軸に平行である.
この点と円電流上の点 $( a \cos \theta , a \sin \theta )$ の距離は
$$\sqrt{ ( x - a \cos \theta )^2 + a^2 \sin^2 \theta } = \sqrt{ x^2 + a^2 - 2 a \cos \theta }$$
により与えられる. 
電流の線素の表式
$$d\mathbf{r} = a \mathbf{e}_\theta d\theta$$
から, ベクトルポテンシャル

$$\mathbf{A} \left( x \right) = \frac{ \mu_0 I }{ 4 \pi } \int_0^{2 \pi} \frac{ a \mathbf{e}_\theta d\theta }{ | \mathbf{r} - \mathbf{r}' | }$$

の $y$ 成分は
$$A_y \left( x \right) = \frac{ \mu_0 }{ 4 \pi I } \int_0^{2 \pi} \frac{ a \cos \theta d\theta }{ \sqrt{ ( x - a \cos \theta )^2 + a^2 \sin^2 \theta } }$$

# 重力磁気効果

post-Newton 近似での計量は Minkowski 計量 $\eta_{\mu \nu}$ に摂動 $h_{\mu \nu}$ を加えた
$$g_{\mu \nu} = \eta_{\mu \nu} + h_{\mu \nu}$$
である. 以下では $h_{\mu \nu}$ について1次の摂動しか取り扱わず, 従って摂動量 $h_{\mu \nu}$ に関する添え字の上げ下げは 
Minkowski 計量 $\eta_{\mu \nu}$ により行うものとしてよい.



非相対論的物質のエネルギー・運動量テンソル $T^{\mu \nu}$ は, その密度 $\rho$, 速度 $v_i$, 圧力 $p$ から
$$T^{0 0} = \rho c^2$$
$$T^{0 i} = \rho c v_i$$
$$T^{i j} = p \delta_{i j} + \rho v_i v_j$$
と書くことができる. 従って Einstein 方程式は, 適当なゲージ条件のもとで


# 物体の運動
