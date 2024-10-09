+++
title = "分類法の数学的定義"
date = 2024-08-24
[extra]
toc = true
[taxonomies]
tags = [ "情報理論", ]
+++

アクセス可能なすべての情報の中から求める情報に辿り着くことは難しい問題で, 古くから
[図書館情報学](https://ja.wikipedia.org/wiki/%E5%9B%B3%E6%9B%B8%E9%A4%A8%E6%83%85%E5%A0%B1%E5%AD%A6)
として研究されてきました.
[検索エンジン](https://ja.wikipedia.org/wiki/%E6%A4%9C%E7%B4%A2%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%B3)
の登場はこの状況に大きな変革をもたらしましたが, それでもすべてを解決することはできません.
具体的にふたつのケースを見てみます.

* 図書館の蔵書の中から利用者が求める書籍を探し出すこと.
検索エンジンはデジタル化されていない情報を検索することができないため, 事前にすべての蔵書の
[書誌情報](https://ja.wikipedia.org/wiki/%E6%9B%B8%E8%AA%8C)
をデジタル化しておく必要があります.
あらゆる書籍を書誌情報という圧縮された情報に要約すること
([図書分類法](https://ja.wikipedia.org/wiki/%E5%9B%B3%E6%9B%B8%E5%88%86%E9%A1%9E%E6%B3%95)) はそれ自体難しい問題で,
個人図書館などの小規模な図書館であれ, 国や大学が運営する大規模な図書館であれ, かなりの労力を必要とします.
出版社などが提供する書誌情報を用いることもできますが, 情報源によってフォーマットや得られる情報が異なるため,
統一的に扱うことができるかどうか, という問題も発生します.
書籍を丸ごとスキャンしてテキスト化するというのも一案ですが, すべての書籍のすべての内容をデジタル化するのは技術的に簡単ではないですし
(例えば複雑な有機化合物の形状を示すためには図が必須であり, それを検索可能な情報としてデジタル化するのは容易ではありません), 
著作権法上の制約を考慮する必要があります.

* eコマースサイトのすべての商品から利用者が求める商品を探し出すこと.
例えば PC を購入する場合, メーカー, デスクトップかラップトップかタブレットか, デザイン,
CPU 性能, グラフィック性能, メモリ, ディスク容量とアクセス速度, 重量, 外部接続端子や無線通信規格, 価格といった様々な要素が購入判断に関わります.
これらを汎用の検索エンジンですべて厳密に指定して検索することは難しいです.
さらに, どのような情報を商品検索に用いるかは eコマースサイトの扱う商品によって異なります
(アパレル店の商品を説明する際に CPU 性能という項目が登場することはありませんし, 
[日本十進分類法](https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E5%8D%81%E9%80%B2%E5%88%86%E9%A1%9E%E6%B3%95) も役に立ちません).

いずれにせよ, このような状況下で求める情報を提示するためには, 所持している情報を整理して扱いやすい形に表現しておくことが必要です.
これが分類法の目標です.


# 定義

上述の例では考えている情報の全体は, 前者は図書館の蔵書, 後者はショップの商品, という単位となる構成要素からできていました.
このように情報の総体がいくつかの個別の構成要素からできているとき, その構成要素のことを __エントリー__ (entry) と呼ぶことにしましょう.
また, 考えているエントリーすべての集合を $X$ を書くことにします.
$X$ は有限集合ですが, その元の数は極めて大きい可能性があります.

エントリー $x \in X$ が与えられると, そのエントリー $x$ が持つ様々な情報が得られます.
例えば書籍の場合, 著者, 出版社, 出版年, 目次, 本文などです.
こういったエントリーが持つ複数の項目のラベルをキー (key) といい, その全体を $K$ とします.
あらゆるデジタルデータは, $B = \\{ 0, 1 \\}$ とするとその有限列の全体
$$\mathbb{B} =  \bigcup_{n = 0}^\infty B^n$$
の元として表現できます. 上の状況は, エントリー $x \in X$ およびキー $k \in K$ が与えられると対応する情報 $I(x, k) \in \mathbb{B}$ が得られる, と要約できます.
数学的にはこれは写像
$$I: X \times K \to \mathbb{B}$$
が与えられている, という意味です.

__分類__ $C$ とは $X$ の部分集合のことです. ただ, あらゆる分類をすべて集めてきたとしても (これは $X$ のべき集合 $\mathfrak{P}(X)$ になります),
情報が雑多すぎてあまり役に立ちそうにありません.
少数の有用な分類だけを集めてきたものだけが意味を持ちます.
そのような分類の集合 $\mathbb{C} \subseteq \mathfrak{P}(X)$ を __分類体系__ と呼びます.
エントリーの数を $|X|$ と書くとき, 分類の総数は高々 $2^{|X|}$ 個です.

なお本記事では記号 $\subseteq$ は部分集合を, 記号 $\subset$ は真部分集合を表します.

要約します. 情報系 (information system) とはふたつの有限集合 $X$, $K$ および写像 $I: X \times K  \to \mathbb{B}$ の組 $(X, K, I)$ のことをいいます.
情報系 $(X, K, I)$ の分類体系 $\mathbb{C}$ とは, $X$ のべき集合 $\mathbb{P}(X)$ の部分集合のことをいいます.


# 階層分類

典型的な分類体系として階層分類 (hierarchical taxonomy) があります.
情報系 $(X, K, I)$ の分類体系 $\mathbb{C}$ が階層分類であるとは, 任意のふたつの異なる分類 $C_1, C_2 \in \mathbb{C}$ が
$$C_1 \subset C_2 \ \ \mathrm{or} \ \ C_1 \supset C_2 \ \ \mathrm{or} \ \ C_1 \cap C_2 = \phi$$
を満たすことをいいます. $C_1 \subset C_2$ であるとき $C_2$ は $C_1$ の上位分類, $C_1$ は $C_2$ の下位分類であるといいます.

エントリー $x$ を含む分類をすべて集めてきて, それを $C_0, C_1, \cdots C_{n-1} \in \mathbb{C}$ としましょう.
$\mathbb{C}$ は有限集合ですから, このような分類は有限個しか存在しません.
$\mathbb{C}$ が階層分類であるならば, このような $C_i$ と $C_j$ は (共通元として常に $x$ が存在するため) 一方が他方の上位分類です.
そこで $C_i$ を $i < j$ ならば $C_i$ が $C_j$ の上位分類であるように並び替えると, エントリー $x$ を含む分類の列
$$C_0 \supset C_1 \supset \cdots \supset C_{n-2} \supset C_{n-1} \ni x$$
が一意的に得られます.

階層分類は図書館分類法に適しています. これは, 図書館においては書籍を書架の特定の場所に配列する必要がありますが,
上位分類によって部屋や区域を分け, 下位分類によって書棚を分けることによって, 書籍を一意的な書棚に配置することができるからです.



# ファセット分類

異なる観点の分類体系として __ファセット分類__ (faceted classification) があります.
これはファセット集合 $F$ と呼ばれるキーの集合 $K$ の部分集合 $F \subseteq K$ によって以下のように定まる分類体系 $\mathbb{F}$ です.

ファセット $f \in F$ およびデジタルデータ $d \in \mathbb{B}$ が定めるファセット分類 $C_{f=d} \in \mathbb{F}$ とは, 分類
$$C_{f=d} = \left\\{ x \in X \mid I ( x, f ) = d \right\\}$$
のことをいいます. 異なるデータ $d_1, d_2 \in \mathbb{B}$ ($d_1 \neq d_2$) に対応するファセット分類は互いに素です.
$$C_{f=d_1} \cap C_{f=d_2} = \phi$$
ひとつのエントリー $x \in X$ は, 異なるファセット $f_1, f_2, \cdots \in F$ に応じて複数のファセット分類
$$C_{f_1 = I(x,f_1)} , \ \ C_{f_2 = I(x,f_2)} , \ \ \cdots$$
に属します. 値 $I(x, f_1)$, $I(x, f_2)$, ... がエントリー $x$ を分類している, とも解釈できます.

ファセット分類は eコマースに適しています. 
これは, 利用者の要望に応じて商品を絞り込んでいくというプロセスがファセット分類の共通部分を取る操作として実現するからです.
ひとつの要望がひとつのファセット分類 $C_{f=d}$ として表現できるため, 
すべての要望が与えられたならば各要望に対応するファセット分類の共通部分が利用者の要望を満たす商品群を与えます.



# タグ分類

タグによる分類は最も数学的特徴に乏しい分類体系です. エントリーをタグによって分類するという行為は, 
勝手な分類体系 $\mathbb{C}$ を与えてその分類 $C \in \mathbb{C}$ に名前 (「タグ」) を与えることに過ぎません.



# 参考文献

* [分類体系 - Wikipedia](https://ja.wikipedia.org/wiki/%E5%88%86%E9%A1%9E%E4%BD%93%E7%B3%BB)
* [Faceted Classification – The Discipline of Organizing: 4th Professional Edition](https://berkeley.pressbooks.pub/tdo4p/chapter/faceted-classification/)