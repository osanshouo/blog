+++
title = "Option<&String>とOption<&str>"
date = 2021-05-05
[taxonomies]
tags = ["Rust"]
+++

[昨日の Rust コード](../04-pdf-toc/)の中で, `&Option<String>` を `Option<&str>` と比較したいシチュエーションがありました.
コマンドライン引数のパースの際に「引数がない, または引数が `--version` である」にマッチしたかったのです.
最初に書いたコードはこんな感じでした.

```rust
let args: Vec<_> = std::env::args().collect();
let arg: Option<&String> = args.get(1);

match arg {
    Some("--version") | None => {
        /* 省略 */
    },
    /* 以下省略 */
}
```

しかしこれはコンパイルが通りません. `arg` は `Option<&String>` であるのに対して, 
マッチの一つ目 `Some("--version")` は `Option<&str>` であり, 型が合っていません.
これを見て, `&String` は `Deref<Target=str>` ですから, `as_deref` を使えば良いだろうと次のように書き換えました.

```rust
let args: Vec<_> = std::env::args().collect();
let arg: Option<&String> = args.get(1);

match arg.as_deref() {
    Some("--version") | None => {
        /* 省略 */
    },
    /* 以下省略 */
}
```

しかしやはり型が合わないという理由でコンパイルエラーでした. はて？

`as_deref` のドキュメントには次のコード例が掲載されています 
([doc](https://doc.rust-lang.org/nightly/std/option/enum.Option.html#method.as_deref) より引用).

```rust
let x: Option<String> = Some("hey".to_owned());
assert_eq!(x.as_deref(), Some("hey"));
```

一瞬同じでは？ と思いますが, よく説明を読むとこのメソッドは `Option<T>` または `&Option<T>` を 
`Option<&T::Target>` に変換する, と書かれています.
今したいことは `Option<&T>` を `Option<&T::Target>` に変換することであり, 微妙に違います.
つまり `as_deref` は使えません.

`&String` を明示的に `&str` に変換する場合, `String::as_str` メソッドが使われます.
従って今の状況では `as_deref` ではなくこのメソッドで map すれば解決します.

```rust
let args: Vec<_> = std::env::args().collect();
let arg: Option<&String> = args.get(1);

match arg.map(String::as_str) {
    Some("--version") | None => {
        /* 省略 */
    },
    /* 以下省略 */
}
```

あるいは汎用的に `Deref` を呼ぶのでも構いません.

```rust
use std::ops::Deref;

let args: Vec<_> = std::env::args().collect();
let arg: Option<&String> = args.get(1);

match arg.map(Deref::deref) {
    Some("--version") | None => {
        /* 省略 */
    },
    /* 以下省略 */
}
```

あるいは今の場合, `arg: Option<&String>` が所有権を持っていないことが問題で,
所有権を持っていれば `as_deref` できます. つまり最初に引数のリスト `args` を確保するのではなく

```rust
let arg = std::env::args().nth(1);

match arg.as_deref() {
    Some("--version") | None => {
        /* 省略 */
    },
    /* 以下省略 */
}
```

とする手もあります.
