+++
title = "[Rust] なぜスライスにwindows_mutはないのか"
date = 2021-01-09
[extra]
toc = true
[taxonomies]
tags = ["Rust", "イテレータ", ]
+++

Rust のスライスには [`windows`](https://doc.rust-lang.org/std/primitive.slice.html#method.windows) メソッドがあります.
これは指定した数の連続した要素の「サブスライス」を順に返すイテレータを作成します.
例えば次のコード

```rust
let slice = &[ 1, 1, 2, 3, 5, 8 ];

for arr in slice.windows(3) {
    println!("{:?}", arr);
}
```

を実行すると, `[1, 1, 2]`, `[1, 2, 3]`, `[2, 3, 5]`, `[3, 5, 8]` と順に表示されます.
大きさの決まった「窓」を先頭から順番にずらしていくイメージです.

よく似たメソッドに `chunks` があり, これは窓を重複なくずらすものです. 例えば

```rust
let slice = &[ 1, 1, 2, 3, 5, 8 ];

for arr in slice.chunks(3) {
    println!("{:?}", arr);
}
```

は `[1, 1, 2]`, `[3, 5, 8]` と順に表示されます. ほとんど同じものに見えますが, 実は両者には大きな違いがあります.
`chunks` には可変参照を返す対応物 `chunks_mut` があるのに対して, `windows` にはありません.
これはなぜでしょうか.


# `chunks` および `chunks_mut` について

これはほとんど同じもので, 前者の返り値 `std::iter::Chanks` は `Iterator<Item = &'a [T]>`,
後者の返り値 `std::iter::ChanksMut` は `Iterator<Item = &'a mut [T]>` です.
内部実装 ([chunks](https://doc.rust-lang.org/src/core/slice/iter.rs.html#1356-1431), 
[chunks_mut](https://doc.rust-lang.org/src/core/slice/iter.rs.html#1516-1593)) を見てもらえばわかるように,
これは要するにスライスを `split_at` または `split_at_mut` しています.

スライスのメソッド `split_at_mut` は興味深いメソッドで, 
ひとつの `&mut [T]` からふたつの `&mut [T]` を作り出すことができます.
Rust ではひとつのメモリ領域に対して同時に複数の可変参照が存在することはできませんが,
しかし今の場合, ふたつの `&mut [T]` が指す範囲が重複していないことが保証されているため, 安全です.
なので `split_at_mut` は内部では `unsafe` になっています.


# `windows` について

それでは `WindowsMut` のようなものは実装できるでしょうか？
これは要するに可変参照は同時にひとつしか存在できないというルールのために Rust では禁止されています.
イテレータの返り値はすべて同じライフタイムを持ちますから, 
`WindowsMut` が上のような調子で `&mut [T]` を生成し続けてしまうと同じ領域を指す可変参照が同時に存在してしまいます.


# streaming iterator

しかしイテレータとして実装するのでなければ `WindowsMut` を実現することができます.
これは次の `next` までに先に生成した `&mut [T]` がドロップされていることが保証されていればよいからで,
streaming iterator と呼ばれる種類のものになります.
streaming iterator については 
[[Rust] 自分への参照を返すイテレータもどき: streaming iterator](https://qiita.com/osanshouo/items/0aa01131adeaf4bed9ba) 
を, `windows_mut` の実装については参考文献をご覧ください.


# 参考文献
* [https://users.rust-lang.org/t/iterator-over-mutable-windows-of-slice/17110](https://users.rust-lang.org/t/iterator-over-mutable-windows-of-slice/17110)
