+++
title = "Kepler問題におけるKustaanheimo-Stiefel変換"
date = 2021-04-12
[extra]
toc = true
[taxonomies]
tags = ["物理学", "天体力学", "解析力学"]
+++

平面 Kepler 問題の正則化としては [Levi-Civita 変換](https://ja.wikipedia.org/wiki/%E3%83%AC%E3%83%B4%E3%82%A3%EF%BC%9D%E3%83%81%E3%83%B4%E3%82%A3%E3%82%BF%E5%A4%89%E6%8F%9B) がよく知られていますが,
3次元問題にこれを拡張したものが Kustaanheimo-Stiefel 変換 (KS 変換) で, 1965年に発表されました[^1].
本記事では KS 変換を主として原論文に沿って導入します.


# 定義
Kepler 問題に任意の摂動 $\boldsymbol{F}$ が加わった運動方程式
$$\frac{ d^2 \boldsymbol{x} }{ d t^2 } = - \mu \frac{ \boldsymbol{x} }{ | \boldsymbol{x} |^3 } + \boldsymbol{F} ( \boldsymbol{x} ) \tag{1}$$
について考えます. これは $| \boldsymbol{x} | \to 0$ の極限で力が発散する座標特異点が存在し, 数学的または数値計算的に扱いが困難です.

Levi-Civita 変換は2次元 Kepler 問題を扱ったもので,座標 $\boldsymbol{x} = ( x_1, x_2 )$ に対して
$$\begin{cases} x_1 &= Q_1^2 - Q_2^2 \\\\ x_2 &= 2 Q_1 Q_2 \end{cases}$$
により座標 $( Q_1, Q_2 )$ を導入するものです ([Wikipedia](https://ja.wikipedia.org/wiki/%E3%83%AC%E3%83%B4%E3%82%A3%EF%BC%9D%E3%83%81%E3%83%B4%E3%82%A3%E3%82%BF%E5%A4%89%E6%8F%9B) を読んでください).
この変換は1対2の対応であり, $( Q_1, Q_2 ) \mapsto ( - Q_1 , - Q_2 )$ としても同一の $( x_1, x_2 )$ が得られることに注意します.

Kustaanheimo-Stiefel 変換は, Levi-Civita 変換を次のように拡張するものです.
$$\begin{cases} x_1 &= u_1^2 - u_2^2 - u_3^2 + u_4^2 \\\\ x_2 &= 2 ( u_1 u_2 - u_3 u_4 ) \\\\ x_3 &= 2 ( u_1 u_3 + u_2 u_4 ) \end{cases} \tag{2}$$
つまり, 3次元空間 $( x_1, x_2, x_3 ) \in \mathbb{R}^3$ と4次元空間 $( u_1, u_2, u_3, u_4 ) \in \mathbb{R}^4$ の間の対応関係になっています.
明らかに $u_3 = u_4 = 0$ とすると Levi-Civita 変換に帰着します.
また, 容易に確認できるように, 座標 $( u_1, u_2, u_3, u_4 )$ は Levi-Civita 変換と類似の
$$x_1^2 + x_2^2 + x_3^2 = ( u_1^2 + u_2^2 + u_3^2 + u_4^2 )^2 \tag{3}$$
という関係式を満足します.

座標 $( u_1, u_2, u_3, u_4 )$ を指す適当な名称が見当たらないため, 本記事ではこの座標のことを KS 座標と呼ぶことにします.
物理空間が3次元であるのに対して KS 座標は4次元ですから1次元が過剰であり, $\beta$ を任意の実数として次の変換
$$\begin{cases}u_1 &\mapsto u_1 \cos \beta - u_4 \sin \beta \\\\
u_2 &\mapsto u_2 \cos \beta + u_3 \sin \beta \\\\
u_3 &\mapsto u_2 \sin \beta - u_3 \cos \beta \\\\
u_4 &\mapsto u_1 \sin \beta + u_4 \cos \beta \end{cases} \tag{4}$$
を施しても同一の物理空間の点 $( x_1, x_2, x_3 )$ を与えます. 
なお2次元の場合, $u_3 = u_4 = 0$ を保つためには $\sin \beta = 0$ でなければならず, 
その結果この内部自由度は上述の離散的な変換 $( u_1, u_2 ) \mapsto ( - u_1, - u_2 )$ に帰着します.
すなわち, Levi-Civita 変換のときの離散的な余剰自由度は, 
KS 座標が持つ $U ( 1 )$ (あるいは $S^1$) 内部自由度のある平面での断面に対応します.


# 拘束条件
KS 座標での運動方程式を導く前に, 物理的考察が必要です.
上述のように KS 座標は $U ( 1 )$ の内部自由度がありますから, 
この自由度の範囲で任意に KS 座標を変化させても物理的には等価です.
それ故に, 物理空間での運動方程式を与えるだけでは, KS 空間での時間発展は一意には決まりません.
$U ( 1 )$ の内部自由度を手で固定する必要があります.
そこで以下では原論文に従って
$$u_4 du_1 - u_3 du_2 + u_2 du_3 - u_1 du_4 = 0 \tag{5}$$
という非ホロノーム拘束を課します. あるいは, $dt$ で割った
$$\Phi ( \boldsymbol{u}, \dot{\boldsymbol{u}} ) = u_4 \frac{ du_1 }{ d t } - u_3 \frac{ du_2 }{ d t } + u_2 \frac{ du_3 }{ d t } - u_1 \frac{ du_4 }{ d t } = 0 \tag{6}$$
という拘束を課すものと理解しても構いません.

この拘束条件は, KS 空間の点 $( u_1, u_2, u_3, u_4 ) \in \mathbb{R}^4$ およびその点での接ベクトル 
$( du_1, du_2, du_3, du_4 )$ に関する条件となっています. 
言い換えると, ある点 $( u_1, u_2, u_3, u_4 )$ が与えられたとき,
その点を通る可能な運動は, 接ベクトルがこの条件を満足する3次元超曲面に限られます.
この意味で問題の拘束条件は KS 空間の過剰な1次元を削減するものになっています.

原論文に従って KS 変換の行列表示
$$\begin{pmatrix} x_1 \\\\ x_2 \\\\ x_3 \\\\ 0 \end{pmatrix} = A ( u ) \begin{pmatrix} u_1 \\\\ u_2 \\\\ u_3 \\\\ u_4 \end{pmatrix} \tag{7}$$
$$A ( u ) = \begin{pmatrix} u_1 & -u_2 & -u_3 & u_4 \\\\ u_2 & u_1 & -u_4 & -u_3 \\\\ u_3 & u_4 & u_1 & u_2 \\\\ u_4 & -u_3 & u_2 & -u_1 \end{pmatrix} \tag{8}$$
を導入しておくと便利です (第4成分は恒等的にゼロです). このとき,KS 変換の定義式を微分することにより
$$\begin{pmatrix} dx_1 \\\\ dx_2 \\\\ dx_3 \\\\ 0 \end{pmatrix} = 2 A ( u ) \begin{pmatrix} du_1 \\\\ du_2 \\\\ du_3 \\\\ du_4 \end{pmatrix} \tag{9}$$
という関係式が成立することが確認できます (ここでは上式とは異なり第4成分が0になるために拘束条件が必要です).
特に, このことから
$$dx_1^2 + dx_2^2 + dx_3^3 = 4 r ( du_1^2 + du_2^2 + du_3^3 + du_4^4 )$$
が導かれます.


# 運動方程式
それでは KS 座標での運動方程式を求めます. 以下では dot は時間微分を表すものとします.

まず運動エネルギー $T = \frac{ 1 }{ 2 } m ( \dot{x}_1^2 + \dot{x}_2^2 + \dot{x}_3^2 )$ は, KS 座標で書き直すと, 拘束条件のために
$$T = 2 m r ( \dot{u}_1^2 + \dot{u}_2^2 + \dot{u}_3^2 + \dot{u}_4^2 )$$
に帰着されます. 簡単のため摂動 $\boldsymbol{F}$ がポテンシャル $V$ から導かれるものと仮定すると, Lagrangian は
$$L = 2 m r ( \dot{u}_1^2 + \dot{u}_2^2 + \dot{u}_3^2 + \dot{u}_4^2 ) + \frac{ \mu }{ r } - V ( \boldsymbol{u} )$$
であり, 対応する運動方程式は, $i = 1, 2, 3, 4$ として
$$4 m \left[ \frac{ d }{ d t } ( r \dot{u}_i ) - u_i ( \dot{u}_1^2 + \dot{u}_2^2 + \dot{u}_3^2 + \dot{u}_4^2 ) \right] = - \frac{ 2 \mu }{ r^2 } u_i + f_i \tag{10}$$
$$f_i = - \frac{ \partial V }{ \partial u_i }$$
と求まります.

力 $\boldsymbol{f}$ について, これは実空間での力 $\boldsymbol{F} = - \partial V / \partial \boldsymbol{x}$ とは
$$f_i = \sum_{j = 1}^3 \frac{ \partial x_j }{ \partial u_i } F_j$$
という関係にあります. KS 変換の定義を代入すれば, 行列表示
$$\begin{pmatrix} f_1 \\\\ f_2 \\\\ f_3 \\\\ f_4 \end{pmatrix} = 2 \begin{pmatrix} u_1 & u_2 & u_3 \\\\ -u_2 & u_1 & u_4 \\\\ -u_3 & -u_4 & u_1 \\\\ u_4 & -u_3 & u_2 \end{pmatrix} \begin{pmatrix} F_1 \\\\ F_2 \\\\ F_3 \end{pmatrix} \tag{11}$$
が得られます. 逆に, この等式により $\boldsymbol{f}$ を定義するものと理解するとき, 上の運動方程式は非保存力に対しても適用できます.

この導出では拘束条件を用いませんでしたが, 実際にはこの運動方程式と拘束条件は両立し,
初期条件として拘束条件を満足するものを与えれば, その後の時間発展においても拘束条件は満足され続けます.
これを証明するために, 運動方程式の各成分 $i = 1, 2, 3, 4$ に対してそれぞれ $u_4$, $-u_3$, $u_2$, $-u_1$ を乗じたものを足し合わせます.
その結果, 右辺は上の行列表示 (11) から恒等的にゼロとなります (ここでは行列表示は摂動部分についてのみ与えましたが, 右辺第1項についても同じ行列表示が成立します).
左辺第2項も同様に恒等的にゼロです. 
残る左辺第1項について, 自明な係数を除くとこれは
$$u_4 \frac{ d }{ d t } ( r \dot{u}_1 ) - u_3 \frac{ d }{ d t } ( r \dot{u}_2 ) + u_2 \frac{ d }{ d t } ( r \dot{u}_2 ) - u_1 \frac{ d }{ d t } ( r \dot{u}_4 )$$
に等しいですが, 微分をくくり出すことができ, この式は $\frac{ d }{ d t } ( r \Phi )$ となります. 以上のことから, 
運動方程式 (10) から
$$\frac{ d }{ d t } \left[ r \Phi \left( \boldsymbol{u}, \dot{\boldsymbol{u}} \right) \right] = 0$$
という方程式が導かれるため, $r \Phi = \mathrm{Const.}$ が成立します. 特に初期条件として $\Phi = 0$ を満たすものを選ぶならば,
運動方程式の解は任意の時刻で $\Phi = 0$ を満足します.


# 正則化
運動方程式 (10) は依然として $r = 0$ が特異点となっています. これを除去するために, 時間座標 $t$ を変換し, 新しい"時間"座標 $s$ を
$$s = \int \frac{ d t }{ r } \tag{12}$$
により定義します. なお以下では摂動が定常な保存力である場合に議論を限定します (保存力でない場合については原論文を参照してください).

運動方程式を変数 $s$ に関する方程式に書き直すには, 変数変換
$$\frac{ d }{ d t } = \frac{ 1 }{ r } \frac{ d }{ d s } \tag{13}$$
を適用します. $s$-微分を prime で表すことにすると, 簡単な計算により
$$4 m \frac{ d^2 u_i }{ d s^2 } + \left( \frac{ 2 \mu }{ r } - \frac{ 4 m \boldsymbol{u}'^2 }{ r } \right) u_i = r f_i$$
が導かれます. ただし $\boldsymbol{u}'^2 = {u'_1}^2 + {u'_2}^2 + {u'_3}^2 + {u'_4}^2$ とおきました.

ところで, いまの仮定のもとではエネルギー積分
$$E = \sum_{i=1}^4 \frac{ \partial L }{ \partial \dot{u}_i } \dot{u}_i - L$$
が存在します. 陽に計算すると
$$E = 2 m r ( \dot{u}_1^2 + \dot{u}_2^2 + \dot{u}_3^2 + \dot{u}_4^2 ) - \frac{ \mu }{ r } + V ( \boldsymbol{u} )$$
あるいは
$$E = \frac{ 2 m \boldsymbol{u}'^2 }{ r } - \frac{ \mu }{ r } + V ( \boldsymbol{u} )$$
となります. これを上式と比較すると, 運動方程式の左辺第2項の係数は
$$\frac{ 2 \mu }{ r } - \frac{ 4 m \boldsymbol{u}'^2 }{ r } = 2 ( V ( \boldsymbol{u} ) - E )$$
となりますから, 運動方程式は最終的に
$$4 m \frac{ d^2 u_i }{ d s^2 } - 2 E u_i = r f_i + 2 V ( \boldsymbol{u} ) u_i \tag{14}$$
に帰着されます. これは (摂動に特異点が存在しなければ) $r \to 0$ の極限でも正則な運動方程式となっています.

特に負エネルギー解 $E < 0$ の場合 (すなわち摂動がなければ楕円軌道となる状況では), 初期軌道長半径 $a_0$ を
$$E = - \frac{ \mu }{ 2 a_0 }$$
により導入でき, 運動方程式は
$$\frac{ d^2 u_i }{ d s^2 } + \frac{ \mu }{ 4 m a_0 } u_i = \frac{ 1 }{ 4 m } \left[ r f_i (\boldsymbol{u}) + 2 V ( \boldsymbol{u} ) u_i \right] \tag{15}$$
となります.


# 参考文献
* P. Kustaanheimo & E. Stiefel, "Perturbation theory of Kepler motion based on spinor regularization", _J. Reine Angew. Math._, __218__, 204 (1965). doi:[10.1515/crll.1965.218.204](https://doi.org/10.1515/crll.1965.218.204)
* Bruno Cordani, "The Kepler Problem: Group Theoretical Aspects, Regularization and Quantization, with Application to the Study of Perturbations", Springer (2003). doi:[10.1007/978-3-0348-8051-0](http://doi.org/10.1007/978-3-0348-8051-0)
* Alessandra Celletti, "Stability and Chaos in Celestial Mechanics", Springer (2010). doi:[10.1007/978-3-540-85146-2](https://doi.org/10.1007/978-3-540-85146-2)

[^1]: 原論文によると, この変換は P. Kustaanheimo, "Spinor Regularization of the Kepler Motion", _Ann. Univ. Turkuens. A. I._, __73__ (1964) 
において提案されているものと本質的に同じであるようですが, この文献はインターネット上では入手できず, 内容を確認できていません.
