+++
title = "AV1全部盛りFFmpegのビルド (2021年6月版)"
date = 2021-06-17
[extra]
toc = true
[taxonomies]
tags = ["Linux", "動画", ]
+++

[FFmpeg](https://ffmpeg.org/) は言わずと知れた動画エンコード/デコードツールです.
`sudo apt install ffmpeg` でインストールできるものの, バージョンが古かったり必要なライブラリが入っていなかったりするので,
これらが問題になるならば自前ビルドが必要です.
本記事では FFmpeg で AV1 関係のツール (libaom, SVT-AV1, dav1d, rav1e) を全部使えるようにします.

基本的には公式のコンパイル手順に従うだけですが, 依存ライブラリが多いためちょっと気合いが要ります.
ただ要するに外部ライブラリをビルドした上で FFmpeg をビルドするというだけなので, 難しくはないはずです.
なお著作権と特許その他に関しては各自で確認をお願いします.


# 環境

* Debian 10.9 on WSL2 (Win10 20H2)
* FFmpeg 2021-06-16 (commit 604924a069735f3f1fd56b5dd125e68d402f15ba)


# 準備

## 作業場所の作成

公式はホームディレクトリに諸々を置いていますが, 日常的に見える場所に置きたくないので, 次のようにします.

* ソース: `~/.ffmpeg-src`
* 中間生成物: `~/.ffmpeg-build`
* 最終成果物: `~/.ffmpeg`

```bash
mkdir ~/{.ffmpeg,.ffmpeg-build,.ffmpeg-src}
```


## 依存パッケージ

最初にビルドに必要なパッケージをインストールします.

```bash
sudo apt install \
  autoconf \
  automake \
  build-essential \
  cmake \
  git-core \
  libass-dev \
  libfreetype6-dev \
  libgnutls28-dev \
  libtool \
  libvorbis-dev \
  meson \
  ninja-build \
  pkg-config \
  texinfo \
  wget \
  yasm \
  zlib1g-dev
```

`build-essential`, `git`, `pkg-config`, `wget` あたりは既にインストールされていることが多いと思います.


# ライブラリのビルド

基本的なライブラリはほぼすべて apt で済みます. このあたりのものは枯れている部類なので, 最新版にこだわらなくても良いでしょう.
唯一気になるのは libaom ですが, どうせ使わないので何でもよいです.

```bash
sudo apt install \
  nasm \
  libx264-dev \
  libx265-dev libnuma-dev \
  libvpx-dev \
  libmp3lame-dev \
  libopus-dev \
  libaom-dev 
```


## FDK-AAC

FDK-AAC はライセンスの問題があり, apt ソースに non-free を含めている場合のみ apt でインストールできます.

```bash
sudo apt install libfdk-aac-dev
```

そうでないならば自前ビルドします.

```bash
cd ~/.ffmpeg-src && \
git clone --depth 1 https://github.com/mstorsjo/fdk-aac && \
cd fdk-aac && \
autoreconf -fiv && \
./configure --prefix="$HOME/.ffmpeg-build" --disable-shared && \
make -j4 && \
make install
```

## SVT-AV1

SVT-AV1 は apt では手に入らないのでビルドが必要です.

```bash
cd ~/.ffmpeg-src && \
git clone --depth=1 https://gitlab.com/AOMediaCodec/SVT-AV1.git && \
cd SVT-AV1/Build && \
cmake -G "Unix Makefiles" \
  -DCMAKE_INSTALL_PREFIX="$HOME/.ffmpeg-build" \
  -DCMAKE_BUILD_TYPE=Release \
  -DBUILD_DEC=OFF \
  -DBUILD_SHARED_LIBS=OFF .. && \
make -j4 && \
make install
```

## dav1d

dav1d は apt で手に入りますが, バージョンが古いので自前ビルドします.

```bash
cd ~/.ffmpeg-src && \
git clone --depth 1 https://code.videolan.org/videolan/dav1d.git && \
mkdir dav1d/build && \
cd dav1d/build && \
meson setup \
  -Denable_tools=false \
  -Denable_tests=false \
  --default-library=static .. \
  --prefix "$HOME/.ffmpeg-build" \
  --libdir="$HOME/.ffmpeg-build/lib" && \
ninja && \
ninja install
```

## rav1e

rav1e は apt では手に入らないのでビルドします. 
なおビルドには Rust 1.51 以降が必要ですが, Rust 一式 (rustc と cargo) のインストールは完了しているものとします.
さらに, Rust で C-API をビルドするために `cargo-c` が必要なので, あらかじめインストールしておきます.

```bash
cargo install cargo-c
```

準備を終えたら rav1e をビルドします.

```bash
cd ~/.ffmpeg-src && \
wget https://github.com/xiph/rav1e/archive/refs/tags/v0.4.1.tar.gz && \
tar xf v0.4.1.tar.gz && \
cd rav1e-0.4.1 && \
cargo cinstall --release \
  --prefix=$HOME/.ffmpeg-build \
  --libdir=$HOME/.ffmpeg-build/lib \
  --includedir=$HOME/.ffmpeg-build/include
```

ただし, どうも共有ライブラリがあると FFmpeg のビルド時にそちらにリンクしに行くようで, うまく動作しません. 
削除しておきます.

```bash
rm ~/.ffmpeg-build/lib/librav1e.so*
```


# FFmpeg のビルド

ここまで来たらいつも通りの `.configure`, `make`, `make install` のセットで終わりです.
なおどうも GnuTLS をつけようとすると configure の際に pkg-config で見つけられないと怒られるので, 
`--enable-gnutls` を外し `--enable-openssl` としています.

```bash
cd ~/.ffmpeg-src && \
wget https://ffmpeg.org/releases/ffmpeg-snapshot.tar.bz2 && \
tar xf ffmpeg-snapshot.tar.bz2 && \
cd ffmpeg && \
PKG_CONFIG_PATH="$HOME/.ffmpeg-build/lib/pkgconfig" ./configure \
  --prefix="$HOME/.ffmpeg-build" \
  --pkg-config-flags="--static" \
  --extra-cflags="-I$HOME/.ffmpeg-build/include" \
  --extra-ldflags="-L$HOME/.ffmpeg-build/lib" \
  --extra-libs="-lpthread -lm" \
  --ld="g++" \
  --bindir="$HOME/.ffmpeg/bin" \
  --disable-ffplay \
  --enable-gpl \
  --enable-openssl \
  --enable-libaom \
  --enable-libass \
  --enable-libfdk-aac \
  --enable-libfreetype \
  --enable-libmp3lame \
  --enable-libopus \
  --enable-libsvtav1 \
  --enable-libdav1d \
  --enable-librav1e \
  --enable-libvorbis \
  --enable-libvpx \
  --enable-libx264 \
  --enable-libx265 \
  --enable-nonfree && \
make -j8 && \
make install
```


# 使ってみる

`.bashrc` か `.profile` あたりでパスを通しておきます. 既にパスの通った場所に bin ファイルを移動しても問題ありません.

```bahs
PATH="$HOME/.ffmpeg/bin:$PATH"
```

## 動作確認

有効化したライブラリは `ffmpeg` を実行すれば確認できます.

> configuration: --prefix=/home/osanshouo/.ffmpeg-build --pkg-config-flags=--static --extra-cflags=-I/home/osanshouo/.ffmpeg-build/include --extra-ldflags=-L/home/osanshouo/.ffmpeg-build/lib --extra-libs='-lpthread -lm' --ld=g++ --bindir=/home/osanshouo/.ffmpeg/bin --disable-ffplay --enable-gpl --enable-openssl --enable-libaom --enable-libass --enable-libfdk-aac --enable-libfreetype --enable-libmp3lame --enable-libopus --enable-libsvtav1 --enable-libdav1d --enable-librav1e --enable-libvorbis --enable-libvpx --enable-libx264 --enable-libx265 --enable-nonfree

また, システムのもの以外は静的にリンクされているので, ソースコードおよび中間生成物を削除しても構いません.

```bash
$ ldd ffmpeg
	linux-vdso.so.1 (0x00007ffd940c2000)
	libxcb.so.1 => /usr/lib/x86_64-linux-gnu/libxcb.so.1 (0x00007fc6610ba000)
	libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007fc660f37000)
	libass.so.9 => /usr/lib/x86_64-linux-gnu/libass.so.9 (0x00007fc660d04000)
	libfreetype.so.6 => /usr/lib/x86_64-linux-gnu/libfreetype.so.6 (0x00007fc660c48000)
	libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007fc660a2a000)
	libbz2.so.1.0 => /lib/x86_64-linux-gnu/libbz2.so.1.0 (0x00007fc660a17000)
	libvpx.so.5 => /usr/lib/x86_64-linux-gnu/libvpx.so.5 (0x00007fc6607ec000)
	libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007fc6607cb000)
	liblzma.so.5 => /lib/x86_64-linux-gnu/liblzma.so.5 (0x00007fc6607a3000)
	libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007fc66079e000)
	libaom.so.0 => /usr/lib/x86_64-linux-gnu/libaom.so.0 (0x00007fc6602f0000)
	libmp3lame.so.0 => /usr/lib/x86_64-linux-gnu/libmp3lame.so.0 (0x00007fc660078000)
	libopus.so.0 => /usr/lib/x86_64-linux-gnu/libopus.so.0 (0x00007fc66001a000)
	libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007fc660000000)
	librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007fc65fff6000)
	libvorbis.so.0 => /usr/lib/x86_64-linux-gnu/libvorbis.so.0 (0x00007fc65ffc8000)
	libvorbisenc.so.2 => /usr/lib/x86_64-linux-gnu/libvorbisenc.so.2 (0x00007fc65ff1d000)
	libx264.so.155 => /usr/lib/x86_64-linux-gnu/libx264.so.155 (0x00007fc65fc5f000)
	libx265.so.165 => /usr/lib/x86_64-linux-gnu/libx265.so.165 (0x00007fc65ed10000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fc65eb4f000)
	/lib64/ld-linux-x86-64.so.2 (0x00007fc6642d2000)
	libXau.so.6 => /usr/lib/x86_64-linux-gnu/libXau.so.6 (0x00007fc65e94b000)
	libXdmcp.so.6 => /usr/lib/x86_64-linux-gnu/libXdmcp.so.6 (0x00007fc65e745000)
	libfribidi.so.0 => /usr/lib/x86_64-linux-gnu/libfribidi.so.0 (0x00007fc65e728000)
	libfontconfig.so.1 => /usr/lib/x86_64-linux-gnu/libfontconfig.so.1 (0x00007fc65e6e2000)
	libharfbuzz.so.0 => /usr/lib/x86_64-linux-gnu/libharfbuzz.so.0 (0x00007fc65e5e5000)
	libpng16.so.16 => /usr/lib/x86_64-linux-gnu/libpng16.so.16 (0x00007fc65e5ac000)
	libstdc++.so.6 => /usr/lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007fc65e428000)
	libogg.so.0 => /usr/lib/x86_64-linux-gnu/libogg.so.0 (0x00007fc65e21f000)
	libnuma.so.1 => /usr/lib/x86_64-linux-gnu/libnuma.so.1 (0x00007fc65e211000)
	libbsd.so.0 => /usr/lib/x86_64-linux-gnu/libbsd.so.0 (0x00007fc65e1f5000)
	libexpat.so.1 => /lib/x86_64-linux-gnu/libexpat.so.1 (0x00007fc65e1b8000)
	libuuid.so.1 => /lib/x86_64-linux-gnu/libuuid.so.1 (0x00007fc65e1af000)
	libglib-2.0.so.0 => /usr/lib/x86_64-linux-gnu/libglib-2.0.so.0 (0x00007fc65e090000)
	libgraphite2.so.3 => /usr/lib/x86_64-linux-gnu/libgraphite2.so.3 (0x00007fc65e063000)
	libpcre.so.3 => /lib/x86_64-linux-gnu/libpcre.so.3 (0x00007fc65dfed000)
```

## AV1 にエンコード

rav1e を使うときは `librav1e` を, SVT-AV1 を使うときは `libsvtav1` を指定します.
デフォルト設定で軽く試した限りでは rav1e はかなり遅い一方で, SVT-AV1 は思っていたよりかなり速く実用レベルという感じでした.
ただこのあたりはオプションの設定次第で大きく変わるかもしれません.

```bash
ffmpeg -i input.mp4 -c:v libsvtav1 output.webm
```


# 参考文献
* [CompilationGuide/Ubuntu – FFmpeg](https://trac.ffmpeg.org/wiki/CompilationGuide/Ubuntu)
* [ffmpegをビルドしなおしてみましょう2021 - ねこにコベイン](https://nyarinkopv.hatenablog.com/entry/2021/01/01/155908)
* [video - How do I use FFmpeg and rav1e to create high quality AV1 files? - Ask Ubuntu](https://askubuntu.com/questions/1189174/how-do-i-use-ffmpeg-and-rav1e-to-create-high-quality-av1-files)
