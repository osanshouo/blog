+++
title = "球面調和関数による多重極展開の導出"
date = 2022-09-02
[taxonomies]
tags = [ "物理学", "天体力学", ]
+++

Binney & Tremaine の導出がやや迂遠で不満だったため, ストレートな導出のメモ.

密度分布 $\rho$ がつくる重力ポテンシャル $\Phi$ が満足する Poisson 方程式
$$\nabla^2 \Phi = 4 \pi G \rho$$
を球座標系で書き直すと
$$\frac{ 1 }{ r^2 } \frac{ \partial }{ \partial r } \left( r^2 \frac{ \partial \Phi }{ \partial r } \right) + \frac{ 1 }{ r^2 } \left[ \frac{ 1 }{ \sin \theta } \frac{ \partial }{ \partial \theta } \left( \sin \theta \frac{ \partial \Phi }{ \partial \theta } \right) + \frac{ 1 }{ \sin^2 \theta } \frac{ \partial^2 \Phi }{ \partial \varphi^2 } \right] = 4 \pi G \rho$$
となる.

ここで, ポテンシャル $\Phi$ および密度 $\rho$ を球面調和関数 $Y_{l m} ( \theta, \varphi )$ で展開することを考える.
$$\Phi ( r, \theta, \varphi ) = \sum_{l = 0}^\infty \sum_{m = - l}^l \Phi_{l m} ( r ) Y_{l m} ( \theta, \varphi )$$
$$\rho ( r, \theta, \varphi ) = \sum_{l = 0}^\infty \sum_{m = - l}^l \rho_{l m} ( r ) Y_{l m} ( \theta, \varphi )$$
なお, 展開係数 $\Phi_{l m} ( r )$, $\rho_{l m} ( r )$ は球面調和関数の直交性により
$$\Phi_{l m} ( r ) = \int \Phi ( r, \theta, \varphi ) Y_{l m}^* ( \theta, \varphi ) \sin \theta d \theta d \varphi$$
$$\rho_{l m} ( r ) = \int \rho ( r, \theta, \varphi ) Y_{l m}^* ( \theta, \varphi ) \sin \theta d \theta d \varphi$$
により与えられる. 球面調和関数の性質
$$\frac{ 1 }{ \sin \theta } \frac{ \partial }{ \partial \theta } \left( \sin \theta \frac{ \partial Y_{l m} }{ \partial \theta } \right) + \frac{ 1 }{ \sin^2 \theta } \frac{ \partial^2 Y_{l m} }{ \partial \varphi^2 } = - l ( l + 1 ) Y_{l m}$$
に注意すると, ポテンシャル $\Phi$ に関する Poisson 方程式は展開係数 $\Phi_{l m}$ に関する常微分方程式
$$\frac{ 1 }{ r^2 } \frac{ d }{ d r } \left( r^2 \frac{ d \Phi_{l m} }{ d r } \right) - \frac{ l ( l + 1 ) }{ r^2 } \Phi_{l m} = 4 \pi G \rho_{l m}$$
へと帰着される. 

座標原点付近の有界な領域にのみ密度分布が存在し, その外部領域では $\rho = 0$ であるという状況を考える.
まず, この外部領域では $\rho_{l m} = 0$ であるため, この方程式のふたつの独立解がただちに $r^l$ および $r^{-1-l}$ と求まる. 
従って, ポテンシャルが無限遠でゼロに収束するという境界条件のもとでは外部領域における 
$\Phi_{l m}$ の $r$-依存性は, $C$ を定数として
$$\Phi_{l m} ( r ) = \frac{ C }{ r^{1 + l} }$$
と決定される. そこで, 任意の $r$ における $\Phi_{l m} ( r )$ を未定の関数 $A ( r )$, $B ( r )$ を用いて
$$\Phi_{l m} ( r ) = r^l A ( r ) + \frac{ B ( r ) }{ r^{l + 1} }$$
と表示しよう. $\Phi_{l m}$ の微分
$$\frac{ d \Phi_{l m} }{ r d } = l r^{l-1} A ( r ) + r^l \frac{ d A }{ d r } - ( l + 1 ) \frac{ B ( r ) }{ r^{l+2} } + \frac{ 1 }{ r^{l+1} } \frac{ d B }{ d r }$$
について, 関数 $A$, $B$ に対して次の関係式
$$r^l \frac{ d A }{ d r } + \frac{ 1 }{ r^{l+1} } \frac{ d B }{ d r } = 0 \tag{X}$$
を要求すると, これは
$$\frac{ d \Phi_{l m} }{ d r } = l r^{l-1} A ( r ) - ( l + 1 ) \frac{ B ( r ) }{ r^{l+2} }$$
へと帰着する. これをさらに微分すると
$$\frac{ d }{ d r } \left( r^2 \frac{ d \Phi_{l m} }{ d r } \right) = l ( l + 1 ) \Phi_{l m} ( r ) + l r^{l+1} \frac{ d A }{ d r } - \frac{ l + 1 }{ r^l } \frac{ d B }{ d r }$$
が得られる. これを Poisson 方程式と比較すると, $A$, $B$ に関する方程式
$$l r^{l+1} \frac{ d A }{ d r } - \frac{ l + 1 }{ r^l } \frac{ d B }{ d r } = 4 \pi G r^2 \rho_{l m} ( r ) \tag{Y}$$
が結論される. これと式 (X) を連立することにより $A$, $B$ を決定することができる.
式 (X), (Y) から $B$ を消去すると, $A$ に関する方程式
$$( 2 l + 1 ) r^{l + 1} \frac{ d A }{ d r } = 4 \pi G r^2 \rho_{l m} ( r )$$
が得られる. $r \to \infty$ で $A \to 0$ でなければならないことに注意してこれを積分すると
$$A ( r ) = - \frac{ 4 \pi G }{ 2 l + 1 } \int_r^\infty \frac{ d a }{ a^{l + 1} } \rho_{l m} ( a )$$
となる. 同様に, 式 (X), (Y) から $A$ を消去すると
$$- \frac{ 2 l + 1 }{ r^l } \frac{ d B }{ d r } = 4 \pi G r^2 \rho_{l m} ( r )$$
となり, $r \to 0$ で $B \to 0$ でなければならないことに注意して積分すると
$$B ( r ) = - \frac{ 4 \pi G }{ 2 l + 1 } \int_0^r d a \\, a^{l+2} \rho_{l m} ( a )$$
となる. 以上から, ポテンシャル $\Phi_{l m}$ の表式
$$\Phi_{l m} ( r ) = - \frac{ 4 \pi G }{ 2 l + 1 } \left[ r^l \int_r^\infty \frac{ d a }{ a^{l + 1} } \rho_{l m} ( a ) + \frac{ 1 }{ r^{l+1} } \int_0^r d a \\, a^{l+2} \rho_{l m} ( a ) \right]$$
が導かれる.

特に, 質量分布がない外部領域では, 第1項の積分がゼロであることからこれは
$$\Phi_{l m} ( r ) = - \frac{ 4 \pi G }{ 2 l + 1 } \frac{ Q_{l m} }{ r^{l+1} }$$
$$Q_{l m} = \int_0^\infty dr \\, r^{l+2} \rho_{l m} ( r )$$
に帰着する. 係数 $Q_{l m}$ を多重極モーメントと呼ぶ. 外部領域での重力ポテンシャル $\Phi$ の最終的な表式は
$$\Phi ( r, \theta, \varphi ) = - 4 \pi G \sum_{l = 0} \sum_{m = - l}^l \frac{ Q_{l m} }{ 2 l + 1 } \frac{ Y_{l m} ( \theta, \varphi) }{ r^{l+1} }$$
である.


# 参考文献

* Binney & Tremaine, Galactic Dynamics 2nd ed., Princeton University Press
