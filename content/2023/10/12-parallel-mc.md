+++
title = "[Rust] モンテカルロ法の並列化"
date = 2023-10-12
[taxonomies]
tags = ["Rust", "数値解析", ]
+++

Edge に実装されたチャット AI くんとお喋りしてみたら, モンテカルロ法の並列化くらい簡単にできるよね？ と言われたので, 
RTA 的なノリでさっと書いてみました.

# `Cargo.toml`

```toml
[dependencies]
rand = "0.8"
rand_xoshiro = "0.6"
```


# `main.rs`

```rust
//! 並列計算の練習としての, モンテカルロ法による円周率の算出.

use std::thread;
use rand::{Rng, SeedableRng};

const N: usize = 1024 * 1024 * 1024;
const THREADS: usize = 4;

/// モンテカルロ法で円周率を求めるルーチンのコア部分.
/// 
/// [0, 1) 区間から一様にふたつの実数 `x`, `y` を生成し, 点 `(x, y)` が
/// 単位円の中に存在するならば (つまり $x^2 + y^2$ が 1 以下ならば) 合格.
/// この処理を `N` 個の点について行い, 合格した点 `(x, y)` の数を出力する.
/// 
/// 入力として PRNG を受け取る.
fn montecarlo<T: Rng>(mut rng: T) -> usize {
    let mut count: usize = 0;
    let (mut x, mut y): (f64, f64);

    for _ in 0..N {
        x = rng.gen();
        y = rng.gen();
    
        if x*x + y*y <= 1. {
            count += 1;
        }
    }

    println!("count = {}", count);

    count
}


/// メイン関数. `THREADS` 個のスレッドを生成し, 各スレッドで関数 `montecarlo` を
/// 実行し, その結果を集計して円周率を算出する.
fn main() {
    // PRNG として XOSHIRO を採用し, ここでシード値を与えて初期化
    let mut rng = rand_xoshiro::Xoshiro256StarStar::seed_from_u64(123);
    // 集計用のカウンター
    let mut count: usize = 0;


    // スレッドを操作するハンドルの集合
    let mut handles = Vec::new();

    for _ in 0..THREADS {
        // 各スレッド用に PRNG を
        rng.jump();
        let rng = rng.clone();
        
        let handle = thread::spawn(|| {
            montecarlo(rng)
        });
        handles.push(handle);
    }

    for handle in handles.into_iter() {
        count += handle.join().unwrap();
    }
    
    println!("pi = {}", 4. * count as f64/(N * THREADS) as f64);
}
```
