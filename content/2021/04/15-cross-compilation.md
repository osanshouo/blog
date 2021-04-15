+++
title = "[Rust] ARMv8にクロスコンパイル"
date = 2021-04-15
[extra]
toc = true
[taxonomies]
tags = ["Rust"]
+++

ARMv8 で動くバイナリを Rust で生成するメモです.


# 環境

## host

* Debian 10.9 (WSL2) on Win10 20H2
* Rust 1.51 stable-x86_64-unknown-linux-gnu

## target

* ARMv8 (aarch64-unknown-linux-musl)


# 作業手順

Rust インストールが完了しており, `rustup` や `rustc` が使えるものとします.

## linker をインストール

```bash
sudo apt install gcc-aarch64-linux-gnu
```

## rust target をインストール

なるべく静的リンクしたかったので musl 版をインストールしました.

```bash
rustup target add aarch64-unknown-linux-musl
```

## コンパイル

rustc を直接使うならば, linker を忘れずに指定します.

```bash
rustc -C linker=aarch64-linux-gnu-gcc --target=aarch64-unknown-linux-musl hello_world.rs
```

cargo を使う場合, プロジェクトのルートディレクトリまたはホームディレクトリに `.cargo/config.toml` というファイルを作成し,
そこで linker を指定します. 
なおビルドのデフォルトターゲットとして設定する場合には, 最初の2行のコメントアウトを外してください.
デフォルト設定するのならばプロジェクトディレクトリに, そうでなければホームディレクトリに設定するのが良さそうです.

```toml
# [build]
# target = "aarch64-unknown-linux-musl"

[target.aarch64-unknown-linux-musl]
linker = "aarch64-linux-gnu-gcc"
```

そして target を指定してビルドします. 

```bash
cargo build --target aarch64-unknown-linux-musl
```


# 参考文献
* [Rustをcross compileしてRaspberry Pi3で動かすぞ！](https://qiita.com/0gajun/items/b4c354ba88a96749d353)
* [rustをインストールしてhello world をARM用にクロスコンパイルするまでの手順](https://qiita.com/tetsu_koba/items/1ab400a3d4ec9725b044)
* [rustのcargoでarm64 linux向けにクロスビルドする](https://qiita.com/tetsu_koba/items/d467f2b3c2bb8b816185#_reference-5d8caedaa6b5ed20b070)
* [x86_64 ubuntu上でcatapultをarm64用にビルドする(cow)](https://mijinc0.github.io/blog/post/20190602_building_catapult_for_arm/)
* [Cross-compilation - The rustup book](https://rust-lang.github.io/rustup/cross-compilation.html)
* [Configuration - The Cargo Book](https://doc.rust-lang.org/cargo/reference/config.html)
