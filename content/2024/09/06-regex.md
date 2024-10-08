+++
title = "正規表現のまとめ"
date = 2024-09-06
[extra]
toc = true
[taxonomies]
tags = [ "JavaScript", ]
+++

# 文字集合と文字列集合

## 文字集合

本記事では文字集合を記号 $\mathbb{A}$ により表します.
これには ASCII 印字可能文字 (`U+0020` から `U+007E`) がすべて含まれていることを仮定しますが,
通常は文字列集合 $\mathbb{A}$ として ASCII 制御文字を含む Unicode の符号化文字集合 (CCS) を選びます.

正規表現の __メタ文字__ とは, 文字 `.`, `[`, `]`, `(`, `)`, `|`, `^`, `$`, `\`, `*` のことをいいます.
以下では文字列集合 $\mathbb{A}$ からこれらメタ文字および ASCII 制御文字を除いたものを $\mathbb{A}_L$ と表記します.


## 文字列集合

本記事では, __文字列__ とは文字集合の元の (順序を持つ) 有限列のことをいいます.

文字列の全体を記号 $\mathbb{S}$ により表します. ここには空文字列も含まれると解釈します.
$$\mathbb{S} = \bigcup_{n = 0}^\infty \mathbb{A}^n$$
文字列の全体 $\mathbb{S}$ の部分集合 $\mathbb{C}$ のことを (文字列) __クラス__ といいます.
$$\mathbb{C} \subset \mathbb{S}$$
すべての文字列クラスの全体がなす集合のことを $\mathbb{S}$ のべき集合 $\mathscr{P}(\mathbb{S})$ というのでした.
本記事では一貫して文字列クラスを表す記号としてフラクトゥールを用います.

ふたつの文字列 $a, b \in \mathbb{S}$ に対して, その結合文字列を記号 $a b$ または $a \cdot b$ により表します.

## 正規表現

正規表現とは, 以下で定義する文字列クラス $\mathbb{R}$, あるいはそこから文字列集合のべき集合への写像
$$\mathrm{regex}: \mathbb{R} \to \mathscr{P} ( \mathbb{S} )$$
のことです. ある文字列 $s \in \mathbb{S}$ が正規表現であるとは, それがクラス $\mathbb{R}$ の元であることをいいます.



# 集合の基本操作

## 直和

正規表現 $a$, $b$ に対して, その直和を表す正規表現を $( a | b )$ と定義します.
つまり, $s \in ( a | b )$ は $s \in a$ または $s \in b$ を満たします.

## 直積

正規表現 $a$, $b$ に対して, その直積を表す正規表現を $a b$ と定義します.
つまり, $s\in a b$ は $\alpha \in a$ および $\beta \in b$ を用いて $s = \alpha \beta$ と表示できます.



# シングルトン

[シングルトン](https://ja.wikipedia.org/wiki/%E5%8D%98%E9%9B%86%E5%90%88) とは, ひとつの文字列だけを含む文字列クラスのことです.

## リテラル

メタ文字を含まない文字列は正規表現であり, それ自身を要素とするシングルトンを与えます:
$s \in \mathbb{A}_L^n$ のとき
$$\mathrm{regex}: s \mapsto \\{ s \\} .$$

## エスケープと特殊文字

文字 `\` とメタ文字を結合した文字列 `\.`, `\[`, `\]`, `\^`, `\$`, `\\`, `\*` は正規表現であり,
そのメタ文字を要素とするシングルトンを与えます:
$m \in \mathbb{A} - \mathbb{A}_L$ のとき
$$\mathrm{regex}: \text{\\\\}m \mapsto \\{ m \\} .$$

メタ文字 `^`, `$` がエスケープされずに用いられた場合, それぞれ行頭および行末を表します.
また, ASCII 制御文字のエスケープ表現や Unicode のコードポイント表示は正規表現として認められています.



# 文字クラス

四角括弧 `[`, `]` で囲まれた文字列は, その中のいずれかの1文字からなる文字列にマッチします.
$$[\text{abc}] = \\{ \text{a} , \text{b}, \text{c} \\}$$
またハイフンを使用することで範囲を指定することもできます.
$$[\text{0-9a-zA-Z}] = \\{ \text{0} , \cdots, \text{9}, \text{a}, \cdots. \text{z}, \text{A}, \cdots, \text{Z} \\}$$
また, 文字クラスの補集合は `[^` および `]` に囲まれた文字列として表現されます.

実用上頻繁に用いられる文字クラスには専用の記号が割り当てられています.

* `\d`: 数字1文字にマッチします. `[0-9]` と等価です.
* `\D`: 数字以外1文字にマッチします. 文字集合 $\mathbb{A}$ から `\d` を除いたものと等価です.
* `\s`: 空白1文字にマッチします. `[ \f\n\r\t\v]` と等価です.
* `\S`: 空白以外1文字にマッチします. 文字集合 $\mathbb{A}$ から `\s` を除いたものと等価です.
* `\w`: ASCII 印字可能文字のうち, 数字, アルファベット, アンダースコアにマッチします.
* `\W`: 文字集合 $\mathbb{A}$ から `\w` を除いたものと等価です.

ただし実装によっては, 例えば `\d` に非 ASCII の数字が含まれたりします.

四角括弧内でのエスケープに関しては注意が必要です.

* [正規表現: 文字クラス [ ] 内でエスケープしなくてもよい記号｜TechRacho by BPS株式会社](https://techracho.bpsinc.jp/hachi8833/2020_11_04/40673)

## `.`

文字列 `.` は正規表現であり, 長さ 1 の文字列全体 (つまり $\mathbb{A}$) を表します.
ただし改行を除外する場合もあります.



# 量指定子

* `*`: 直前の正規表現の0回以上の反復.
* `+`: 直前の正規表現の1回以上の反復.
* `?`: 直前の正規表現の0回または1回の反復.
* `{n}`: 直前の正規表現のn回の反復.
* `{n,}`: 直前の正規表現のn回以上の反復.
* `{n,m}`: 直前の正規表現のn回以上m回以下の反復.

なお, 通常の実装ではこれらの量指定子を含む正規表現が与えられたとき, 最左最長一致を探索します.
最左最短一致探索には `?` を後ろに追加します.

* [量指定子 (正規表現) - .NET | Microsoft Learn](https://learn.microsoft.com/ja-jp/dotnet/standard/base-types/quantifiers-in-regular-expressions)



# 後方参照

正規表現 `(x)` はマッチした文字列を記憶します (キャプチャグループ). 
n番目にマッチしたグループを `\n` として参照することができます.
`(?<name>x)` という形でキャプチャグループに名前 `<name>` を定義することもできます.



# 参考文献

* [正規表現構文早見表 - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Guide/Regular_expressions/Cheatsheet)
* [正規表現言語 - クイック リファレンス - .NET | Microsoft Learn](https://learn.microsoft.com/ja-jp/dotnet/standard/base-types/regular-expression-language-quick-reference)
* [正規表現 - Wikipedia](https://ja.wikipedia.org/wiki/%E6%AD%A3%E8%A6%8F%E8%A1%A8%E7%8F%BE)
* [手を動かしながら覚える正規表現＜基礎入門編＞](https://doc.mas3.net/regexp/)
