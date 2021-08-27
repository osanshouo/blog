+++
title = "一般三体問題におけるLagrange点"
date = 2021-08-28
[extra]
toc = true
[taxonomies]
tags = ["物理学", "天体力学", ]
+++

Lagrange 点は円制限三体問題の特殊解として極めて有名ですが, 対応する特殊解が一般三体問題においても存在することはあまり知られていないようです.
本記事ではこのことに証明を与えます.


# 運動方程式

互いに重力相互作用する3つの質点からなる系について考えます.
$i = 1, 2, 3$ 番目の質点の質量を $m_i$, 座標を $\mathbfit{X}_i$ とするとき, これらの質点の運動方程式は
$$\frac{ d^2 \mathbfit{X}_i }{ d t^2 } = \sum\_{j \neq i} - G m_j \frac{ \mathbfit{X}_i - \mathbfit{X}_j }{ | \mathbfit{X}_i - \mathbfit{X}_j |^3 }$$
です. 

明らかな保存量として Euler 積分すなわち全エネルギー $E$, 全運動量 $\mathbfit{P}$, 全角運動量 $\mathbfit{L}$ が存在します.
$$E = \sum_i \frac{ 1 }{ 2 } m_i \dot{\mathbfit{X}}_i^2 - \sum\_\mathrm{pair} \frac{ G m_i m_j }{ | \mathbfit{X}_i - \mathbfit{X}_j | }$$
$$\mathbfit{P} = \sum_i m_i \dot{\mathbfit{x}}_i$$
$$\mathbfit{L} = \sum_i m_i \mathbfit{X}_i \times \dot{\mathbfit{X}}_i$$
適当な Galilei 変換により常に $\mathbfit{P} = 0$ かつ重心を座標原点に固定することができますから, 以下ではこの慣性系を用います.
この結果, 三体の座標 $\mathbfit{X}_i$ は
$$\sum_i m_i \mathbfit{X}_i = 0$$
を満足します.


# Lagrange 点

円制限問題における Lagrange 点とは, 回転座標系で見たときに三体がいずれも静止して見えるような解のことでした. 
これを一般化し, $R ( t )$ を回転行列
$$R ( t ) = \begin{pmatrix} \cos \Omega t & - \sin \Omega t & \\\\ \sin \Omega t & \cos \Omega t & \\\\ & & 1 \end{pmatrix}$$
として次の形に書ける解を探します.
$$\mathbfit{X}_i ( t ) = R ( t ) \mathbfit{x}_i \tag{☆}$$
ここに $\mathbfit{x}_i$ は時刻 $t$ によらない定ベクトルです. 

まず求める解においては第 $i$ 体と第 $j$ 体の距離 $| \mathbfit{X}_i ( t ) - \mathbfit{X}_j ( t ) |$ は時間的に変化しないことに注意します.
すなわち
$$| \mathbfit{X}_i ( t ) - \mathbfit{X}_j ( t ) | = | \mathbfit{x}_i - \mathbfit{x}_j | = r\_{i j}$$
が成立します. 一方で, 式 (☆) の二階時間微分について, $\mathsf{P}$ を $( X, Y )$-平面への射影演算子
$$\mathsf{P} = I - \mathbf{e}_z \otimes \mathbf{e}_z = \begin{pmatrix} 1 & & \\\\ & 1 & \\\\ & & 0 \end{pmatrix}$$
とすると, これは
$$\frac{ d^2 \mathbfit{X}_i }{ d t^2 } = - \Omega^2 R \mathsf{P} \mathbfit{x}_i$$
と計算できます[^1]. 
これを運動方程式に代入すると, 両辺で回転行列 $R ( t )$ の作用がくくり出せ, 
それが可逆であることから
$$\Omega^2 \mathsf{P} \mathbfit{x}_i = \sum\_{j \neq i} G m_j \frac{ \mathbfit{x}_i - \mathbfit{x}_j }{ | \mathbfit{x}_i - \mathbfit{x}_j |^3 } \tag{♢}$$
という方程式系に帰着されます. 従って問題はこの方程式を満足するベクトル $\mathbfit{x}_i$ を求めることです.

なお, この問題は有効ポテンシャル
$$U = - \sum_i \frac{ 1 }{ 2 } m_i \Omega^2 | \mathsf{P} \mathbfit{x}\_i |^2 - \frac{ G m\_1 m_2 }{ r_{12} } - \frac{ G m_1 m_3 }{ r_{13} } - \frac{ G m_2 m_3 }{ r_{23} }$$
の停留点を求める問題に等しいです.


# $z_i = 0$ であること

すべての質点が $z = 0$ 平面上に乗ることを示します. 
いずれかひとつの質点 (質点1とします) がこの平面に乗らないと仮定しましょう. このとき $z_1 > 0$ として一般性を失いません. 
さらに, 質点2, 質点3を $z_1 \geq z_2 \geq z_3$ となるように選びます.

いま座標原点が重心となるように座標系を選んでいますから, 
$$m_1 z_1 + m_2 z_2 + m_3 z_3 = 0$$ 
でなければなりません. 質量 $m_i$ はすべて正ですから, このことは $z_3 < 0$ であることを意味します.

質点 $i=1$ に関する式 (♢) の $z$ 成分を整理すると
$$0 = - \left( \frac{ m_2 }{ r_{21}^3 } + \frac{ m_3 }{ r_{31}^3 } \right) z_1 + \frac{ m_2 }{ r_{21}^3 } z_2 + \frac{ m_3 }{ r_{31}^3 } z_3$$
という関係式が得られます. この等式を満足するためには $z_1 > 0$ および $z_3 < 0$ であることから $z_2 > 0$ でなければなりません.
ところが $i = 3$ に関する式 (♢) の $z$ 成分は
$$0 = \frac{ m_1 }{ r_{31}^3 } z_1 + \frac{ m_2 }{ r_{23}^3 } z_2 - \left( \frac{ m_1 }{ r_{31}^3 } + \frac{ m_2 }{ r_{23}^3 } \right) z_3$$
であり, 同様の考察からは $z_2 < 0$ が導かれます. これは矛盾であり, 結局 $z_i = 0$ でなければなりません.
逆にこのとき式 (♢) の $z$ 成分はすべて自明に満足されます.


# Euler の直線解

次に, 3質点がすべて同一直線に乗るような解が存在するか検討します.
この直線としては $x$ 軸を選んでよく, $z_i = 0$ かつ $y_i = 0$ として一般性を失いません.
さらに, 質点の名前を $x_1 > x_2 > x_3$ となるように取ります.

$y_i = 0$ により式 (♢) の $y$ 成分は自明に満足されます. 従って非自明なのは $x$ 成分だけです.
仮定により $r_{12} = x_1 - x_2$ などとなることに注意してそれを書き下してみます.
$$\Omega^2 x_1 = G m_2 \frac{ 1 }{ ( x_1 - x_2 )^2 } + G m_3 \frac{ 1 }{ ( x_1 - x_3 )^2 } \tag{1}$$
$$\Omega^2 x_2 = - G m_1 \frac{ 1 }{ ( x_1 - x_2 )^2 } + G m_3 \frac{ 1 }{ ( x_2 - x_3 )^2 } \tag{2}$$
$$\Omega^2 x_3 = - G m_1 \frac{ 1 }{ ( x_1 - x_3 )^2 } - G m_2 \frac{ 1 }{ ( x_2 - x_3 )^2 } \tag{3}$$
なお以下では重力定数 $G$ は式から省略します ($G m_i$ を $m_i$ と略記していると解釈してください).

式(1)から式(2)を差し引いたもの, また式(2)から式(3)を差し引いたものは $r_{ij}$ に関する等式に帰着されます.
$$\Omega^2 r_{12} = \frac{ m_1 + m_2 }{ r_{12}^2 } + \frac{ m_3 }{ r_{13}^2 } - \frac{ m_3 }{ r_{23}^2 } \tag{4}$$
$$\Omega^2 r_{23} = \frac{ m_2 + m_3 }{ r_{23}^2 } + \frac{ m_1 }{ r_{13}^2 } - \frac{ m_1 }{ r_{12}^2 } \tag{5}$$
ここで $\delta = r_{12} / r_{23}$ とおくと, 式(4)において
$$r_{13} = \frac{ 1 + \delta }{ \delta } r_{12} , \ \ r_{23} = r_{12} / \delta$$
を代入することでこの方程式を $r_{12}$ と $\delta$ だけに関する方程式
$$\Omega^2 r_{12}^3 = m_1 + m_2 + m_3 \left( \frac{ \delta^2 }{ ( 1 + \delta )^2 } - \delta^2 \right) \tag{6}$$
へと帰着させられます. 同様に式(5)は
$$r_{13} = ( 1 + \delta ) r_{23} , \ \ r_{12} = \delta r_{23} \tag{6}$$
により
$$\Omega^2 r_{23}^2 = m_2 + m_3 + m_1 \left( \frac{ 1 }{ ( 1 + \delta )^2 } - \frac{ 1 }{ \delta^2 } \right) \tag{7}$$
となります. $r_{23} = r_{12} / \delta$ ですから式(7)の左辺は $\Omega^2 r_{12}^3 / \delta^3$ に等しく, 
従って式(6)と連立することで $r_{12}$ を消去できます.
$$m_1 + m_2 + m_3 \left( \frac{ \delta^2 }{ ( 1 + \delta )^2 } - \delta^2 \right) = \delta^3 \left[ m_2 + m_3 + m_1 \left( \frac{ 1 }{ ( 1 + \delta )^2 } - \frac{ 1 }{ \delta^2 } \right) \right]$$
これを整理すると, $\delta$ に関する五次方程式
$$( m_2 + m_3 ) \delta^5 + ( 2 m_2 + 3 m_3 ) \delta^4 + ( m_2 + 3 m_3 ) \delta^3 - ( 3 m_1 + m_2 ) \delta^2 - ( 3 m_1 + 2 m_2 ) \delta - ( m_1 + m_2 ) = 0$$
が得られます.
この方程式は符号の変化が一回だけなので, [Descartes の符号法則](https://ja.wikipedia.org/wiki/%E3%83%87%E3%82%AB%E3%83%AB%E3%83%88%E3%81%AE%E7%AC%A6%E5%8F%B7%E6%B3%95%E5%89%87) 
により正の解はひとつのみ存在します. その解 $\delta$ が求める直線解の配位を決定します.

まとめると, 一般三体問題の直線解は, まず三体の質量 $m_1$, $m_2$, $m_3$ から得られる五次方程式の解 $\delta$ によってその相対的な配位が決定されます.
$r_{12}$ または $r_{23}$ のどちらか一方が解の空間スケールを特定し, 対応する回転角速度 $\Omega$ は式(4)または式(5)から得られます.

なお Euler の直線解は3個 (L<sub>1</sub>, L<sub>2</sub>, L<sub>3</sub>) ありましたが,
これはそれぞれ $m_1$, $m_2$, $m_3$ が他の二体の質量に比べて小さい場合の極限に対応します.


# Lagrange の正三角形解

次に, 三体が同一直線に乗るとは限らない一般の可能な配位について検討します.
第1体が $x$ 軸に乗るように座標系を選んで一般性を失いません. 
このとき $y_1 = 0$ ですから, 重心が座標原点に一致するという条件から
$$m_2 y_2 + m_3 y_3 = 0 \tag{8}$$
が要求されます. 一方, このとき $i=1$ に関する式(♢)の $y$ 成分は
$$m_2 \frac{ y_2 }{ r_{12} } + m_3 \frac{ y_3 }{ r_{13} } = 0 \tag{9}$$
に帰着します. これら2式を連立し $y_3$ を消去すると
$$\left( \frac{ 1 }{ r_{12} } - \frac{ 1 }{ r_{13} } \right) y_2 = 0$$
という方程式が得られ, $y_2 = 0$ であるか $r_{12} = r_{13}$ であるかのふたつの可能性しかありません.
前者の場合, 式(8)から $y_3 = 0$ が従い, 従ってこれは直線解です.
$i = 2, 3$ についても同様の議論を繰り返すと, 直線解以外の可能性としては
$$r_{12} = r_{23} = r_{13}$$
を満足するものしかないことが結論されます. これは三体が正三角形を形作る解です.


# 中心配位

ここで求めたものは三体がなす図形の大きさが変化せず単に回転するもの (relative equilibirum と呼ばれます) でしたが, 
回転と同時に相似変形を許すような解 (homographic solution) は一般の $N$ 体問題において詳しく調べられており,
そのような解における回転や相似変換を除いた $N$ 体の配置のことを中心配位 ([central configuration](https://en.wikipedia.org/wiki/Central_configuration)) と呼びます.
これについては参考文献や [Scholarpedia の記事](http://www.scholarpedia.org/article/Central_configurations) をご覧ください.


# 参考文献
* Boccaletti & Pucacco, _Theory of Orbits 1: Integrable Systems and Non-perturbative Methods_, Springer (2001)


[^1]: $\mathbfit{x}_i$ が時刻 $t$ に依存する場合, この等式は
$$\frac{ d^2 \mathbfit{X}_i }{ d t^2 } = R \left[ \ddot{\mathbfit{x}}_i + 2 \Omega \mathbf{e}_z \times \dot{\mathbfit{x}}_i - \Omega^2 \mathsf{P} \mathbfit{x}_i \right]$$
へと変更されます. 第1項が加速度項, 第2項が Coriolis 力項, 第3項が遠心力項です.
