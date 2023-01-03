+++
title = "Debian11へアップデート"
date = 2023-01-03
[extra]
toc = true
[taxonomies]
tags = ["Linux"]
+++

Debian 10 (Buster) では glibc のバージョンが足りずに動かなかったのでアップデートした記録です.

# 環境

* Windows 11 22H2
* Debian 10 -> 11 on WSL2 


# アップデート

まずはアップデートを当てて現バージョンの最新環境にしておきます.

```bash
$ sudo apt update
$ sudo apt upgrade
```

続いて `/etc/apt/source.list` を次のように書き換えます.
`buster/updates` の部分が `bullseye-security` にまるっと変わっているのに注意です.

```
deb http://deb.debian.org/debian bullseye main
deb http://deb.debian.org/debian bullseye-updates main
deb http://security.debian.org/debian-security/ bullseye-security main
deb http://ftp.debian.org/debian bullseye-backports main
```

最後にアップデートを当てて終わりです. 
2回ほど yes/no を聞かれましたが, 何も問題なくヌルっとできます.

```bash
$ sudo apt update
$ sudo apt full-upgrade
```

# 参考文献
* [第4章 Debian 10 (buster) からのアップグレード](https://www.debian.org/releases/stable/i386/release-notes/ch-upgrading.ja.html)
* [debian 10 から11にアップグレードしてみた | ゆっくり遅報](https://www.yukkuriikouze.com/2021/08/17/4446/)
