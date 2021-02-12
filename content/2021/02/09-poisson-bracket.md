+++
title = "Poisson括弧の符号について"
date = 2021-02-09
[extra]
toc = true
[taxonomies]
tags = ["物理学", "解析力学", "シンプレクティック幾何学", ]
+++

Landau & Lifshitz が逆符号で定義しているのもあり Poisson 括弧の符号についていつも混乱するので,
いつでも見直せるように丁寧にまとめておきます.

# Poisson 括弧

$n$ 自由度の Hamilton 系について, その正準座標を $( p_i, q_i )$ とします.
任意の物理量 $f ( p, q )$, $g ( p, q )$ について, その Poisson 括弧を
$$\left\\{ f, g \right\\} = \sum_{i = 1}^n \left( \frac{ \partial f }{ \partial q_i } \frac{ \partial f }{ \partial p_i } - \frac{ \partial f }{ \partial p_i } \frac{ \partial g }{ \partial q_i } \right)$$
により定義します. このように定義すると, Poisson 括弧は
$$\\{ q_i, p_j \\} = \delta_{i j}$$
を満足し, 量子力学における正準交換関係 $[ q_i, p_j ] = i \hbar \delta_{i j}$ と符号を含めて対応します.

この定義では, 任意の物理量 $f$ の時間発展を記述する Liouville 方程式は
$$\frac{ d f }{ d t } = \left\\{ f, H \right\\} + \frac{ \partial f }{ \partial t }$$
となり, やはり Heisenberg 方程式
$$i \hbar \frac{ d f }{ d t } = \left[ f, H \right]$$
と対応します.

主要な古典力学の教科書その他について, Poisson 括弧の符号についてまとめておきます.
+1が上記定義と一致するもの, -1が反対符号です (他の列については下を参照).

| author            | PB | $\omega$       | ♭  |
|:-----------------:|:--:|:--------------:|:---:|
| Landau & Lifshitz | -1 | -              | -   |
| Arnold            | -1 | $dp \wedge dq$ | 2nd |
| 山本 & 中村       | +1 | $dp \wedge dq$ | 2nd |
| 本記事            | +1 | $dp \wedge dq$ | 1st |
| 深谷              | +1 | $dp \wedge dq$ | 1st |
| Goldstein         | +1 | $dq \wedge dp$ | 1st |
| Abraham & Marsden | +1 | $dq \wedge dp$ | 1st |
| 大貫 & 吉田       | +1 | $dq \wedge dp$ | -   |
| enwp, jawp        | +1 | $dq \wedge dp$ | 1st |

この表を見るに, ソ連では反対符号が普及していたようです.
それ以外の部分は... 見事にバラバラです. Goldstein 方式が比較的優勢でしょうか.


# シンプレクティック形式

$2 n$ 次元多様体 $M$ 上の非退化な閉 2-形式 $\omega$ が与えられたとき, 
組 $( M, \omega )$ をシンプレクティック多様体と呼ぶのでした.
Darboux 座標 $( p, q )$ では $\omega$ を
$$\omega = \sum_{i = 1}^n dp^i \wedge dq^i = \sum_i \left( dp^i \otimes dq^i - dq^i \otimes dp^i \right)$$
と表示することができます. 
この定義は Arnold および深谷に従うものですが, $p$ と $q$ を逆に表示する場合もあり, 
Goldstein および Abraham & Marsden や enwp はこちらの流儀です.

さて, $M$ 上のベクトル場 $X$ が与えられたとき,
シンプレクティック形式 $\omega$ は
$$X^\flat \left( \cdot \right) = \omega \left( X, \cdot \right)$$
により余ベクトル場 $X^\flat$ を定めます. 逆に, 余ベクトル場 $\alpha$ は
$$\alpha \left( \cdot \right) = \omega \left( \alpha^\sharp, \cdot \right)$$
によりベクトル場 $\alpha^\sharp$ を定めます. 
明らかにこのふたつの写像 $\flat$, $\sharp$ は逆写像の関係にあります (音楽同型).
なお $X^\flat$ のことを $\omega^\flat ( X )$ または $i_X \omega$ とも書きます.
この定義は深谷, Abraham & Marsden (および enwp, jawp) と一致します.
ただし Arnold および山本&中村は第2引数との縮約として定義しているため, 符号が逆です.

具体的に Darboux 座標 $( p, q )$ を取るとき, ベクトル場 $X$ を座標基底で展開すると
$$X = \sum_{i = 1}^n \left( X^{p, i} \frac{ \partial }{ \partial p^i } + X^{q, i} \frac{ \partial }{ \partial q^i } \right)$$
と書けます. このとき $X^\flat$ は
$$X^\flat = \sum_{i = 1}^n \left( X^{p, i} dq^i - X^{q, i} dp^i \right)$$
により与えられます. また, 余ベクトル場 
$$\alpha = \sum_{i = 1}^n \left( \alpha_{p, i} dp^i + \alpha_{q, i} dq^i \right)$$
の $\sharp$ 写像の像は
$$\alpha^\sharp = \sum_{i = 1}^n \left( \alpha_{q, i} \frac{ \partial }{ \partial p^i } - \alpha_{p, i} \frac{ \partial }{ \partial q^i } \right)$$
です.


# Hamilton ベクトル

$M$ 上の関数 $f: M \to \mathbb{R}$ について, 付随する Hamilton ベクトル $X_f$ を
$$X_f = - d f^\sharp$$
により定義します. 深谷の定義ではマイナスがありませんが, その定義では正準方程式に一致しません.
Arnold および山本&中村の定義では, 音楽同型の定義が逆符号である結果, やはりこの定義からマイナス符号が除かれています.
Goldstein, Abraham & Marsden および enwp では, $\omega$ の符号がこことは逆であるため, やはりマイナス符号は現れません.

前節の結果から Darboux 座標 $( p, q )$ ではこれは
$$X_f = \sum_{i = 1}^n \left( - \frac{ \partial f }{ \partial q^i } \frac{ \partial }{ \partial p^i } + \frac{ \partial f }{ \partial p^i } \frac{ \partial }{ \partial q^i } \right)$$
を意味します. 従って Hamilton の正準方程式は Hamilton ベクトル場の積分曲線のことであると言い換えることができます.
(というよりも, そうなるように $X_f$ を定義します. 従って $X_f$ の座標表示は深谷を除いてすべて一致します.)


# Poisson 括弧 (2)

以上の定義のもとでは, $f$ と $g$ の Poisson 括弧は
$$\\{ f, g \\} = - \omega ( X_f, X_g )$$
と表せます. 山本&中村と式の上では一致します.
深谷では Hamilton ベクトルの定義が逆ですからマイナスはつきません.
Arnold では Poisson 括弧の定義が逆ですからマイナスはつきません.
Goldstein や Abraham & Marsden, enwp では $\omega$ の符号が逆ですからマイナスはつきません.

以下の表式は Poisson 括弧の符号が +1 ならば一致します (深谷を除く).
$$\\{ f, g \\} = df ( X_g ) = X_g ( f )$$
$$X_{\\{f, g\\}} = - [ X_f, X_g ]$$


# 参考文献

* L. Landau & E. M. Lifshitz, "Mechanics", Pergamon, 1969
* V. I. Arnold, "Mathematical Methods of Classical Mechanics", Springer, 1989
* H. Goldstein, C. Poole & J. Safko, "Classical Mechanics", Pearson, 2001
* Ralph Abraham & Jerrold E. Marsden, "Foundations of Mechanics", Benjamin-Cummings, 2008
* 山本義隆, 中村孔一, 「解析力学」, 朝倉書店, 1998
* 深谷賢治, 「解析力学と微分形式」 岩波書店, 2004
* 大貫義郎, 吉田春夫, 「力学」, 岩波書店, 1994
* [https://en.wikipedia.org/wiki/Poisson_bracket](https://en.wikipedia.org/wiki/Poisson_bracket)
* [https://ja.wikipedia.org/wiki/ポアソン括弧](https://ja.wikipedia.org/wiki/%E3%83%9D%E3%82%A2%E3%82%BD%E3%83%B3%E6%8B%AC%E5%BC%A7)
