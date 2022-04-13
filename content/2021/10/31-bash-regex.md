+++
title = "[shell] 正規表現にマッチするテキストを抽出"
date = 2021-10-31
[taxonomies]
tags = [ "Linux", ]
+++

テキストからマッチする部分を取り出すには `grep` の `-o` オプションを使うのが簡単です.
デフォルトでは `grep` は単一行ごとにマッチするかを判定しますが, 
`-P` オプションをつければ複数行でのマッチが可能になります.

* [grepで複数行を対象にサーチ - minus9d&#39;s diary](https://minus9d.hatenablog.com/entry/20130209/1360377537)

一方, `grep` には複数のマッチ条件を指定する `-e` オプションがあります.
しかし `-P` と `-e` は併用することができません. 正規表現の OR `|` を使うのが良いと思います.
たとえば HTML 文書から `<h1>` タグおよび `<h2>` タグを抜き出すには次のようにします.

```bash
grep -Poz '<h1[\s\S]*?</h1>|<h2[\s\S]*?</h2>' index.html
```