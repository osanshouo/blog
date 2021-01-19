+++
title = "[Rust] 数値積分アルゴリズムあれこれ"
date = 2021-01-19
[extra]
toc = true
[taxonomies]
tags = ["数値解析", "Rust", ]
+++

数値積分法としては台形公式および Simpson の公式が有名ですが, 他にも優れたアルゴリズムが存在し,
例えば Numerical Recipes では台形公式と Richardson 補外を組み合わせる __Romberg 積分__ が推奨されています.
そこで本記事ではこれらの数値積分法を Rust で実装してみます.


# 問題設定

区間 $[ a, b ]$ 上で定義された $C^\infty$-級関数 $f: [ a, b ] \to \mathbb{R}$ の積分
$$I = \int_a^b f \left( x \right) dx$$
を数値的に求めることを考えます. 本記事で扱うアルゴリズムは, 
いずれも区間 $[ a, b ]$ を $N$ 個の小区間に分割するものです. 
そこで, 以下では $h = ( b - a ) / N$ とし, $i = 0, 1, \cdots, N-1$ 番目の小区間を
$$[ x_i, x_{i+1} ] \ \ ( x_i = a + i h)$$
と書きます. $a = x_0$, $b = x_N$ であることに注意してください.


# 台形公式

台形公式は, 小区間 $[ x_i, x_{i+1} ]$ において関数 $f$ を一次関数により近似する
$$\int_a^b f \left( x \right) dx \approx h \left[ \frac{ 1 }{ 2 } f \left( x_0 \right) + f \left( x_1 \right) + \cdots + 2 f \left( x_{N-1} \right) + \frac{ 1 }{ 2 } f \left( x_N \right) \right]$$
というものです. 誤差は $O ( h^2 )$ すなわち $O ( N^{-2} )$ です.

Rust での実装はこんな感じになると思います. イテレータで良い感じに書けます.

```rust
pub fn trapezoidal<F>(f: &F, a: f64, b: f64, n: usize) -> f64 
where
    F: Fn(f64) -> f64,
{
    let h = (b - a)/(n as f64);

    let (_, sum) = (1..n).fold((a + h, 0.), |(x, sum), _| {
        (x + h, sum + f(x))
    });

    ( sum + (f(a) + f(b))*0.5 ) * h
}
```


# Simpson の公式

台形公式は問題の関数を各小区間で一次関数と近似するものでしたが, Simpson の公式は二次関数により近似します.
そのため, 区間数 $N$ は偶数であるものとします.

被積分関数の評価点は台形公式と同じで, 係数がすこし変わります. 
誤差は $O ( h^4 )$ すなわち $O ( N^{-4} )$ です.

```rust
pub fn simpson<F>(f: &F, a: f64, b: f64, n: usize) -> f64 
where
    F: Fn(f64) -> f64,
{
    let h = (b - a)/(n as f64);

    let (_, _, sum) = (1..n).fold((a + h, true, 0.), |(x, odd, sum), _| {
        let c = if odd { 4. } else { 2. };
        (x + h, !odd, sum + c*f(x))
    });

    ( sum + f(a) + f(b) ) * h / 3.
}
```

なお一般に被積分関数を $m+1$ 点を通る $m$ 次関数により近似するとき, Newton-Cotes のアルゴリズムと呼び, 積分を次の和
$$\frac{ h }{ s_m } \sum_{i = 0}^N \sigma_{m, i} f \left( x_i \right)$$
として求めることができます. ただ, 次数を上げ過ぎると係数 $\sigma_{m, i}$ が負の値を取るようになり,
その場合各項の間で有効桁数が相殺し精度が落ちてしまうという問題が発生します.
なのでむやみに次数を上げることは推奨できません.


# Romberg 積分

台形公式により得られた積分値を小区間の幅 $h$ の関数とみるとき,
$h \to 0$ という外挿を行うことによってより精度の良い積分値を得ることができる, というアイデアに基づく積分法が Romberg 積分です.
そのために, 複数の $h$ (あるいは複数の分割数 $N$) について台形公式による積分値を計算し, それを Richardson 補外します.

```rust
pub fn romberg<F>(f: &F, a: f64, b: f64, ns: &[usize]) -> f64 
where
    F: Fn(f64) -> f64
{
    let hs: Vec<f64> = ns.iter()
        .map(|n| (b - a)/(*n as f64))
        .collect();
    
    let t: Vec<f64> = ns.iter()
        .map(|n| trapezoidal(f, a, b, *n))
        .collect();

    romberg_neville(&hs, t)
}

fn romberg_neville(hs: &[f64], mut ts: Vec<f64>) -> f64 {
    let size = hs.len();

    for k in 1..size {
        for i in (k..size).rev() {
            ts[i] += (ts[i] - ts[i-1])/((hs[i-k] / hs[i]).powi(2) - 1.);
        }
    }

    ts[size - 1]
}
```

補外には Neville のアルゴリズムを使用します. 誤差は $O ( {h_0}^2 \cdots {h_m}^2 )$ です.

この実装では各々の台形公式の適用は独立な処理なので, この部分は容易に並列化できるでしょう.
ただ, 代わりに同一点での関数値 $f ( x_i )$ を複数回評価しています.
$f$ の評価に計算時間を要する場合には, これを避けて異なる分割数での台形公式を同時に計算した方がよいかもしれません.
Neville のアルゴリズムは下手に並列化してもオーバーヘッドのため遅くなるのではないかと思います (未検証です) し,
現代のコンピュータならこの部分に要する計算時間は無視できるでしょう.

# 参考文献
* J. Stoer & R. Bulirsch, _Introduction to Numerical Analysis_, Springer, 2002. doi:[10.1007/978-0-387-21738-3](https://dx.doi.org/10.1007%2F978-0-387-21738-3). ISBN 978-0-387-21738-3
