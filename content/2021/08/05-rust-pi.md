+++
title = "[Rust] 円周率の表記"
date = 2021-08-05
[taxonomies]
tags = ["Rust", ]
+++

Rust 1.53 において stable で解禁された non-ascii-idents ですが, 私にとってその最も重要な用途は円周率をギリシャ文字 `π` で表記することです.
これは次のような形で実現されます.

```rust
#![allow(mixed_script_confusables)]
use std::f64::consts::PI as π;
```

円周率の π なんて見慣れているはずですが, コード中にギリシャ文字が出てくると慣れるまではすこし驚くかもしれません.
おそらくフォントの問題もあるでしょう (エディタに Computer Modern や Latin Modern Math を設定している人なんてほとんどいないと思います)

冒頭の mixed_script_confusables の許可ですが, これは non-ascii-ident が意図せず紛れ込んでいる可能性を警告するもので,
コード中に特定の[用字](https://ja.wikipedia.org/wiki/%E7%94%A8%E5%AD%97_(Unicode))を含む識別子がひとつだけ存在するかをチェックします.
従って上の場合にはギリシャ文字識別子が円周率以外にもコード中に存在すればこのアトリビュートがなくとも警告は出ないのですが,
円周率しかないこともしばしばでしょうし, 常にこのアトリビュートを設定しておけばよいと思います.

# 参考文献
* [Announcing Rust 1.53.0 | Rust Blog](https://blog.rust-lang.org/2021/06/17/Rust-1.53.0.html)
* [MIXED_SCRIPT_CONFUSABLES in rustc_lint::non_ascii_idents - Rust](https://doc.rust-lang.org/stable/nightly-rustc/rustc_lint/non_ascii_idents/static.MIXED_SCRIPT_CONFUSABLES.html)
