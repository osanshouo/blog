+++
title = "WSL2にdockerを導入"
date = 2021-03-23
[taxonomies]
tags = [ "Linux", ]
+++

せっかく WSL2 に移行したので docker もインストールしてみました.

# 導入手順

インターネット検索すれば日本語の記事がたくさん出てきますが, WSL2 はかなり新しい技術で変化が非常に速いですから,
公式の情報に従うのが一番でしょう. 幸いにも日本語化されているのでとても楽です.

* [Docker Desktop WSL 2 バックエンド &mdash; Docker-docs-ja 19.03 ドキュメント](https://docs.docker.jp/docker-for-windows/wsl.html)
* [Windows Subsystem for Linux で Docker コンテナーの使用を開始する | Microsoft Docs](https://docs.microsoft.com/ja-jp/windows/wsl/tutorials/wsl-containers)

この通りにインストールしたら簡単にできました. Linux 側に docker をインストールする必要はなく,
Win10 側で Docker Desktop が動いていれば `docker` コマンドが通ります (！).

勝手にスタートアップに登録されるのですが, 起動時にそこそこ負荷がかかるしメモリも圧迫します.
日常的に使うのならその方が便利なのでしょうけれども, 導入した PC ではそんなに頻繁には使わないと思われるのでオフにしました.
使うときに起動すればよいでしょう.


# 使い方

docker はすぐにコマンドを忘れるんですよね... 

## イメージ

* `docker images` または `docker image ls`: ローカルにあるイメージの一覧
* `docker pull debian:stable-slim` とか: Docker Hub からイメージをダウンロード

## コンテナ

* `docker ps -a`: コンテナの稼働状況の一覧
* `docker run -it [image]`: `[image]` をもとにコンテナを作成し対話モードでアタッチ
    * `--name [name]` でコンテナ名を指定
    * `-v [HOST]:[CONTAINER]` でホスト側のパス `[HOST]` をコンテナ側のパス `[CONTAINER]` としてマウント
    * 注意: オプションはイメージ名の前で指定すること
* `docker start [id]`: コンテナ `[id]` を起動
* `docker stop [id]`: コンテナ `[id]` を停止
* `docker attach [id]`: 起動しているコンテナ `[id]` にアタッチ
* `C-p C-q`: コンテナからデタッチ 
    * [この記事](https://qiita.com/hironobu_s/items/358b0ba5a7089521b60e)に従って WSL2 側の設定ファイルをいじれば変更できる

## その他

* `docker cp [file] [id]:[path]`: ローカルのファイル `[file]` をコンテナ `[id]` のパス `[path]` にコピー
    * ホスト側とコンテナ側は逆でも可
    * コンテナが停止していてもよい
