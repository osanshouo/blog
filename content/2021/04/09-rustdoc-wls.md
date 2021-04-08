+++
title = "WSL2でRustドキュメントを開く"
date = 2021-04-09
[taxonomies]
tags = ["Rust"]
+++

Rust には標準でドキュメントを開くツールが付属しており, 
`rustup doc` により the Book や標準ライブラリを,
`cargo doc --open` で開発中のクレートや依存クレートのドキュメントをブラウザで表示することができます.
ただしこれは WSL では (WSL1, WSL2 ともに) デフォルトではうまく動作しません.
開くべきドキュメントは WSL 側にあるものの, ブラウザは Windows 側にあるためです.

以前まで `rustup doc` 相当のことをするために nginx を使用して HTML ファイル等を配信するというアプローチをとっていましたが,
これは `cargo doc` の場合には (ひと手間かけないと) 使えません.
しかし rustup や cargo の issue を眺めていたところ, WSL 側のファイルパスを Windows 側のパスに変換し,
それを Windows 側のブラウザに渡すという完全な解決策を発見しました ([参考文献](#参考文献)を参照).
ただし Windows 側から WSL 側のファイルを直接読みに行っているので, 
ファイルアクセスは高速とは言い難いです. とはいえローカルで完結しているので,
ストレージの性能によりますが, オンラインドキュメントの場合と比較して遅いということはないと思います.


# 作業内容

Firefox で開く場合, WSL 側で

```bash
#! /bin/bash
WINPATH="file:///$(wslpath -m ${1})"
/mnt/c/Program\ Files/Mozilla\ Firefox/firefox.exe $WINPATH
```

というファイルを任意の場所に保存しパスを通します. 実行権限があることを確認してください (なければ `chmod 744 <script>` など). 
次に, 環境変数 `BROWSER` にこのスクリプトのパスを設定します.
`~/.bashrc` あたりに

```bash
export BROUWER=<上記スクリプトのフルパス>
```

と書き込んで bash を再読み込みします (`source ~/.bashrc` またはシェルを再起動). 以上で Rust のドキュメントがブラウザで開けるはずです.


# 参考文献
* [https://github.com/rust-lang/rustup/issues/2206#issuecomment-688089371](https://github.com/rust-lang/rustup/issues/2206#issuecomment-688089371)
* [https://github.com/rust-lang/cargo/issues/7557#issuecomment-791320960](https://github.com/rust-lang/cargo/issues/7557#issuecomment-791320960)
* [【WSL】パスのフォーマットを変換する wslpath コマンドの使い方](https://laboradian.com/wslpath-command-for-wsl/)
