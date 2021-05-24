+++
title = "BibJSONの仕様"
date = 2021-05-24
draft = true
[extra]
toc = true
[taxonomies]
tags = ["本", ]
+++

# はじめに

BibJSON についての公式情報とみなせるものは次の公式ウェブページくらいしかありません.

* [The purpose of BibJSON](http://okfnlabs.org/bibjson/)

これだけでは明らかに不十分に思えます. 仕様を補完する情報源として, 特に以下のページは参考になります.

* [BibJSON feedback report | Open Bibliography and Open Bibliographic Data](http://openbiblio.net/p/jiscopenbib2/bibjson-feedback-report/index.html)
* [Representing bibliographic data in JSON - rdmpage/bibliographic-metadata-json](https://github.com/rdmpage/bibliographic-metadata-json)
* [Open Bibliography for Science, Technology, and Medicine](https://aspace.repository.cam.ac.uk/bitstream/handle/1810/238394/obs-final.html?sequence=1&isAllowed=y)

しかし, 公式の仕様がないために, 人によって BibJSON の仕様が違うように見えます. これらの文献の間で既に矛盾しています.
逆に言うと, 確立した仕様はないので, 好きなように独自拡張しても怒られない訳です.

ということで, 本記事では私家版 BobJSON の仕様をまとめます.


# 一般論

書誌情報は基本的には [BibTeX](https://ja.wikipedia.org/wiki/BibTeX) 互換であるべきでしょう. つまり, 
`article`, `book`, `inproceedings` といったタイプがあり, 
それぞれ `author` や `title` といった必須項目を持ちます.
また, BibTeX キーに相当する "id" フィールドもあるべきでしょう.
つまり BibJON の基本形は次のようなものになります.

```json
{
    "type": "", 
    "id": "",
    "title": "",
    "author": [
    ],
    /* ... */
}
```

`author` は一般には複数の値を取りますから, オブジェクトのリストでなければなりません.


# 論文

論文に関しては公式に完全な例が載っているため, 独自拡張の余地はあまりありません.

## テンプレート

```json
{
    "type": "article", 
    "title": "",
    "author": [
        {"lastname": "", "firstname": ""}
    ],
    "year": "",
    "journal": {
        "name": "",
        "volume": "",
        "issue": {
            "number": ""
        },
        "pages": ""
    },
    "abstract": "",
    "identifier": [
        {"type":"doi", "id":""},
        {"type":"bibcode", "id":""}
    ]
}
```

## コメント

`author` は `"name": "Erdös, Paul"` という形でまとめて記述しても良いですが, テンプレートでは個人的な好みで明確に区分しました.

`pages` は `"pages: "1--15"` というように半角ハイフンふたつで区切ります. おそらくこれは BibTeX との互換性のためでしょう.

リスト `journal` に配置するオブジェクトには `name` に加えて `shortcode` を設定しても構いません.
省略名は書誌情報を表示する側で担当するべき処理だとは思いますが, 
しかし雑誌の正式名称がわからないが省略名はわかるということはありがちなので, 
そのような場合には `name` の代わりに `shortcode` を埋めるという使い方はできるでしょう.

なお `id` は手動ではなく管理アプリが自動で付与すべきという考えから, テンプレートからは除外してあります.


# 書籍

公式には書籍の例はありません. なので以下の BibJSON は独自仕様であり, 他の環境ではサポートされていません.

## テンプレート

```json
{
    "type": "book",
    "title": "",
    "author": [
        {"lastname": "", "firstname": ""}
    ],
    "editor": [
        {"lastname": "", "firstname": ""}
    ],
    "edition": "",
    "year": "",
    "publisher": {
        "name": "",
    },
    "identifier": [
        {"type": "isbn-13", "id": ""},
        {"type": "doi",     "id": ""}
    ],
    "keywords": [
        ""
    ]
}
```

## コメント

独自仕様とはいえ, 論文の `journal` を `publisher` に置き換えたくらいで, 誰が考えてもこうなるでしょう.
`publisher` には `location` などの情報を追加しても良いと思います.


# 書誌情報データベース

実際にはひとつのファイルに複数の書誌情報をまとめておきたいです.
この場合, 次のような形で並べることが想定されているようです.

```json
{
    "metadata": {
        "collection": "",
    },
    "records": [
        /* ここに上記エントリーを並べる */
    ]
}
```
