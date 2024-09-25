+++
title = "Rust edition 2024に向けてrand::Rng::genが改名される模様"
date = 2024-09-26
[taxonomies]
tags = [ "Rust", ]
+++

Rust edition 2024 は 2025年2月20日にリリースされる予定の Rust 1.85 と同時にリリースされる見通しです.
* [Rust 2024 🚧 - The Rust Edition Guide](https://doc.rust-lang.org/nightly/edition-guide/rust-2024/index.html)

Edition 2024 には過去の edition と同様にいくつかの破壊的な変更が含まれる予定です.
言うまでもなく後方互換性には配慮されており, 明示的に edition を上げない限り, 
既存のコードは edition 2021 ないしそれ以前の edition のコードとして処理されるので,
過去の Rust コードが何もしていないのに動かなくなることはありません.

Edition 2024 での変更点の中で個人的に影響が大きいのが, `gen` がキーワードとして予約されるというものです.
* [gen keyword - The Rust Edition Guide](https://doc.rust-lang.org/nightly/edition-guide/rust-2024/gen-keyword.html)

この結果, `gen` という識別子を含むコードをそのまま edition 2024 に切り替えるとコンパイルに失敗すると思われます.
最小限の修正で済ませるには, 既存の識別子 `gen` を
[raw identifier](https://doc.rust-lang.org/nightly/reference/identifiers.html#raw-identifiers) と呼ばれる形 `r#gen` に置き換えれば, 
キーワードではない識別子 `gen` として解釈されるので OK です. 詳細は上記 Edition Guide をご覧ください.
これはコマンド

```
cargo fix --edition
```

により自動的に実行できます.

問題は, `gen` という識別子が [`rand`](https://docs.rs/rand/latest/rand/) クレートという使用頻度の高いクレートの基本的なメソッド名 
(`Rng::gen`) として採用されていることです. 次の issue
* [CHANGE: Rename `Rng::gen` to avoid conflicting with a keyword in Rust 2024 · Issue #1435 · rust-random/rand · GitHub](https://github.com/rust-random/rand/issues/1435)

での議論により, `Rng::gen` は `Rng::random` に改名されることになりました.
この名称は [`rand::random`](https://docs.rs/rand/latest/rand/fn.random.html) 関数とも整合的です.
なお `Rng::gen` は一応非推奨 (deprecated) として残されるようです ([commit](https://github.com/vks/rand/commit/bd304d2e730a943fa9ac5a939355f3f7bd37c611)).

この変更は `rand 0.9` にて反映される予定です.
* [Tracker: rand 0.9 · Issue #1165 · rust-random/rand · GitHub](https://github.com/rust-random/rand/issues/1165)

早く `rand 1.0` にならないかな～と思っていたのですが, まさかこんな変更が必要になるとは.
