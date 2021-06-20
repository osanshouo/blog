+++
title = "平均律, Pythagoras音律, 純正律"
date = 2021-06-20
draft = true
[taxonomies]
tags = ["音楽", "音響", ]
[extra]
toc = true
+++
<style>
input[type="button"] { 
    border: solid 1px var(--tag-bg-color);
    background: var(--bg-color); 
    color: var(--tag-fg-color);
}
.num3, .num2, .num1, .num0 { text-align: right; display: block; }
.num3 { margin-right: 3.5ch; }
.num2 { margin-right: 2.3ch; }
.num1 { margin-right: 1.1ch; }
.center { text-align: center; display: block; }
</style>

<script>
function sin_wave(freq) {
    console.log(freq);
    let audioctx = new AudioContext();
    let osc = new OscillatorNode(audioctx);
    osc.frequency.value = freq;
    console.log(osc);
    osc.connect(audioctx.destination);
    osc.start();
    osc.stop(5);
}</script>

本記事では[音律](https://ja.wikipedia.org/wiki/%E9%9F%B3%E5%BE%8B) (平均律, Pythagoras 音律, 純正律) についてまとめます.
JavaScript の Web Audio API を用いて実際に音を鳴らして試聴できるようにしました.
なおハ長調ではなくイ長調を採用しています.


# 音と振動数

本記事で扱うような微妙な振動数差を表すために [__セント__](https://ja.wikipedia.org/wiki/%E3%82%BB%E3%83%B3%E3%83%88_(%E9%9F%B3%E6%A5%BD)) 
(cent) という概念を導入する.
基準振動数 $f_0$ を任意に設定し (例えば $f_0 = 442\\,\mathrm{Hz}$), 
任意の振動数 $f$ の音についてそのセントを
$$n ( f ) = 1200 \\, \log_2 \frac{ f }{ f_0 }$$
と定義する. 逆に $n$ セントの音の振動数 $f$ は
$$f = f_0 2^{n / 1200}$$
である.

通常, 振動数 $f$ の音に対して振動数 $2^i f$ ($i$ は整数) の音は __オクターブ__ (octave) の関係にあると呼ばれ, 音高としては同一視される. 
言い換えると, ちょうど 1200 セントの差を持つ音を同一視する.


# 平均律

対数空間で等間隔に取った音高のことを [__平均律__](https://ja.wikipedia.org/wiki/%E5%B9%B3%E5%9D%87%E5%BE%8B) 
(equal temperament) と呼び, 現代では標準的に用いられる.
つまり, 平均律では 0, 100, 200, $\cdots$, 1100 セントに対応する音のみが用いられる.
これを順に A, B, H, C, Cis, D, Dis, E, F, Fis, G, Gis と呼ぶ.

音名 | セント | Hz      |   |
:---:|-------:|:-------:|---|
G    | -200   | 393.777 |<input type="button" value="再生" onclick="sin_wave(393.777);"/>|
Gis  | -100   | 417.192 |<input type="button" value="再生" onclick="sin_wave(417.192);"/>|
A    |    0   | 442.000 |<input type="button" value="再生" onclick="sin_wave(442.000);"/>|
B    |  100   | 468.283 |<input type="button" value="再生" onclick="sin_wave(468.283);"/>|
H    |  200   | 496.128 |<input type="button" value="再生" onclick="sin_wave(496.128);"/>|
C    |  300   | 525.630 |<input type="button" value="再生" onclick="sin_wave(525.630);"/>|
Cis  |  400   | 556.885 |<input type="button" value="再生" onclick="sin_wave(556.885);"/>|
D    |  500   | 589.999 |<input type="button" value="再生" onclick="sin_wave(589.999);"/>|
Dis  |  600   | 625.082 |<input type="button" value="再生" onclick="sin_wave(625.082);"/>|
E    |  700   | 662.252 |<input type="button" value="再生" onclick="sin_wave(662.252);"/>|
F    |  800   | 701.631 |<input type="button" value="再生" onclick="sin_wave(701.631);"/>|
Fis  |  900   | 743.352 |<input type="button" value="再生" onclick="sin_wave(743.352);"/>|
G    | 1000   | 787.554 |<input type="button" value="再生" onclick="sin_wave(787.554);"/>|


# 倍音列

長さ $L$ の弦の振動について考える (管楽器でも原理的には同じである). 
一方の端点から測った座標を $x$ とするとき, 時刻 $t$ での弦の横方向の変位 $z ( t, x )$ により弦の状態は記述される.
ただし固定端境界条件のもとでは $z ( t, 0 ) = z ( t, L ) = 0$ である.

固定端境界条件のために, 変位 $z ( t, x )$ を次のように座標 $x$ について Fourier 級数展開することができる.
$$z ( t, x ) = \sum_{n=1}^\infty Z_n ( t ) \sin k_n x , \ \ k_n = \pi \frac{ n }{ L }$$
変位 $z ( t, x )$ は, $c_s$ を音速として波動方程式
$$\frac{ \partial^2 z }{ \partial t^2 } - {c_s}^2 \frac{ \partial^2 z }{ \partial x^2 } = 0$$
を満足する. これを Fourier モード $A_n$ に関する方程式として書き直すと
$$\frac{ d^2 Z_n }{ d t^2 } = - { c_s }^2 { k_n }^2 Z_n$$
これはただちに解けて, $A_n$ を振幅, $\alpha_n$ を初期位相として
$$Z_n = A_n \cos ( \omega_n t + \alpha_n ) , \ \ \omega_n = c_s k_n$$
となる. 言い換えると, 長さ $L$ の弦に生じる振動は, 次の離散的な振動数
$$f_n = \frac{ \omega_n }{ 2 \pi } = \frac{ n c_s }{ 2 L } , \ \ n = 1 , 2, \cdots$$
に限られる, ということになる. これを [__倍音列__](https://ja.wikipedia.org/wiki/%E5%80%8D%E9%9F%B3) (harmonics) と呼ぶ.
特に最も小さな振動数を持つ (つまり最も波長が長い) $n = 1$ のモードを __基音__ (fundamental tone) と呼ぶ.
また, 第 $n$ モードの周波数 $f_n$ は基音の周波数 $f_n$ と
$$f_n = n f_1$$
という関係にあることを強調しておく. 従って, 
ある倍音列 $\\{ f_n \\}_{n = 1, 2, \cdots}$ に含まれるふたつの周波数 $f_n$, $f_m$ は, 
その比が有理数であるという顕著な特徴を持つ.
$$\frac{ f_n }{ f_m } = \frac{ n }{ m }$$
逆に, 有理数比を持つふたつの音程は __純正音程__ (pure interval) と呼ばれ,
特に単純な有理数比 ($1:2$ や $2:3$ など) をもつ音程は __協和音程__ として知られる.

基音 $f_1 = 110.5\\,\mathrm{Hz}$ に対応する倍音列およびそれに最も近い平均律での音名を次の表に示す.
また, 平均律の場合に期待される音高との差 $\Delta c$ (セント) も併せて示す.

モード | 音名 | 周波数 | <span class="center">$\Delta c$</span> | |
-------|:----:|-------:|-----------:|-|
$n=1$  | A    |  110.5 | <span class="num3">  0    </span>  |<input type="button" value="再生" onclick="sin_wave(110.5*1 );"/>|
$n=2$  | A    |  220.1 | <span class="num3">  0    </span>  |<input type="button" value="再生" onclick="sin_wave(110.5*2 );"/>|
$n=3$  | E    |  331.5 | <span class="num0">+ 1.955</span>  |<input type="button" value="再生" onclick="sin_wave(110.5*3 );"/>|
$n=4$  | A    |  442.0 | <span class="num3">  0    </span>  |<input type="button" value="再生" onclick="sin_wave(110.5*4 );"/>|
$n=5$  | Cis  |  552.5 | <span class="num0">-13.636</span>  |<input type="button" value="再生" onclick="sin_wave(110.5*5 );"/>|
$n=6$  | E    |  663.0 | <span class="num0">+ 1.955</span>  |<input type="button" value="再生" onclick="sin_wave(110.5*6 );"/>|
$n=7$  | G    |  773.5 | <span class="num0">-31.174</span>  |<input type="button" value="再生" onclick="sin_wave(110.5*7 );"/>|
$n=8$  | A    |  884.0 | <span class="num3">  0    </span>  |<input type="button" value="再生" onclick="sin_wave(110.5*8 );"/>|
$n=9$  | H    |  994.5 | <span class="num0">+ 3.910</span>  |<input type="button" value="再生" onclick="sin_wave(110.5*9 );"/>|
$n=10$ | Cis  | 1105.0 | <span class="num0">-13.686</span>  |<input type="button" value="再生" onclick="sin_wave(110.5*10);"/>|
$n=11$ | Dis  | 1215.5 | <span class="num0">-48.682</span>  |<input type="button" value="再生" onclick="sin_wave(110.5*11);"/>|
$n=12$ | E    | 1326.0 | <span class="num0">+ 1.955</span>  |<input type="button" value="再生" onclick="sin_wave(110.5*12);"/>|
$n=13$ | Fis  | 1436.5 | <span class="num0">-59.472</span>  |<input type="button" value="再生" onclick="sin_wave(110.5*13);"/>|
$n=14$ | G    | 1547.0 | <span class="num0">-31.174</span>  |<input type="button" value="再生" onclick="sin_wave(110.5*14);"/>|
$n=15$ | Gis  | 1657.5 | <span class="num0">-11.731</span>  |<input type="button" value="再生" onclick="sin_wave(110.5*15);"/>|
$n=16$ | A    | 1768.0 | <span class="num3">  0    </span>  |<input type="button" value="再生" onclick="sin_wave(110.5*16);"/>|


# Pythagoras 音律

[Pythagoras 音律](https://ja.wikipedia.org/wiki/%E3%83%94%E3%82%BF%E3%82%B4%E3%83%A9%E3%82%B9%E9%9F%B3%E5%BE%8B)は, 
基準音からオクターブ (純正完全八度) $1:2$ および純正完全五度 $2:3$ を積み重ねることにより得られる音階のことを言う.
例えば基準音 A ($f_0$) に対して, その完全5度上の音 (E) の振動数は $\frac{ 3 }{ 2 } f_0$ となる.
セントで表すとこの音は
$$n_\mathrm{E} = 1200 ( \log_2 3 - 1 ) = 701.955$$
に対応し, 平均律での E 音とは約 2 セントの差を生じる. 同様に E 音の完全5度上は H 音であり, 
その振動数は $f = \left( \frac{3}{2} \right)^2 f_0$, セントは
$$n_\mathrm{H} = 2 n_\mathrm{E} - 1200 = 203.910$$
であり, 平均律とは約 4 セント異なる. このように, 完全五度変化する毎に平均律とは約 2 セントの相違が
累積することが Pythagoras 音律の特徴である.

Pythagoras 音律において平均律で用いられるのと同じ12音を構成しようとすると特有の原理的困難を生じる.
まず, A から上昇していくと

- A - E - H - Fis - Cis - Gis - Dis

となるが, 下降していくと

- A - D - G - C - F - B - Es 

となる. 平均律では Dis と Es は完全に同一の音高 (1100 セント) であるにも関わらず,
Pythagoras 音律では 23.460 セント異なった音である 
([Pythagoras コンマ](https://ja.wikipedia.org/wiki/%E3%83%94%E3%82%BF%E3%82%B4%E3%83%A9%E3%82%B9%E3%82%B3%E3%83%B3%E3%83%9E)). 
従って, 例えば Es を採用した楽器では Es - Gis の和音は Pythagoras 音律で期待される 701.955 セント差ではなく, 678.495 セントとなる.
これを __ウルフの五度__ と呼ぶ.

<span class="center">上昇音列</span>

音名 | 周波数 | <span class="center">$\Delta c$</span> | | |
:---:|-------:|-----------:|-|-|
A    | 442    | <span class="num3">  0    </span>  |<input type="button" value="再生" onclick="sin_wave(442.*  1/ 1 );"/>|
E    | 663    | <span class="num0">+ 1.955</span>  |<input type="button" value="再生" onclick="sin_wave(442.*  3/ 2 );"/>|<input type="button" value="再生" onclick="sin_wave(442.*  3/ 2 /2);"/>|
H    | 994.5  | <span class="num0">+ 3.910</span>  |<input type="button" value="再生" onclick="sin_wave(442.*  9/ 4 );"/>|<input type="button" value="再生" onclick="sin_wave(442.*  9/ 4 /2);"/>|
Fis  |1491.75 | <span class="num0">+ 5.865</span>  |<input type="button" value="再生" onclick="sin_wave(442.* 27/ 8 );"/>|<input type="button" value="再生" onclick="sin_wave(442.* 27/ 8 /2);"/>|
Cis  |2237.625| <span class="num0">+ 7.820</span>  |<input type="button" value="再生" onclick="sin_wave(442.* 81/16 );"/>|<input type="button" value="再生" onclick="sin_wave(442.* 81/16 /4);"/>|
Gis  |3356.438| <span class="num0">+ 9.775</span>  |<input type="button" value="再生" onclick="sin_wave(442.*243/32 );"/>|<input type="button" value="再生" onclick="sin_wave(442.*243/32 /4);"/>|
Dis  |5034.656| <span class="num0">+11.730</span>  |<input type="button" value="再生" onclick="sin_wave(442.*729/64 );"/>|<input type="button" value="再生" onclick="sin_wave(442.*729/64 /8);"/>|

<span class="center">下降音列</span>

音名 | 周波数 | <span class="center">$\Delta c$</span> | | |
:---:|-------:|-----------:|-|-|
A    | 442    | <span class="num3">  0    </span>  |<input type="button" value="再生" onclick="sin_wave(442.* 1/  1 );"/>| |
D    | 294.667| <span class="num0">- 1.955</span>  |<input type="button" value="再生" onclick="sin_wave(442.* 2/  3 );"/>|<input type="button" value="再生" onclick="sin_wave(442.* 2/  3 *2 );"/>|
G    | 196.444| <span class="num0">- 3.910</span>  |<input type="button" value="再生" onclick="sin_wave(442.* 4/  9 );"/>|<input type="button" value="再生" onclick="sin_wave(442.* 4/  9 *2);"/>|
C    | 130.963| <span class="num0">- 5.865</span>  |<input type="button" value="再生" onclick="sin_wave(442.* 8/ 27 );"/>|<input type="button" value="再生" onclick="sin_wave(442.* 8/ 27 *4);"/>|
F    |  87.309| <span class="num0">- 7.820</span>  |<input type="button" value="再生" onclick="sin_wave(442.*16/ 81 );"/>|<input type="button" value="再生" onclick="sin_wave(442.*16/ 81 *8);"/>|
B    |  58.206| <span class="num0">- 9.775</span>  |<input type="button" value="再生" onclick="sin_wave(442.*32/243 );"/>|<input type="button" value="再生" onclick="sin_wave(442.*32/243 *8);"/>|
Es   |  38.804| <span class="num0">-11.730</span>  |<input type="button" value="再生" onclick="sin_wave(442.*64/729 );"/>|<input type="button" value="再生" onclick="sin_wave(442.*64/729 *16);"/>|


# 純正律

純正完全五度 (振動数の比 2:3) に加えて, 純正長三度 (振動数の比 4:5) を用いて構成した音律が
[__純正律__](https://ja.wikipedia.org/wiki/%E7%B4%94%E6%AD%A3%E5%BE%8B) (just intonation) である.

古典和声の基礎となるトニカ (A-Cis-E), ドミナント (E-Gis-H), サブドミナント (D-Fis-A) がそれぞれ振動数の比 4:5:6 
を持つように音高を定めることにより, 全音階 A, H, Cis, D, E, Fis, Gis を定めることができる.
この場合, 全音階に含まれる完全五度のうち, H-Fis, Cis-Gis, Fis-Cis という組は純正完全五度にはならない. 

音名 | 周波数 |$f/f_0$| <span class="center">$\Delta c$</span> | |
:---:|-------:|:---:|-----------:|-|
A    |<span class="num3">442    </span>|1/1|<span class="num3">  0    </span>  |<input type="button" value="再生" onclick="sin_wave(442.* 1/  1);"/>|
H    |<span class="num1">497.25 </span>|9/8|<span class="num0"> +3.910</span>  |<input type="button" value="再生" onclick="sin_wave(442.* 9/  8);"/>|
Cis  |<span class="num2">552.5  </span>|5/4|<span class="num0">-13.686</span>  |<input type="button" value="再生" onclick="sin_wave(442.* 5/  4);"/>|
D    |<span class="num0">589.333</span>|4/3|<span class="num0"> -1.955</span>  |<input type="button" value="再生" onclick="sin_wave(442.* 4/  3);"/>|
E    |<span class="num3">663    </span>|3/2|<span class="num0"> +1.955</span>  |<input type="button" value="再生" onclick="sin_wave(442.* 3/  2);"/>|
Fis  |<span class="num0">736.667</span>|5/3|<span class="num0">-15.641</span>  |<input type="button" value="再生" onclick="sin_wave(442.* 5/  3);"/>|
Gis  |<span class="num1">828.75|</span>15/8|<span class="num0">-11.731</span>  |<input type="button" value="再生" onclick="sin_wave(442.*15/  8);"/>|
