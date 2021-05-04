+++
title = "PDFに目次を追加する"
date = 2021-05-04
[extra]
toc = true
[taxonomies]
tags = ["Linux", "PDF"]
+++

EdgeHTML 版の Microsoft Edge は PDF ビューワーとしてとても優れていたのですが,
Chromium ベースに移行した際に大部分の機能が欠落してかなり不便になっていました 
([参考](https://support.microsoft.com/ja-jp/microsoft-edge/%E6%96%B0%E3%81%97%E3%81%84-microsoft-edge-%E3%81%A7%E7%8F%BE%E5%9C%A8%E5%88%A9%E7%94%A8%E3%81%A7%E3%81%8D%E3%81%AA%E3%81%84%E6%A9%9F%E8%83%BD-4307f116-8184-0c59-dcb4-3c55e00f70bf)).
しかし徐々に改善されていて, 最近だと目次を表示する機能が復活しました.
それで手持ちの PDF 書籍に目次を追加すれば読みやすくなると思ったので, 既存の PDF に目次を追加する方法をまとめます.
基本的に [PDFtk](https://ja.wikipedia.org/wiki/PDFtk) でできます.


# PDF の目次

PDF の目次機能とはブックマークのことです. しおりと呼ばれることもあります.
この仕様は ISO 32000 で定められています (必須機能ではないのですが).

ひとつのブックマークはタイトル, レベル, ページ数の3個の情報を持ちます.
Rust 風に定義するとこんな感じです.

```rust
struct Bookmark {
    title: String,
    level: u32,
    page_number: u32,
}

type BookmarkInfo = Vec<Bookmark>;
```

タイトルとページ数は良いでしょう. ブックマークのレベルとは何かというと, 
書籍でいうと章レベル見出しがレベル1, 節レベル見出しがレベル2, 小節レベル見出しがレベル3, ..., という感じです.
LaTeX や Word などで自作した PDF ならばブックマークのリンク先をページ中の任意の要素に指定することができるのですが,
目次を後付けする場合, (Acrobat などのソフトウェアを用いない限り) ページ単位での指定しかできません.

PDFtk を用いて既存の PDF から目次データを抽出するコマンドがこちら.

```bash
$ pdftk <INPUT-FILE> dump_data_utf8 > metadata.txt
```

とするとメタデータ一覧が取得でき, その中にブックマークの情報も含まれます.
このメタデータ一覧はかなり長いので, テキストファイルに出力するようにします.


# 目次データの準備

さて, PDF に目次データを追加するには, あらかじめ目次データをテキストファイルとして準備しておくのがよいでしょう.
二つ目の参考文献では PDFtk の規定のフォーマット ([こちら](https://www.pdflabs.com/blog/export-and-import-pdf-bookmarks/)より引用)

```
BookmarkBegin
BookmarkTitle: PDF Reference (Version 1.5)
BookmarkLevel: 1
BookmarkPageNumber: 1
BookmarkBegin
BookmarkTitle: Contents
BookmarkLevel: 2
BookmarkPageNumber: 3
```

でそれを用意していますが, これでは入力がいささか面倒という問題があります.
目次情報はだいたいどこかからコピペしてくることができるはずで, 
加工が必要にしてもあまり面倒なことはしたくありません.

[SiddharthPant/booky](https://github.com/SiddharthPant/booky) というスクリプトは JSON 風の独自フォーマットを定義しており,
Python スクリプトで PDFtk 可読な形に変換しています.
それでも良いとは思いますが, 独自フォーマットというのはいただけません.
ここは YAML で同じことをしましょう.

```yaml
- PDF Reference (Version 1.5) 1
- 
  - Contents 3
```

ページ番号についてはフィールドを分けるのが正統だと思いますが, 入力が面倒なので, 
上記スクリプトを参考にスペース区切りで書くことにしてしまいます. 


# PDF に目次を追加

目次のない PDF ファイル `INPUT.pdf` に上記 PDFtk 形式のテキストファイル `toc.txt` に基づいて目次を追加するコマンドは

```bash
pdftk INPUT.pdf update_info_utf8 bookmarks.txt output OUTPUT.pdf
```

です. `OUTPUT.pdf` が目次情報が追加された出力 PDF ですが, 入力ファイルと同じ名前にはするべきではなかったはずです.

上記 YAML ファイルから PDFtk 形式に変換し, このコマンドを実行する Rust コードはこちら.

[https://github.com/osanshouo/pdftoc-rs](https://github.com/osanshouo/pdftoc-rs)

すぐに書けると思ったら案外苦労しました. Python ならもっとさくっと書けたのではと思いますが,
ただ Python で書いていたら見落としていたようなエラーハンドリングをちゃんとすべて指摘してくれるのがありがたいですね.
特にファイル I/O があるので破壊的操作をするツールですし.


# 参考文献
* [PDFのしおりってなに？ どうやって作るの？](https://www.antenna.co.jp/pdf/reference/pdf-shiori.html) - アンテナハウス
* [自炊したPDF加工についてのメモ &mdash; KaoriYa](https://www.kaoriya.net/blog/2017/01/03/)
* [How to Export and Import PDF Bookmarks](https://www.pdflabs.com/blog/export-and-import-pdf-bookmarks/) - PDF Labs
