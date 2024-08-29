+++
title = "高次元Vitali集合"
date = 2024-08-29
[extra]
toc = true
[taxonomies]
tags = ["数学", "測度論",]
+++

# 記号

$n$ は正の整数とします. $\mu$ は $\mathbb{R}^n$ の Lebesgue 測度です.

$n$ 次元 Euclid 空間 $\mathbb{R}^n$ の2点 $x, y \in \mathbb{R}^n$ の和 $x+y$ および不等号 $x \leq y$ を, 
成分表示 $x = ( x_1, \cdots, x_n )$, $y = (y_1, \cdots, y_n)$ を用いて
$$x+y = (x_1+y_1, \cdots, x_n+y_n)$$
$$x \leq y \ \ \Leftrightarrow \ \  x_i \leq y_i \ \ (i = 1, \cdots, n)$$
と定義します. 点 $x \in \mathbb{R}^n$ および $\mathbb{R}^n$ の部分集合 $A \subseteq \mathbb{R}^n$ に対して,
集合 $x + A \subseteq \mathbb{R}^n$ を
$$x + A = \\{ x + a \mid a \in A \\}$$
により定義します. 


# 本論

## Vitali 集合の構成

2点 $x, y \in \mathbb{R}^n$ に関して,
$$x - y \in \mathbb{Q}^n$$
であるとき $x \sim y$ と書くことにすると, これは $\mathbb{R}^n$ の同値関係です.
そこでこの同値関係 $\sim$ による $\mathbb{R}^n$ の商 $\mathbb{R}^n / \sim$ について考えます.
この操作は, $\mathbb{R}^n$ および $\mathbb{Q}^n$ を加法に関する群とみるとき, $\mathbb{Q}^n$ は $\mathbb{R}^n$ の部分群ですから,
その剰余類 $\mathbb{R}^n / \mathbb{Q}^n$ を考えることになっています.
点 $x \in \mathbb{R}^n$ の同値類は
$$x + \mathbb{Q}^n = \left\\{ x + q \mid q \in \mathbb{Q}^n \right\\}$$
です.

選択公理により, すべての同値類 $x + \mathbb{Q}^n \in \mathbb{R}^n / \mathbb{Q}^n$ から代表元 $x \in \mathbb{R}^n$ を得ることができます.
特に, この代表元を超立方体
$$\gamma = [0, 1]^n$$
から選ぶことは常に可能です. このような代表元の集まりを $V$ と書き, ($n$ 次元) __Vitali 集合__ といいます.
言い換えると, Vitali 集合とは超立方体 $\gamma$ の部分集合であって, その任意の2元 $v_1, v_2 \in V$ に関して
$$v_1 \sim v_2 \ \ \Rightarrow \ \ v_1 = v_2$$
が成り立ち, なおかつ任意の $x \in \mathbb{R}^n$ に対して
$$x = v + q$$
となるような $v \in V$, $q \in \mathbb{Q}^n$ が存在するものです.


## Vitali 集合の性質

Vitali 集合 $V$ に対して集合 $q + V$ ($q \in \mathbb{Q}^n$) を考えると, 
$q_1 \neq q_2$ のとき $q_1 + V$ と $q_2 + V$ は互いに素です. 
実際, $(q_1 + V) \cap (q_2 + V)$ の元 $x$ が存在したと仮定すると, ある $v_1, v_2 \in V$ が存在して
$$x = q_1 + v_1 = q_2 + v_2$$
が成立します. 従って 
$$v_2 = v_1 + (q_1 - q_2)$$
であり $v_1 \sim v_2$ となりますが, Vitali 集合の構成からこのことは $v_1 = v_2$ すなわち $q_1 = q_2$ を導きます.

さらに, 任意の $x \in \mathbb{R}^n$ に対して $x = q + v$ となる $q \in \mathbb{Q}^n$, $v \in V$ が存在することから
$$\mathbb{R}^n = \bigcup_{q \in \mathbb{Q}^n} ( q + V )$$
です. 上述のことから右辺の和集合は直和になっています.

$C = (\mathbb{Q} \cap [-1, 1])^n$ とおきます. このとき集合
$$U = \bigcup_{q \in C} (q + V)$$
(この和集合も直和です) は
$$[0, 1]^n \subseteq U \subseteq [-1, 2]^n$$
を満たします. 実際, $V \subseteq [0, 1]^n$ ですから $r \in [-1, 1]^n$ のとき $r + V \subseteq [-1, 2]^n$ です.
また $[0, 1]^n$ の任意の元 $x \in [0, 1]^n$ について, Vitali 集合の構成から
$$x = v + q$$
となるような $v \in V$, $q \in \mathbb{Q}^n$ が存在しますが, 
$$(0, \cdots, 0) \leq x \leq (1, \cdots, 1)$$
$$(0, \cdots, 0) \leq v \leq (1, \cdots, 1)$$
により $q = x - v$ は
$$(-1, \cdots, -1) \leq q \leq (1, \cdots, 1)$$
を満たします. よって $q \in C$ であり, $x = v + q \in U$ です.


## Lebesgue 非可測性

Vitali 集合 $V$ は Lebesgue 非可測集合であることを証明します.
それが Lebesgue 可測であったと仮定しましょう. 従って $\mu(V) \in \mathbb{R} \cup [-\infty, \infty]$ が定義できます.
Lebesgue 測度の並進不変性により, 任意の $q \in \mathbb{Q}^n$ に対して $q + V$ は Lebesgue 可測であり
$$\mu(q + V) = \mu(V)$$
が成り立ちます. よって, 上述の集合 $U$ に関して, これもまた Lebesgue 可測であり
$$\mu(U) = \sum_{q \in C} \mu(q+V) = \sum_{q \in C} \mu(V)$$
です. ところが包含関係
$$[0, 1]^n \subseteq U \subseteq [-1, 2]^n$$
の Lebesgue 測度を取ると
$$1 = \mu([0,1]^n) \leq \sum_{q \in C} \mu(V) \leq \mu([-1, 2]^n) = 3^n$$
ですが, $C$ が可算無限集合であるため, この不等式が成り立つような $\mu(V)$ は存在しません.
故に Vitali 集合は Lebesgue 非可測です.


# 参考文献
* [NonMeasurableSets.pdf](https://e.math.cornell.edu/people/belk/measuretheory/NonMeasurableSets.pdf)
* [measure theory - Vitali set in higher dimensions - Mathematics Stack Exchange](https://math.stackexchange.com/questions/3159423/vitali-set-in-higher-dimensions)
