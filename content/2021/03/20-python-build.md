+++
title = "WSL2でPython環境構築 (2021年3月版)"
date = 2021-03-20
[extra]
toc = true
[taxonomies]
tags = [ "Python", "Linux", ]
+++

Win10 ノートを初期化して環境構築し直したので, 環境構築メモです.


# はじめに

Win10 で Python を扱う場合, Win10 側で実行するか, WSL を利用して Linux 環境で実行するかという選択肢があります.
多くのライブラリは Linux 向けに作成されているので, WSL を利用するのがおすすめです.

そうすると, 次に WSL1 と WSL2 という選択肢があります. 
WSL2 のメリットは主にファイル I/O が爆速であることと, docker が使えることでしょうか. 
逆にデメリットとしてメモリ食い虫であること, Win10 側のタスクマネージャーの情報量が減ることがあります.
メモリがカツカツなのでなければ WSL2 のほうが良いと思いますが, どちらでも構いません.


# Linux 環境構築

## WSL2 の導入

公式の [Windows 10 用 Windows Subsystem for Linux のインストール ガイド](https://docs.microsoft.com/ja-jp/windows/wsl/install-win10) に従ってください.
私は Debian (10.8) をインストールしました.

## Linux 環境構築

必要なパッケージをインストールしておきます. 

```shell
$ sudo apt update
$ sudo apt install build-essential gfortran wget
$ sudo apt install sudo apt install libreadline-dev libncursesw5-dev libssl-dev libsqlite3-dev libgdbm-dev libbz2-dev liblzma-dev zlib1g-dev uuid-dev libffi-dev libdb-dev tk-dev
```


# Python のインストール

Python は実行速度が遅いのでなるべく高速化するために自前ビルドします.
個人開発では仮想環境を利用する必要に迫られたことはないので venv 等いろいろありますが気にしなくてよいと思います.
本当に必要になったら docker を使えばよいでしょう.

[Python 公式](https://www.python.org/downloads/source/) から最新 stable のソースコードをダウンロードし解凍します.

```shell
$ wget https://www.python.org/ftp/python/3.9.2/Python-3.9.2.tar.xz
$ tar xf Python-3.9.2.tar.xz
$ cd Python-3.9.2
```

そして適当にオプションを設定したらビルドします. 
実行速度向上のために LTO や PGO を有効化します.
`make` の引数の `-j4` は 4 スレッド並列でコンパイルするという指示です. CPU に合わせて適当に増減してください.

```shell
$ ./configure --prefix=$HOME/.local --with-ensurepip --enable-optimizations --with-lto
$ make -j4
$ make altinstall
```

これでインストール完了です. 

```shell
$ python3.9
>>> print("Hello, world!")
Hello, world!
>>>
```

実行できない場合, `~/.local/bin` にパスが通っていることを確認してください.必要に応じて symlink を設定すると便利でしょう.

```shell
$ cd ~/.local/bin
$ ln -s python3.9 python3
$ ln -s pip3.9 pip3
```


# パッケージのインストール

パッケージは pip で管理します. pip を最新バージョンに更新しておきます.

```shell
$ pip3 install --upgrade pip
```

## Intel-MKL のインストール

NumPy や SciPy を pip でインストールすると標準では openblas を使用しますが, Intel-MKL を使用したほうが高速です.
いつの間にか Intel oneAPI Math Kernel Library に改称していた等, 以前環境構築したときとは要領が変わっていて戸惑いました.

[Intel](https://software.intel.com/content/www/us/en/develop/tools/oneapi/components/onemkl.html) からリンクを探してきて任意の場所にダウンロードします
(オフライン版でもオンライン版でも構いません).
シェルスクリプトになっているので `sudo` 付きで実行すると対話式のインストールが始まります.

```shell
$ sudo sh l_onemkl_p_2021.1.1.52_offline.sh
```

この際に最初は `Error opening terminal: xterm-256color` というエラーが出て困惑しましたが, その場合

```shell
$ export TERM=xterm-color
``` 

としてください ([参考文献](https://blog.bgbgbg.net/archives/4227)). 成功すると `/opt/intel` 配下にいろいろとファイルが配置されるはずです.

その後, `~/.profile` 等を編集し必要な環境変数を設定します (このパスも変更されているので注意してください).

```bash
export MKLROOT=/opt/intel/oneapi/mkl/latest
export LD_LIBRARY_PATH=$MKLROOT/lib/intel64:/opt/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin/:$LD_LIBRARY_PATH
export LIBRARY_PATH=$MKLROOT/lib/intel64:$LIBRARY_PATH
export PKG_CONFIG_PATH=$MKLROOT/tools/pkgconfig:$PKG_CONFIG_PATH
```

## NumPy と SciPy

`~/.numpy-site.cfg` というファイルを作成し, 次を書き込みます.

```cfg
[mkl]
library_dirs = /opt/intel/oneapi/mkl/latest/lib/intel64/
include_dirs = /opt/intel/oneapi/mkl/latest/include
mkl_libs = mkl_rt
lapack_libs =
```

そうしたら, NumPy と SciPy もソースからビルドします. `gfortran` が必要なのでインストールし忘れに注意してください.

```shell
$ pip3 install --no-binary :all: numpy
$ pip3 install --no-binary :all: scipy
```

## その他のパッケージ

その他のパッケージはソースビルドしなくてよいでしょう. 必要なものをインストールしてください.

```shell
$ pip3 install matplotlib sympy
```
