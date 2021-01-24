+++
title = "三項間漸化式の漸近的振る舞い"
date = 2021-01-25
[extra]
toc = true
[taxonomies]
tags = ["数学", "数値解析"]
+++

__三項間漸化式__ (three-term recurrence relation, TTRR) は直交多項式や特殊関数の理論において重要な役割を果たします.
そこで本記事では三項間漸化式の基本的な振る舞いについて述べます.

複素係数の漸化式について議論しますが, 当然, 実係数でも構いません.
また応用上の動機から三項間漸化式に限定しますが, $k$ 項間漸化式へと拡張できます (Lantsman を参照してください).


# 定義

次の三項間漸化式を満足する数列 $y = ( y_k )$ ($k \in \mathbb{N}$) について考える.
$$y_{n+1} + b_n y_n + a_n y_{n-1} = c_n \ \ (n = 1, 2, 3, \cdots)$$
ただし $a_n \neq 0$ ($\forall n$) とする. 
$a_n = -1$ ($\forall n$) が成り立つとき, この漸化式は __対称__ (symmetric) であるといい,
また $c_n = 0$ ($\forall n$) であるとき __斉次__ (homogeneous), そうでないとき __非斉次__ (inhomogeneous) であるという.
本記事では斉次漸化式に議論を限定し, 以下漸化式とは斉次三項間漸化式のことを指すものとする.

三項間漸化式を満足する数列は最初の2項 $y_0$ および $y_1$ によって一意に特定される:.
特に, 所与の斉次三項間漸化式を満足する数列の全体は2次元 $\mathbb{C}$-ベクトル空間[^3]をなす.
この線型構造に関してふたつの数列 $f$, $g$ が一次独立であるための必要十分条件は, __Casorati 行列式__
$$D ( n, n+1 ) = f_n g_{n+1} - f_{n+1} g_n$$
がゼロでないことである. 実際, 漸化式の表式からただちに $n \geq 1$ のとき
$$D ( n, n+1 ) = - a_{n+1} D ( n-1, n )$$
が成立することが導かれるため, 任意の $D ( n, n+1 )$ がゼロであるかは 
$D ( 0, 1 )$ がゼロであるかと同値である.
そして $D ( 0, 1 )$ がゼロであるかは $( p_0, p_1 )$ と $( q_0, q_1 )$ が線型従属であるかと同値である.


# 定数係数三項間漸化式

係数 $b_n$, $a_n$ が $n$ によらない定数である場合, TTRR は解析的に解くことができる.
等比数列解 $y_n \propto \lambda^n$ について考えると, $\lambda$ は __特性多項式__ (characteristic polynomial)
$$\lambda^2 + b \lambda + a = 0$$
を満足する. よってそれが重根ではない2つの解 $\lambda_1$, $\lambda_2$ を持つのであれば,
${\lambda_1}^n$ と ${\lambda_2}^n$ が TTRR のふたつの独立な解を与える.
一方, 特性多項式が重根を持つとき (すなわち $b^2 - 4 a = 0$ であるのならば), その重根 $\lambda$ からふたつの独立解が $\lambda^n$, $n \lambda^n$ と定まる.


# 一般の TTRR の漸近的振る舞い

定数係数の TTRR の線型独立解は (特性多項式が重根を持つ場合を除いて) 等比数列である.
実用上重要な $b_n$, $a_n$ が $n$ に依存する場合 (特に $n$ の有理関数である場合) には, 一般解が求まることは期待できない.
しかし以下に述べる定理によると, その $n \to \infty$ での漸近的な振る舞いは定数係数の場合と非常によく似ており,
等比級数的になる.

## Poincaré-Perron の定理

Poincaré-Perron の定理は以下のように述べられる (前半を Poincaré の定理, 後半を Perron の定理と呼ぶ):

* 数列 $y_n$ に関する斉次三項間漸化式 $y_{n+1} + b_n y_n + a_n y_{n-1} = 0$ について, 極限
$$\lim_{n \to \infty} a_n = a, \ \ \lim_{n \to \infty} b_n = b$$
が存在すると仮定する. この極限値に対応する特性多項式 $\lambda^2 + b \lambda + a$ の2つの根 $\lambda_1$, $\lambda_2$ が 
$|\lambda_1 | \neq | \lambda_2 |$ を満たすならば,
漸化式の任意の非自明解[^1] $y$ について, ある $\lambda_j$ が存在し
$$\lim_{n \to \infty} \frac{ y_{n+1} }{ y_n } = \lambda_j$$
が成立する. 一方 $| \lambda_1 | = | \lambda_2 |$ であるならば, 任意の非自明解 $y_n$ は
$$\limsup_{n \to \infty} \left| y_n \right|^\frac{1}{n} = \left| \lambda_1 \right|$$
を満足する.
* 上の状況で $a_n$ が有限個を除いてゼロではないと仮定する. 
$| \lambda_1 | \neq | \lambda_2 |$ であるならば, TTRR にはふたつの線型独立解 $f$, $g$ が存在し
$$\lim_{n \to \infty} \frac{ f_{n+1} }{ f_n } = \lambda_1 , \ \ \lim_{n \to \infty} \frac{ g_{n+1} }{ g_n } = \lambda_2$$
を満たす.

証明は Lantsman の pp. 380-392 を見よ.

## Perron-Kreuser の定理

係数 $b_n$, $a_n$ が $n$ のべき乗へと漸近する場合に Poincaré-Perron の定理を一般化したものが Perron-Kreuser の定理である:

* 数列 $y_n$ に関する斉次三項間漸化式 $y_{n+1} + b_n y_n + a_n y_{n-1} = 0$ について, 係数 $b_n$, $a_n$ が $n \to \infty$ で漸近形
$$a_n \sim a n^\alpha , \ \ b_n \sim b n^\beta \ \ (n \to \infty)$$
($a \neq 0$, $b \neq 0$) を持つと仮定する. 
1. $\beta > \alpha / 2$ である場合, TTRR にはふたつの線型独立解 $f$, $g$ が存在し次を満たす:
$$\frac{ f_{n+1} }{ f_n } \sim - \frac{ a }{ b } n^{\alpha - \beta} , \ \ \frac{ g_{n+1} }{ g_n } \sim - b n^\beta .$$
2. $\beta = \alpha / 2$ である場合, 特性多項式 $\lambda^2 + b \lambda + a$ の2つの根 $\lambda_1$, $\lambda_2$ が 
$|\lambda_1 | \neq | \lambda_2 |$ を満たすならば, ふたつの線型独立解 $f$, $g$ が存在し次を満たす:
$$\frac{ f_{n+1} }{ f_n } \sim \lambda_1 n^\beta , \ \ \frac{ g_{n+1} }{ g_n } \sim \lambda_2 n^\beta .$$
一方 $| \lambda_1 | = | \lambda_2 |$ であるならば任意の非自明解 $y_n$ は次を満たす:
$$\limsup_{n \to \infty} \left[ \frac{ | y_n | }{ ( n! )^\beta } \right]^\frac{1}{n} = \left| \lambda_1 \right| .$$
3. $\beta < \alpha / 2$ である場合, 任意の非自明解 $y_n$ は次を満たす:
$$\limsup_{n \to \infty} \left[ \frac{ | y_n | }{ ( n! )^{\alpha / 2} } \right]^\frac{1}{n} = \sqrt{ \left| \lambda_1 \right| } .$$

証明は Gil, Segura & Temme, pp. 93-94 を見よ. 
なおケース 2, 3  は ${\hat{y}}_n = y_n / ( n! )^{\alpha / 2}$ とおき, 
数列 ${\hat{y}}_n$ に Poincaré-Perron の定理を適用することでただちに得られる.
ケース 1 は ${\hat{y}}_n = y_n / ( n! )^\beta$ に Poincaré-Perron の定理を適用することで得られるが, 多少の議論が必要である. 


# minimal solution

所与の TTRR を満足する数列 $f$ がその __minimal solution__ であるとは, $f$ とは線型独立な解 $g$ が存在し
$$\lim_{n \to \infty} \frac{ f_n }{ g_n } = 0$$
を満足することをいう. またこのとき $g$ を __dominant solution__ と呼ぶ.
Poincaré-Perron の定理が適用できる場合, $| \lambda_1 | < | \lambda_2 |$ であるならば, 
$\lambda_1$ に対応する解 $f_n$ が minimal solution, もう一方の $g_n$ が dominant solution である.
Perron-Kreuser の定理が適用できる場合, 場合 1 および場合 2 の $| \lambda_1 | < | \lambda_2 |$ 
の状況では同様に $f_n$ が minimal solution である.
なおこれ以外の状況 ($| \lambda_1 | = | \lambda_2 |$ である場合など) では, 
TTRR に minimal solution が存在するかどうかはこれらの定理からは判定できない.

minimal solution を数値的に計算しようとすると, 
誤差項が dominant solution であるため $n \gg 1$ で誤差項が成長してしまうため, 数値的に安定ではない.
この問題を回避するには, 漸化式を逆向きに使い大きな $N$ に対応する項 $f_N$ から遡ってくることにより $f_n$ を求めればよい.
これを __Miller のアルゴリズム__ と呼ぶ.
逆向き漸化式では minimal solution が dominant に, dominant solution が minimal になるため, これは数値的に安定なスキームである.
詳しくは Gil, Segura & Temme, pp. 105-110 を見よ.


# 参考文献
* Amparo Gil, Javier Segura & Nico M. Temme, _Numerical Methods for Special Functions_, Society for Industrial and Applied Mathematics (2007) doi:[10.1137/1.9780898717822](https://doi.org/10.1137%2F1.9780898717822)
* M. H. Lantsman, _Asymptotics of Linear Differential Equations_, Springer (2001) doi:[10.1007/978-94-015-9797-5](https://doi.org/10.1007/978-94-015-9797-5)

[^3]: 実数係数漸化式で初期値も実に選ぶ場合には実ベクトル空間.

[^1]: 自明解とは, 有限項を除いて $y_n = 0$ であるような解のこと.
