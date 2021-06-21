+++
title = "時間に依存しないSchrödinger方程式？"
date = 2021-06-21
[taxonomies]
tags = ["物理学", "量子力学"]
+++

化学の教科書を眺めていると, 「時間に依存する Schrödinger 方程式」, 
「時間に依存しない Schrödinger 方程式」という物理学では用いられない言い回しが現れます.
私としてはこれはそれぞれ「Schrödinger 方程式」, 「Hamiltonian 固有値方程式」と呼ぶべきではないかと思います.

という話を以前知人としたのですが, 備忘録がてらまとめておきます.
別に専門用語なんて界隈で通じれば十分なので実際に用語法を変更して欲しい訳ではないのですが.


# Schrödinger 方程式とはなにか

量子系の状態はある Hilbert 空間[^1]のベクトル $| \psi \rangle$ により表され,
時間発展はこの Hilbert 空間上のユニタリ作用素 $U ( t )$ により表現されます.
すなわち, (Schrödinger 描像では) 時刻 $t$ に系が状態 $| \psi, t \rangle$ にあったならば,
時刻 $t'$ の状態 $| \psi, t' \rangle$ は
$$| \psi, t' \rangle = U ( t' - t ) | \psi, t \rangle$$
により与えられます. そこで $t' \to t$ の極限について考えると, Hamiltonian 
$$H = \frac{ 1 }{ i \hbar } \left. \frac{ d U }{ d t } \right|_{t \to 0}$$
を導入すると, 上式は
$$i \hbar \frac{ d }{ d t } | \psi, t \rangle = H | \psi, t \rangle$$
に帰着されます. これが Schrödinger 方程式です.
Schrödinger 方程式は系の時間発展が連続なユニタリ変換であるという一般的な原則だけからの帰結であって,
系を構成する粒子の数や種類, また相対論的であるかどうかによらず適用できます.
もちろん Hamiltonian $H$ の具体形はこれらの情報に依存します.

Schrödinger 方程式は系の時間発展を記述するものなのですから,
「時間に依存する Schrödinger 方程式」という表現は「馬から落馬した」と同じ重言に聞こえます.


# 時間に依存しない Schrödinger 方程式

それでは「時間に依存しない Schrödinger 方程式」とは何でしょうか？ 方程式
$$H | \psi \rangle = E | \psi \rangle$$
は Hamiltonian $H$ の固有値 $E$ および固有ベクトル $| \psi \rangle$ を定めるもので,
つまり Hamiltonian の固有値方程式に過ぎません.
ですから「時間に依存しない Schrödinger 方程式」という謎用語を導入せずとも, 
そのまま「Hamiltonian 固有値方程式」と呼べば十分でしょう.
その方が方程式が表す内容も明白ですし.


[^1]: この Hilbert 空間という物理学の用語法にも思うところがありますが,
それはこの記事の主題とは関係がないので置いておきます.
