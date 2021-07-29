+++
title = "[Rust] 論理否定演算子の視認性向上策"
date = 2021-07-29
[extra]
toc = true
[taxonomies]
tags = [ "Rust", ]
+++

Rust には特徴的な一文字の単項演算子 `?` があり, これは識別子ないし `()` の後ろにつき, かなり快適です.
これはこの演算子は基本的には軽く読み飛ばせばよいという趣旨のもので, それに応じて軽い表記になっているためです.

```rust
use std::fs;

fn main() -> Result<(), std::io::Error> {
    for dir in fs::read_dir("./")? {
        let entry = dir?;
        println!("{:?}", entry.path());
    }

    Ok(())
}
```

それに対して, 論理否定演算子 `!` は真理値をひっくり返すという作用の重大さの割に正直なところ視認性が悪いです.
識別子の前につき, しかも単なる縦棒に近いため, うっかり見落とすのではないかといつもひやひやします.

```rust
/// 引数 (bool) が false なら `Ok!` と出力する. true ならば何もしない.
fn check_false(condition: bool) {
    if !condition {
        println!("Ok!");
    }
}
```

Python で同等の処理は `if not` という形で書けます. 
つまり `not` というキーワードが `!` に比べて冗長なため, 見落とす可能性が低いです.

```python
def check_bool(condition):
    '''引数が false なら `Ok!` と出力する. true ならば何もしない.'''

    if not condition:
        print("Ok!")
```

このあたりを何とかできないか, というのが本記事の主題です.


# エディタの表示設定

この手の問題はエディタ側でなんとかするのが王道でしょう. 
演算子が一文字であり, しかもかなり線が細く見にくい文字だというのが問題の根源であり, 
おそらく `!` が読みやすいフォントを採用するのが最も適切な解決策だと思いますが,
好みのフォントの `!` が読みやすいかはわかりません.
フォント自作まで行くと完全にぬかるみにはまってしまいます.

より簡単な解決策としてはシンタックスハイライトをカスタマイズするというものがあります.
例えば VS Code で論理否定演算子 `!` を太字かつ赤字にするならば, `settings.json` の
`editor.tokenColorCustomizations` > `textMateRules` に次の設定を追加してください.

```json
{
    "scope": "keyword.operator.logical.rust",
    "settings": {
        "foreground": "#ff0000",
        "fontStyle": "bold"
    }
}
```

なお VS Code におけるシンタックスハイライトのカスタマイズについては次の記事がわかりやすいです.

* [Visual Studio Codeの設定「虎の巻」：構文ハイライト／配色テーマ自作編：特集：Visual Studio Codeを使いこなそう（2/4 ページ） - ＠IT](https://www.atmarkit.co.jp/ait/articles/1710/20/news023_2.html)


# 括弧をつける

常に `!(...)` という形で書くようにすると, かなり可読性が向上します. 
`!` の後にスペースを入れてもよいですが, それよりは括弧の方が良いと思います.

```rust
/// 引数 (bool) が false なら `Ok!` と出力する. true ならば何もしない.
fn check_false(condition: bool) {
    if !(condition) {
        println!("Ok!");
    }
}
```

不要な括弧なのでコンパイラに警告されるのではと思いましたが, 
少なくとも最新 stable ではこれは警告されず rustfmt でも修正されないようです.
ただ個人的にはあまり好みではありません.


# `Not` トレイト

そもそも `!` 演算子が何かというと `std::ops::Not` トレイトの `Not::not` 関数の糖衣構文です.
ですから `!` を使いたくないのであれば, 単純に `not` メソッドに置き換えることは常に可能です.

```rust
use std::ops::Not;

/// 引数 (bool) が false なら `Ok!` と出力する. true ならば何もしない.
fn check_false(condition: bool) {
    if condition.not() {
        println!("Ok!");
    }
}
```

しかし (最初に `Not` トレイトをインポートする手間は気にしないにしても) `if not` ほどの読みやすさはありません.
`if` と `not` が離れているのが問題ですが, それならばいっそ

```rust
use std::ops::Not;

/// 引数 (bool) が false なら `Ok!` と出力する. true ならば何もしない.
fn check_false(condition: bool) {
    if Not::not(condition) {
        println!("Ok!");
    }
}
```

とするのはどうでしょう. かなり冗長ですが, 否定演算子を決して見落としてはならない文脈ならば案外ありかもしれません.
