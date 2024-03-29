+++
title = "書誌情報フォーマット"
date = 2021-05-24
[extra]
toc = true
[taxonomies]
tags = ["本", "PDF", "EPUB"]
+++

手元の電子書籍 (PDF および EPUB) の数が増えてきたので, 管理方法を考えています.
あるファイルにアクセスしたくなるときはほとんど著者名でそれを認識しているので,
現状ではファイル名を `著者名 - タイトル.pdf` のような形にしておき, Win10 の検索機能で PDF を開いています.
しかしこれではある特定の主題に関する文献が欲しい, というような状況では不便です.
いまは分野別のフォルダに分けて保存していますが, ひとつのファイルはひとつのパス (例えば `Physics/Thermodynamics/`) にしか保存できないので, 
あるファイルが複数の領域にまたがっており両方からアクセスしたいという需要には応えられません.
さらに, より詳しく細分化しようとすると一覧性が下がってしまいます.
ショートカット/symlink を貼るのは管理が非常に面倒です.

そこでなにか簡単なインターフェースを作成しようと思っているのですが, 
その前提としてどこかに各ファイルの書誌情報を記録しておく必要があります.
このような情報はどのようなフォーマットのファイルに保存しておくべきか？ が本記事の主題です.


# 要件
まず最初に, このファイルフォーマットに求める要件をはっきりさせておきましょう.
この書誌情報には著者, タイトル, 出版社, 年などの標準的な項目に加えて,
ファイルパス, 自分でつけた管理用キーワードといった情報を記録しておきたいです.
再利用性を考慮するならば BibTeX といった他の標準的なフォーマットに変換できることが望ましいですが, あまり重視しません.

## 書誌情報のインポート
この手の情報はどこかのデータベースからインポートできると便利ですが, 
サービスによってインポートできる情報が違ったりして結局手動での調整は必要です.
自動化が必要なほどの件数もありません. あまり気にしなくてもよいでしょう.

## 文献管理ソフト
こういうことは文献管理ソフトを使うべきなのでしょうけれども, 商用のものは基本的にクラウドストレージの容量の問題で有料プランでないといけません.
しかし大部分のファイルはアクセス頻度がかなり低いですし, それなのに永久に課金し続けるというのも不毛です.
所詮 PDF なのですから, 手元の NAS に置いておき, 必要になったら掘り出せばよいのです.
適当なオープンソースソフトウェアがあればそれでもよいですが, 
所詮メタデータをちょっと検索したいというだけの要件なので, 自作しても大した手間ではありません.


# 書誌情報フォーマット

## BibTeX/BibLaTeX
既によく普及した書誌情報フォーマットは存在します. BibTeX です.
しかし個人的にはあまり好みではなく, 避けられるものなら避けたいものです
(複数人の author がいるときの扱いが気に入らないのと, そもそも LaTeX をあまり使わなくなっている).
しかしこれが最も普及しているため, 現実的には一番楽かもしれません. 
Rust クレートとしては [nom-bibtex](https://crates.io/crates/nom-bibtex) と
[biblatex](https://crates.io/crates/biblatex) が実用可能な程度には実装されているようです.

## MARC 21
図書館業界では大昔から [MARC](機械可読目録) という形式が使われており, それを現代化した MARC21 がスタンダードなようです.

* [JAPAN/MARC MARC21フォーマットマニュアル - 国立国会図書館](https://www.ndl.go.jp/jp/data/JAPANMARC_MARC21manual_MS.pdf)

ただ日本の図書館のデータベースはアルファベットを全角文字で入力しているため, 使う気になりません.
このフォーマット自体, バイナリ形式でなにかと面倒です.

## XML
J-Stage は XML を推しているようで, [ガイドライン](https://www.jstage.jst.go.jp/static/pages/GuidelineAndManuals/TAB2/-char/ja) が公開されています. 
他に [Microsoft Word 形式](https://docs.microsoft.com/ja-jp/office/vba/word/concepts/working-with-word/working-with-bibliographies) もあり, 
これは Word がメインの人にとっては便利かもしれません.

いずれにせよ XML は入力が面倒なので, 使うにしても他の形式で作成したものを変換するという形になるでしょう 
(話が逸れますが, これこそが MathML が失敗した理由だと思います).

## JSON
JSON で書誌情報を記述するために [BibJSON](http://okfnlabs.org/bibjson/) や [CSL-JSON](https://citeproc-js.readthedocs.io/en/latest/csl-json/markup.html) という仕様があるようです. 
なんでふたつもあるんでしょうか. BibJSON は doi の入力が面倒そうなのが気になります.

## YAML
[Serde](https://serde.rs/#data-formats) が対応しているテキスト形式と考えると, その他の選択肢は YAML か TOML になります.
TOML はより構造化されたデータを想定しているため, どちらかというと YAML でしょうか.
[pandoc](https://pandoc-doc-ja.readthedocs.io/ja/latest/users-guide.html#citations) は YAML 推しのようです.


# まとめ
書誌情報界隈で最も普及している BibTeX/BibLaTeX, 汎用フォーマットとして最も普及している JSON, 入力しやすい YAML あたりが現実的な選択肢でしょうか.
ここまで調べるだけでかなり疲れたので今日はこのあたりまでとします.
