+++
title = "ガンマ行列の一意性"
date = 2021-06-07
[extra]
toc = true
[taxonomies]
tags = ["物理学", "場の量子論", ]
+++

ガンマ行列の一意性 (Pauli の基本定理) は結果のみ紹介されることが多く, 証明が見つけにくいのでここで証明を与えます.
ここで紹介するものは表現論を用いない初等的なものです.


# はじめに

本記事では $D$ 次元 Euclid 空間におけるガンマ行列 $\Gamma_\mu$ ($\mu = 1, 2, \cdots, D$) について考えます. 
その定義は Clifford 関係式
$$\Gamma_\mu \Gamma_\nu + \Gamma_\nu \Gamma_\mu = 2 \delta_{\mu \nu}$$
です ($\delta_{\mu \nu}$ は Kronecker デルタ). ガンマ行列の次数 $N$ は $N = 2^{\lfloor D / 2 \rfloor}$ です.
Minkowski 時空での対応物などの詳細については以前の記事「[高次元ガンマ行列](@/2021/03/01-gamma-matrix.md)」を参照してください.

## Pauli の基本定理

時空次元 $D$ は偶数とし, $N = 2^{D / 2}$ とおきます. このとき, Clifford 関係式を満たす任意の二組の $N$ 次正方行列の組 $\Gamma_\mu$ ($\mu = 1, \cdots, D$), 
$\Lambda_\mu$ ($\mu = 1, \cdots, D$) に対して, 正則行列 $F$ が存在し
$$\Lambda_\mu = F \Gamma_\mu F^{-1}$$
が成立します. 


# ガンマ行列の積

Pauli の基本定理を証明する準備として, 任意個のガンマ行列の積が生成する $\mathbb{C}$-ベクトル空間
$$X = \left\langle I, \ \Gamma_\mu, \ \Gamma_\mu \Gamma_\nu , \ \Gamma_\mu \Gamma_\nu \Gamma_\rho , \ \cdots, \ \Gamma_1 \cdots \Gamma_D \right\rangle$$
について考えます. 2個の相異なるガンマ行列の積 $\Gamma_\mu \Gamma_\nu$ ($\mu \neq \nu$) は Clifford 関係式より
$$\Gamma_\mu \Gamma_\nu = - \Gamma_\nu \Gamma_\mu$$
を満たす, つまり反可換です. $\mu = \nu$ のとき Clifford 関係式から $( \Gamma_\mu )^2 = I$ となることから, 
$D + 1$ 個以上のガンマ行列の積は, 順序を入れ替えれば $\Gamma_\mu$ と $\Gamma_\mu$ の積をくくり出すことができ,
それを単位行列に置き換えることで常に $D$ 個以下のガンマ行列の積に帰着できます.

従って独立なものは $\Gamma_\mu \Gamma_\nu \cdots \Gamma_\rho$ ($\mu < \nu < \cdots < \rho$) という形の積のみです. 
その総数は外積代数の次元を求める計算と同じで
$$\sum_{k = 0}^D \binom{N}{k} = 2^D$$
です. この $2^D$ 個の行列を $\Gamma_A$ ($A = 0, 1, \cdots, 2^D-1$) と書くことにします ($0$ 始まりなのは $\Gamma_\mu$ を最初の定義と一致させたかったからです).
なお $A = 2^D - 1$ に対応する行列を $\Gamma_\Omega$ とも書きます.
$$\Gamma_\Omega = \Gamma_1 \Gamma_2 \cdots \Gamma_D$$


## $\Gamma_A$ のトレース

ガンマ行列のトレースは空間次元の偶奇によって振る舞いが異なります. 
偶数次元のときに限ってすべての $A \neq 0$ について $\mathrm{tr} ( \Gamma_A ) = 0$ であることが証明できます.

$\Gamma_\mu$ について, $( \Gamma_\nu )^2 = I$ であることから, $\mu \neq \nu$ に対して
$$\mathrm{Tr} ( \Gamma_\mu ) = \mathrm{Tr} ( \Gamma_\mu \Gamma_\nu \Gamma_\nu ) .$$
ここでガンマ行列の反対称性から右辺は $- \mathrm{Tr} ( \Gamma_\nu \Gamma_\mu \Gamma_\nu )$ と書き換えられるのですが,
トレースの性質からこれはさらに $- \mathrm{Tr} ( \Gamma_\mu \Gamma_\nu \Gamma_\nu )$ と変形できます. 故に
$$\mathrm{Tr} ( \Gamma_\mu ) = - \mathrm{Tr} ( \Gamma_\mu )$$
からこのトレースはゼロです. 

次に $\Gamma_\Omega = \Gamma_1 \Gamma_2 \cdots \Gamma_D$ のトレースについて考えます. 上と同様に
$$\mathrm{Tr} ( \Gamma_\Omega ) = \mathrm{Tr} ( \Gamma_D \Gamma_1 \cdots \Gamma_{D-1} )$$
ですから, 反可換性を用いて $\Gamma_D$ を右端まで移動するとこれは $( -1 )^{D-1} \mathrm{Tr} ( \Gamma_1 \cdots \Gamma_D )$ を与えます. よって
$$\left[ 1 + ( - 1 )^D \right] \mathrm{Tr} ( \Gamma_\Omega ) = 0$$
が導かれますが, $D$ が偶数のときのみここから
$$\mathrm{Tr} ( \Gamma_\Omega ) = 0$$
が結論できます (奇数次元では成立しません).

ここで $\Gamma_\Omega$ は次の性質を満足することに注意します.
$$( \Gamma_\Omega )^2 = \epsilon_D I , \ \ \epsilon_D = \begin{cases} +1 & D \equiv 0, 1 \ \mathrm{mod} \ 4 \\\\ -1 & D \equiv 2, 3 \ \mathrm{mod} \ 4\end{cases}$$
$$\Gamma_\Omega \Gamma_\mu + ( -1 )^D \Gamma_\mu \Gamma_\Omega = 0$$
特に, 偶数次元では $\Gamma_\Omega$ は $\Gamma_\mu$ と反可換です. このことを用いて, 
偶数次元では奇数個の $\Gamma_\mu$ の積のトレースはすべてゼロであることを示しましょう.
$$\mathrm{Tr} ( \overbrace{\Gamma_\mu \cdots \Gamma_\nu}^n ) = \frac{ 1 }{ \epsilon_D } \mathrm{Tr} ( \Gamma_\Omega \Gamma_\Omega \overbrace{\Gamma_\mu \cdots \Gamma_\nu}^n )$$
において, ひとつの $\Gamma_\Omega$ をトレースの性質を用いて右端に移動します.
$$\frac{ 1 }{ \epsilon_D } \mathrm{Tr} ( \Gamma_\Omega \overbrace{\Gamma_\mu \cdots \Gamma_\nu}^n \Gamma_\Omega )$$
残された左端の $\Gamma_\Omega$ を反可換性を用いて右端に移動すると, 符号 $( - 1 )^n$ が生じます.
従って $n$ が奇数ならば上と同様の論法によって $\mathrm{Tr} ( \overbrace{\Gamma_\mu \cdots \Gamma_\nu}^n )$ がゼロであることが従います.

残るは偶数個の相異なる $\Gamma_\mu$ の積ですが, これは
$$\mathrm{Tr} ( \overbrace{\Gamma_\mu \cdots \Gamma_\nu}^n )$$
の右端の $\Gamma_\nu$ を左端に移動し, 反可換性を用いて右端に移動すれば符号 $( - 1 )^{n - 1}$ が生じることから同様にゼロです
(これは一般次元で成立しますが, 同一の $\Gamma_\mu$ が複数個含まれる場合には適用できません).


## $\Gamma_A$ の線型独立性

この段階で, $\Gamma_A$ ($A = 0, 1, \cdots, 2^D-1$) が線型独立であることが証明できます.
このことはベクトル空間 $X$ の次元が $2^D$ であり, 従って $N = 2^{D/2}$ 次正方行列の全体に一致することを意味します[^1].

$\Gamma_A$ の線型結合がゼロであると仮定します.
$$\sum_A c_A \Gamma_A = 0$$
両辺に $\Gamma_B$ を乗じてトレースを取ると, 右辺はゼロを与えます. 左辺の項 $\Gamma_A \Gamma_B$ について, 
これを構成する $\Gamma_\mu$ について添え字の昇順に並び替え, 同一の $\Gamma_\mu$ は $( \Gamma_\mu )^2 = I$ となることを用いて消去すると,
$\pm 1$ 倍を除いてある $\Gamma_C$ に一致します.
特に $A = B$ のときには $\Gamma_C = I$ まで帰着できますが, そうでなければ相異なる $\Gamma_\mu$ が残ります.
従ってそのトレースは $A = B$ のときのみゼロでない値を取り, それ故に左辺の和からは
$A = B$ となる項だけが残ります. 故に $c_B = 0$ が導かれ, $B$ が任意であることからこれによって $\Gamma_A$ の線型独立性が示されました.


# Pauli の基本定理の証明

偶数次元時空において, Clifford 関係式を満足する $\Gamma_\mu$ および $\Lambda_\mu$ について, 両者が相似変換により結ばれることを示します.

## 準備

線型独立性の議論で行った, $\Gamma_A \Gamma_B$ を Clifford 関係式を用いて整理しある $\Gamma_C$ へと帰着させる操作について考えます[^2].
これを
$$\Gamma_A \Gamma_B = g ( A, B ) \Gamma_{C ( A, B )}$$
と書くとき, この操作は Clifford 関係式のみによって定義されているため, $\Lambda_A$ についても同じ関係が成立します.
$$\Lambda_A \Lambda_B = g ( A, B ) \Lambda_{C ( A, B )}$$

ガンマ行列の組 $\Gamma_0$, $\Gamma_1$, ..., $\Gamma_\Omega$ に左から $\Gamma_A$ を乗じ, $2^D$ 個の行列
$$\Gamma_A \Gamma_0 , \ \ \Gamma_A \Gamma_1 , \ \ \cdots, \ \ \Gamma_A \Gamma_\Omega$$
を得る写像について, 象 $\Gamma_A \Gamma_B$ は相異なります (つまり, これは単射です). 
実際, $\Gamma_A \Gamma_{B_1} = \Gamma_A \Gamma_{B_2}$ であるならば, $( \Gamma_A )^2$ は単位行列の $\pm 1$ 倍ですから,
左から $\Gamma_A$ を乗じれば $\Gamma_{B_1} = \Gamma_{B_2}$ が得られます. 
$\Gamma_B$ ($B = 0, 1, \cdots, 2^D-1$) が線型独立であることから, このことは $B_1 = B_2$ を意味します.
故に, この写像は $\pm 1$ 倍を除くと $\Gamma_A$ の並び替えに他なりません.

## 証明

任意の $N$ 次正方行列 $K$ に対して
$$\tilde{K} = \sum_A \Lambda_A K ( \Gamma_A )^{-1}$$
という行列を定義します. $\tilde{K} \Gamma_B$ という行列について,
$( \Gamma_B )^2 = ( \Lambda_B )^2 = \epsilon_B I$ ($\epsilon_B = g ( B, B ) = \pm 1$) に注意してこれを
$$\tilde{K} \Gamma_B = \frac{ 1 }{ \epsilon_B } \Lambda_B \left( \sum_A \Lambda_B \Lambda_A K ( \Gamma_A )^{-1} \epsilon_B ( \Gamma_B )^{-1} \right)$$
と書き直します.
$$\Lambda_B \Lambda_A = g ( B, A ) \Lambda_{C ( B, A )} ,$$
$$( \Gamma_A )^{-1} ( \Gamma_B )^{-1} = ( \Gamma_B \Gamma_A )^{-1} = \frac{ 1 }{ g ( B, A ) } ( \Gamma_{C ( B, A )} )^{-1}$$
によりこれは
$$\tilde{K} \Gamma_B = \Lambda_B \left( \sum_A \Lambda_{C ( B, A )} K ( \Gamma_{C ( B, A )} )^{-1} \right)$$
に帰着されますが, $B$ を固定して $A$ が $0$ から $2^D-1$ までを走るとき, $C ( B, A )$ それ自体も $0$ から $2^D - 1$ を走るため, 
この和の添え字を $C$ に置き換えることができます. よってこの和は $\sum_C \Lambda_C K ( \Gamma_C )^{-1} = \tilde{K}$ となり, 等式
$$\tilde{K} \Gamma_B = \Lambda_B \tilde{K} \tag{*}$$
が結論されます.

同様に, 任意の $N$ 次正方行列 $L$ に対して
$$\hat{L} = \sum_A \Gamma_A L ( \Lambda_A )^{-1}$$
とおくとき, $\hat{L} \Lambda_B = \Gamma_B \hat{L}$ が成立します. これらの結果から
$$\hat{L} \tilde{K} \Gamma_B = \Gamma_B \hat{L} \tilde{K}$$
が従いますが, $\Gamma_B$ は $N$ 次正方行列がなす $\mathbb{C}$-ベクトル空間の基底ですから, 
このことは $\hat{L} \tilde{K}$ という行列が任意の行列と可換であることを意味します.
ところがそのような行列は単位行列の複素数倍しかありません ([参考](https://wasan.hatenablog.com/entry/2016/04/20/215854)).
つまり, 任意のふたつの $N$ 次正方行列 $K$, $L$ に対して
$$\hat{L} \tilde{K} = a ( L, K ) I$$
となるような複素数 $a ( L, K )$ が常に存在します.

ある $K$, $L$ に対して $a ( L, K )$ はゼロではない値を取ることを背理法で示します.
任意の $K$, $L$ について $\hat{L} \tilde{K} = 0$ であるならば, これを $K$ で微分することにより
$$\sum_A \left[ \hat{L} \Lambda_A \right]_{i j} \left[ \Gamma_A \right]\_{k l} = 0$$
という等式が得られます ($i$, $j$, $k$, $l$ は行列添え字). これを $k$, $l$ を添え字とする行列に関する等式と見ると,
$\Gamma_A$ の線型独立性により
$$\hat{L} \Lambda_A = 0$$
が導かれます. 特に $A = 0$ とすると $\hat{L} = 0$ でなければなりません. 
これを $L$ で微分すると, 同様に $\Gamma_A = 0$ が導かれますが, これは Clifford 代数を満足しないため, 矛盾します.

$a ( L, K ) \neq 0$ となるような $K$ と $L$ について, $\frac{ 1 }{ a ( L, K ) } \hat{L} \tilde{K} = I$ により $\tilde{K}$ は可逆行列となります.
そこで式 (*) の両辺に $\tilde{K}^{-1}$ を右から乗じれば
$$\Lambda_B = \tilde{K} \Gamma_B \tilde{K}^{-1}$$
となります. すなわち, Clifford 代数を満足する任意の二組のガンマ行列は相似変換により結ばれます. ∎


# 参考文献
* 益川敏英『いま、もう一つの素粒子論入門』丸善 (1998).
* [Gamma matrices - Wikipedia](https://en.wikipedia.org/wiki/Gamma_matrices)
* [Lecture note on Clifford algebra - Jeong-Hyuck Park](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.519.7273&rep=rep1&type=pdf)
* D. S. Shirokov, _Extension of Pauli’s Theorem to Clifford Algebras_, Doklady Mathematics, __84__, 2, 699-701 (2011). doi:[10.1134/S1064562411060329](https://doi.org/10.1134/S1064562411060329)
* [Pauli の原論文の英訳](http://www.neo-classical-physics.info/uploads/3/4/3/6/34363841/pauli_-_dirac_matrices.pdf)


[^1]: このことから $D$ 次元時空においてガンマ行列は $N = 2^{D/2}$ 次以上の正方行列でなければならないことがわかります.

[^2]: 例えば3次元では Pauli 行列 $\sigma_1$, $\sigma_2$, $\sigma_3$ がガンマ行列を与えますが,
$\sigma_1 \sigma_2 \sigma_3 = i I$ という非自明な関係式を用いれば $\sigma_1 \sigma_2 \sigma_3$ を単位行列の定数倍まで帰着させることはできます.
しかしここで考えている操作は Clifford 関係式のみを用いるものであり, このような非自明な簡約は行いません.
