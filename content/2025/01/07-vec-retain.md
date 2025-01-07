+++
title = "[Rust] Vec<T>の要素を条件を満たすかで分割する"
date = 2025-01-07
[extra]
toc = true
[taxonomies]
tags = [ "Rust", ]
+++

Rust において, `Vec<T>` が与えられたとき, 条件を満たす要素だけを残し,
条件を満たさない要素を取り出して新しい `Vec<T>` を作ることを考えます.


# イテレータとして扱う

もとの `Vec<T>` の要素を順に見ていき, 条件を満たすものに対して何らかの処理を行いたい, という場合は, 
[`Iterator::filter`](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.filter) の出番です. 

```rust
fn main() {
    let vec = vec![
        1, 1, 2, 3, 5, 8, 13, 21, 34, 55,
    ];
    
    // 偶数だけ取り出す
    for a in vec.iter().filter(|&a| a%2 == 0) {
        println!("{}", a);
    }
}
```


# 除去された要素を別の `Vec<T>` にまとめる

しかし, 条件を満たす要素だけを残した `Vec<T>` を作りたい,
除去された要素はまとめて別の `Vec<T>` として確保したい, という場合は良い感じのメソッドが見当たらず, ちょっと書くのが面倒です.
近いメソッドとしては [`Vec::retain`](https://doc.rust-lang.org/std/vec/struct.Vec.html#method.retain) がありますが, 
これは `Vec<T>` の要素のうち条件を満たさないものをすべて除去するメソッドで, 除去された要素は消去されてしまい二次利用できません.

単純にインデックスアクセスで書くとこんな感じでしょうか.

```rust
fn main() {
    let mut vec = vec![
        1, 1, 2, 3, 5, 8, 13, 21, 34, 55,
    ];
    
    // 偶数だけ残し, 除去された要素を `rem` として確保する.
    let rem = myretain(&mut vec, |&a| a%2 == 0);
    println!("{:?}", &vec); // [2, 8, 34]
    println!("{:?}", &rem); // [1, 1, 3, 5, 13, 21, 55]
}

fn myretain<T, F>(vec: &mut Vec<T>, mut f: F) -> Vec<T>
where 
    F: FnMut(&T) -> bool 
{
    let mut rem = Vec::new();
    let mut i = 0;
    while i < vec.len() {
        if !f(&vec[i]) {
            let a = vec.remove(i);
            rem.push(a);
        } else {
            i += 1;
        }
    }
    
    rem
}
```

ただ, このように先頭から順に処理する方針では, 何度も $O(n)$ のコストがかかる 
[`remove`](https://doc.rust-lang.org/std/vec/struct.Vec.html#method.remove) を呼び出す必要があり, 
あまり効率的とは言えないかもしれません.
ドキュメントにあるように, `vec` の要素の順序が重要でないなら `swap_remove` に置き換えた方が良いでしょう.
