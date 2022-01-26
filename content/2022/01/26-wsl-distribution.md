+++
title = "WSL用Linuxディストリビューションについて"
date = 2022-01-26
[taxonomies]
tags = ["Linux", "Windows", ]
+++

以前 Microsoft Store で WSL 用 Arch Linux が配布されていたものの, 野良ビルドで果たして安全か？ という話がありました.

* [WSL対応「Arch Linux」が“Microsoft Store”に登場 ～ただし偽物？ - やじうまの杜 - 窓の杜](https://forest.watch.impress.co.jp/docs/serial/yajiuma/1184731.html)

今となっては欲しいディストリビューションがあるのなら Docker で入れればよいというだけの話ですが, ストアから2クリックでインストールできるのは便利すぎます. 
しかし既にこのパッケージはストアから削除されたようです.
他のディストリビューションも確認しましたが, 上記記事から状況はおおよそ変わっていないようです.
つまり, Ubuntu, Debian, OpenSUSE, Kali Linux, Alpine, Fedora Remix あたりが並んでいるだけで, 他に気になるディストリビューションはストアにはありませんでした.

一方 GUI に関しては Microsoft が Win11 で正式に対応したので, サードパーティ製アプリが不要になったようです. 

* [WSL で Linux GUI アプリを実行する | Microsoft Docs](https://docs.microsoft.com/ja-jp/windows/wsl/tutorials/gui-apps)

まだ VcXsrv を使っているので, 環境を再構築する際に試してみたいところです.
デスクトップ環境がそろそろ時代遅れになりつつあるので, アップデートしたいところなのですが.
