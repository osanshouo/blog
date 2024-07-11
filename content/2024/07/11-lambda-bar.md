+++
title = "[TeX] λの上にバーをつける"
date = 2024-07-11
[taxonomies]
tags = [ "TeX", ]
+++

[換算 Planck 定数](https://ja.wikipedia.org/wiki/%E3%83%87%E3%82%A3%E3%83%A9%E3%83%83%E3%82%AF%E5%AE%9A%E6%95%B0) $\hbar$ のように, 
文字自体にバー (ストローク) をつける表記法が採用されることがあります.
$\hbar$ は LaTeX コマンド `\hbar` として収録されているので良いのですが, 
天文学で用いられる $ƛ$, 熱力学で用いられる不完全微分 $đ$ などは通常のコマンド `\bar{}` では実現できません.

要件として, 通常の LaTeX だけでなく, MathJax やできれば pandoc でも扱えるものが好ましいです.


# TeX コマンドでがんばる

参考文献に載っているコマンドをいろいろと試してみましたが, MathJax でもうまくいったものはふたつだけです.
ただしいずれも pandoc では MathML に変換できません.

まず一番上の文献に載っている
```tex
{\lambda \kern -0.5em\raise 0.5ex \hbox{--}}
```
です. 実際に使ってみたものがこちら:
$${\lambda \kern -0.5em\raise 0.5ex \hbox{--}} = \frac{ \lambda }{ 2 \pi }$$
多少修正して
```tex
{\lambda \kern -0.8em\raise 0.5ex -}
```
としても類似の結果になります.
$${\lambda \kern -0.8em\raise 0.5ex -} = \frac{ \lambda }{ 2 \pi }$$


もう一つが Wikipedia の [Inexact differential](https://en.wikipedia.org/wiki/Inexact_differential) に載っていた
```tex
\rlap{\textrm{d}}{\bar{\phantom{w}}}
\rlap{{\lambda}}{\bar{\phantom{w}}}
```
です. ただ d の方は斜体にしてしまうとストロークの位置がずれてしまいます.
$$\rlap{\textrm{d}}{\bar{\phantom{w}}}$$
$$\rlap{{\lambda}}{\bar{\phantom{w}}}$$


# 専用の Unicode 符号を使う

これらのバー記号は Unicode では [ストローク符号](https://ja.wikipedia.org/wiki/%E3%82%B9%E3%83%88%E3%83%AD%E3%83%BC%E3%82%AF%E7%AC%A6%E5%8F%B7)
と呼ばれているもので, 専用の Unicode 符号が与えられています 
([ラテン文字拡張A](https://ja.wikipedia.org/wiki/%E3%83%A9%E3%83%86%E3%83%B3%E6%96%87%E5%AD%97%E6%8B%A1%E5%BC%B5A),
[ラテン文字拡張B](https://ja.wikipedia.org/wiki/%E3%83%A9%E3%83%86%E3%83%B3%E6%96%87%E5%AD%97%E6%8B%A1%E5%BC%B5B)).
なのでこれらに含まれている文字ならば, それを直接入力してしまえば Unicode が表示できるすべての環境で使用することはできます.
ただし適切なフォントがあるかどうかは別問題で, LaTeX デフォルトの Computer Modern (やその派生フォント) には収録されておらず,
フォント面では期待した見た目にならない可能性があります.

コピペ用:

```
đ
```

```
ƛ
```

ちなみにどちらも単独記事になっています.
* [D with stroke](https://en.wikipedia.org/wiki/D_with_stroke)
* [Barred lambda](https://en.wikipedia.org/wiki/Barred_lambda)


# 参考文献

* [ラムダバー（\lambdabar）の作り方 - 天文学的研究メモ](https://yoshiyuki-kitne.hatenadiary.org/entry/20070305/p1)
* [【Proton.jp】 LaTeXのTips集](https://web.archive.org/web/20090101221347/http://www.proton.jp/latex/tips.html)
* [symbols - How can I type "lambda-bar"? - TeX - LaTeX Stack Exchange](https://tex.stackexchange.com/questions/96479/how-can-i-type-lambda-bar)
* [math mode - d with a little line through the top of it - TeX - LaTeX Stack Exchange](https://tex.stackexchange.com/questions/203508/d-with-a-little-line-through-the-top-of-it)


