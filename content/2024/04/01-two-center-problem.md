+++
title = "重力2中心問題"
date = 2024-04-01
[extra]
toc = true
[taxonomies]
tags = [ "物理学", "解析力学", ]
+++

本記事では重力2中心問題 (two-center problem), または Euler の三体問題として知られる系について議論します.

空間的に固定された二つの質点がつくる重力場に従う質点の運動について考えます.
この系には重力源となる二つの質点を結ぶ直線を回転軸とする回転対称性があり, 
物体の運動はその初速度とこの直線がなす平面内に限られます.
従ってこの系は2次元系として扱って良く, ふたつの重力源の座標が $( \pm c, 0 )$ となる座標 $(x, y)$ を取ります.

この問題の Lagrangian $L$ は
$$L = \frac{ 1 }{ 2 } ( \dot{x}^2 + \dot{y}^2 )  + \frac{ m_+ }{ \sqrt{ ( x - c )^2 + y^2 } } + \frac{ m_- }{ \sqrt{ ( x + c )^2 + y^2 } }$$
により与えられます. 以下では点 $(x, y )$ と重力源 $( \pm c, 0 )$ の距離を $r_{\pm}$ と書くことがあります.
$$r_\pm = \sqrt{ ( x \mp c )^2 + y^2 }$$

注意として, この問題は通常の三体問題 (特に制限三体問題) とは異なります. 
制限三体問題は Kepler 運動するふたつの質点がつくる重力場中の質点の運動を扱うものでしたが,
重力二中心問題は, __空間的に固定された__ ふたつの質点がつくる重力場を考えます.
従って重力二中心問題の運動方程式は, 円制限三体問題の運動方程式から Coriolis 項を除いたものに一致します.


# 楕円座標

ここで楕円座標 $( \mu, \nu )$ を次式により定義しましょう.
$$\mu = \frac{ r_- + r_+ }{ 2 } , \ \ \nu = \frac{ r_- - r_+ }{ 2 }$$
明らかに $r_\pm = \mu \mp \nu$ が成立します. 両辺を二乗すると
$$(x \mp c )^2 + y^2 = \mu^2 \mp 2 \mu \nu + \nu^2$$
となることから, 座標 $x$ は
$$x = \frac{ \mu \nu }{ c }$$
と表示できます. これを上式に代入して整理すると
$$y^2 = \frac{ ( \mu^2 - c^2 ) ( c^2 - \nu^2 ) }{ c^2 }$$
あるいは
$$y = \pm \sqrt{ \mu^2 + \nu^2 - c^2 - \frac{ \mu^2 \nu^2 }{ c^2 } }$$
を得ます. つまり $(\mu, \nu)$ を指定しただけでは 
$y$ の符合は特定できません (二価の対応) が, 対称性から $y > 0$ についてのみ議論すれば十分です.

速度 $\dot{x}$, $\dot{y}$ は上式の時間微分
$$\dot{x} = \frac{ \dot{\mu} \nu + \mu \dot{\nu} }{ c }$$
$$\dot{y} = \pm \frac{ 1 }{ \sqrt{ \mu^2 + \nu^2 - c^2 - \frac{ \mu^2 \nu^2 }{ c^2 } } } \left[ \frac{ c^2 - \nu^2 }{ c^2 } \mu \dot{\mu} - \frac{ \mu^2 - c^2 }{ c^2 } \nu \dot{\nu} \right]$$
です. ここから, Lagrangian の運動エネルギー項は, 楕円座標 $(\mu, \nu)$ では
$$\dot{x}^2 + \dot{y}^2 = \frac{ \mu^2 - \nu^2 }{ \mu^2 - c^2 } \dot{\mu}^2 + \frac{ \mu^2 - \nu^2 }{ c^2 - \nu^2 } \dot{\nu}^2$$
と表示されることがわかります.
ここで $\dot{\mu}$ と $\dot{\nu}$ の積の項が消えること (楕円座標が直交座標であること) に注意してください.
よって, 楕円座標 $(\mu, \nu)$  に正準共役な運動量 $p_\mu$, $p_\nu$ は
$$p_\mu = \frac{ \mu^2 - \nu^2 }{ \mu^2 - c^2 } \dot{\mu}$$
$$p_\nu = \frac{ \mu^2 - \nu^2 }{ c^2 - \nu^2 } \dot{\nu}$$
と求まります.


# 正準理論

重力2中心問題の Hamiltonian 
$$H = \frac{ \partial L }{ \partial \dot{\mu} } \dot{\mu} + \frac{ \partial L }{ \partial \dot{\nu} } \dot{\nu} - L$$
を求めましょう. Lagrangian のポテンシャル項は
$$\frac{ m_+ }{ r_+ } + \frac{ m_- }{ r_- } = \frac{ 1 }{ \mu^2 - \nu^2 } \left[ ( m_+ + m_- ) \mu + ( m_+ - m_- ) \nu \right]$$
となりますが, これをより一般的に
$$- \frac{ U_\mu ( \mu ) + U_\nu ( \nu ) }{ \mu^2 - \nu^2 }$$
という形に書いておきます. つまり, $U_\mu = - ( m_+ + m_- ) \mu$, $U_\nu = - ( m_+ - m_- ) \nu$ です.
その結果, この系の Hamiltonian は
$$H = \frac{ 1 }{ 2 ( \mu^2 - \nu^2 ) } \left[ ( \mu^2 - c^2 ) p_\mu^2 + ( c^2 - \nu^2 ) p_\nu^2 \right] + \frac{ U_\mu ( \mu ) + U_\nu ( \nu ) }{ \mu^2 - \nu^2 }$$
となります.

この Hamiltonian を Hamilton-Jacobi 理論に基づいて取り扱います.
重力2中心問題は自励系ですからエネルギー $E$ が保存量であり, Hamilton の主関数 $S$ は時間依存性を取り出した
$$S = S_1 ( \mu, \nu ) - E t$$
という形になります. よって Hamilton-Jacobi 方程式は
$$\frac{ 1 }{ 2 ( \mu^2 - \nu^2 ) } \left[ ( \mu^2 - c^2 ) \left( \frac{ \partial S_1 }{ \partial \mu } \right)^2 + ( c^2 - \nu^2 ) \left( \frac{ \partial S_1 }{ \partial \nu } \right)^2 \right] + \frac{ U_\mu ( \mu ) + U_\nu ( \nu ) }{ \mu^2 - \nu^2 } = E$$
と書けます. これを整理すると
$$\left[ ( \mu^2 - c^2 ) \left( \frac{ \partial S_1 }{ \partial \mu } \right)^2  + 2 U_\mu ( \mu ) - 2 E \mu^2 \right] + \left[ ( c^2 - \nu^2 ) \left( \frac{ \partial S_1 }{ \partial \nu } \right)^2 + 2 U_\nu ( \nu ) + 2 E \nu^2 \right] = 0$$
となり, 明らかな変数分離系に帰着されます. すなわち重力2中心問題は可積分系です.
そこで第1項を定数 $\Phi$ と等値します.

まとめると, Hamilton の主関数 $S$ は
$$S = S_\mu ( \mu ) + S_\nu ( \nu ) - E t$$
という形に表示できます. 関数 $S_\mu$, $S_\nu$ はそれぞれ
$$( \mu^2 - c^2 ) \left( \frac{ d S_\mu }{ d \mu } \right)^2  + 2 U_\mu ( \mu ) - 2 E \mu^2 = \Phi$$
$$( c^2 - \nu^2 ) \left( \frac{ d S_\nu }{ d \nu } \right)^2 + 2 U_\nu ( \nu ) + 2 E \nu^2 = - \Phi$$
を満足します.
