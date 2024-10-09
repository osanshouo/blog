+++
title = "Python 3.13.0を試してみた"
date = 2024-10-09
[extra]
toc = true
[taxonomies]
tags = [ "Python", ]
+++

2024-10-07 に Python 3.13.0 が[リリースされました](https://pythoninsider.blogspot.com/2024/10/python-3130-final-released.html). 
リリースノートはこちら:
* [What’s New In Python 3.13 — Python 3.13.0 documentation](https://docs.python.org/3.13/whatsnew/3.13.html)

個人的な注目点はふたつです.

* Global Interpreter Lock (GIL) の無効化された free-threaded モードが実験的に実装されました. 
これまで Python での高速な並列計算のためにはマルチプロセス化するしかなかった訳ですが,
これにより Python でのマルチスレッド並列計算が可能になりました.
* 実験的な JIT コンパイラが実装されました.
これにより Python の最大の弱点であった実行速度の遅さが改善に向かうかもしれません.

もっとも, 実行速度が必要なら最初から Rust で書くよ, という話もありますが...


# インストール

JIT コンパイラを有効化してビルドするためには `clang-18` が必要です. 必要なら次のドキュメントに従ってインストールします.

* [cpython/Tools/jit at main · python/cpython · GitHub](https://github.com/python/cpython/tree/main/Tools/jit)

基本的な Python のビルドおよびインストールの手順は以前の記事「[WSL2でPython環境構築 (2021年3月版)](@/2021/03/20-python-build.md)」そのままですが, 
GIL 無効化および JIL コンパイラ有効化を `./configure` のオプションで明示的に指定する必要があります.

```bash
./configure \
    --prefix=$HOME/.local \
    --with-ensurepip \
    --enable-optimizations \
    --with-lto \
    --disable-gil \
    --enable-experimental-jit=yes
```

公式ドキュメントはこちら:

* [3. Configure Python — Python 3.13.0 documentation](https://docs.python.org/3/using/configure.html)

`--disable-gil` オプションをつけてビルドすると, GIL が有効な (旧式の) バイナリ `python3.13` と
GIL が無効化された (実験的な) バイナリ `python3.13t` が生成されます.


# JIT コンパイル

例として以前書いた SymPy のコードを実行してみます.

* [[SymPy] Lie変換摂動論の方程式の導出](@/2021/08/12-lie-transform.md)

上の configure オプションはデフォルトで JIT コンパイラを有効化し, 
環境変数 `PYTHON_JIT=0` が設定されているときにのみ JIT コンパイラを無効化する設定になります.

実際に試してみたところ, `time env PYTHON_JIT=0 python3 lie.py` と `time python3 lie.py` でほぼ実行時間に差はなく,
むしろ (実行時の条件によるとは思いますが) JIT 無効化時の方が安定している印象です.
現時点ではまだあまり JIT の恩恵はないようです (もしくは何か失敗しているのかもしれません).


# マルチスレッド計算

GIL を実行時に有効化するにはコマンドラインオプション `-X gil=1` を渡します.
簡単なマルチスレッドプログラムはこんな感じになると思います.

```python
import threading

def main_task():
    // ここにコードを書く

thread1 = threading.Thread(target=main_task, args=[])
thread2 = threading.Thread(target=main_task, args=[])

thread1.start()
thread2.start()

thread1.join()
thread2.join()
```

試してみた結果, 確かに GIL を無効化することでマルチスレッド計算が高速化していましたが, 
約6秒の処理が約5秒になったくらいで, 期待ほどの高速化は達成できませんでした.
