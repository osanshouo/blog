+++
title = "UbuntuのGeForce 5000系ドライバ対応状況"
date = 2025-04-22
[taxonomies]
tags = [ "Linux", "GPU", ]
+++

※PCを新調する前に対応状況を調べたものです. まだ実際に試してはいません.
Windows 用とはバージョン番号が違うのでややこしい.

調査日: 2025-04-22


# ドライバのバージョン

* <https://www.nvidia.com/ja-jp/drivers/>

NVIDIA公式サイトで　GeForce 5000 系 (Blackwell), 例えば 5070 用の Linux 64bit 用ドライバを検索する.
するとバージョン 570 が配布されているので, このバージョンのドライバをインストールすればよいことがわかる.
現時点での安定最新版は 570.144 (2025-4-17) で, 大量のバグフィックスが含まれると[ニュース](https://news.mynavi.jp/article/20250416-3195052/)になっていたもの.

一方で 5060 Ti 用ドライバはベータ版である 575.51.02 (2025-4-16) のみとなっている.

## CUDA 12.8

* <https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html>

Linux で CUDA 12.8 を動かすにはドライバ 570.12 が必要な模様.



# Ubuntu 公式リポジトリ

* <https://packages.ubuntu.com/>

Ubuntu 公式リポジトリで nvidia driver を検索する.
Ubuntu 25.04 (Plucky Puffin) 用のパッケージに限定すること.
すると `nvidia-driver-570` が出てくる.

* <https://packages.ubuntu.com/plucky/nvidia-driver-570>

変更履歴を確認すると, NVIDIA が新バージョンの安定版ドライバを出すと
Ubuntu 側も速やかにバージョンアップしていることがわかる.

ただし4月に入ってから新バージョンは出ていないし, `nvidia-driver-575` パッケージもない.
従って 5060 Ti 用ドライバは現時点では公式リポジトリからは入手できないと思われる.
ベータ版ではなく安定版がリリースされるまで, 公式リポジトリは更新されないか？

