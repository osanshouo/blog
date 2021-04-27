+++
title = "[Rust] Stockham型FFT"
date = 2021-04-27
[extra]
toc = true
[taxonomies]
tags = ["数値解析", "Rust"]
+++

[高速 Fourier 変換](https://ja.wikipedia.org/wiki/%E9%AB%98%E9%80%9F%E3%83%95%E3%83%BC%E3%83%AA%E3%82%A8%E5%A4%89%E6%8F%9B) 
(fast Fourier transformation, FFT) のアルゴリズムは何度勉強しても忘れるんですよね...

# 離散 Fourier 変換

本記事を通じて $i$ は虚数単位を表すものとします.
$N$ 個の複素数 $a_j$ ($j = 0, 1, \cdots, N-1$) の離散 Fourier 変換 (discrete Fourier transformation, DFT) $c_k$ ($k = 0, 1, \cdots, N-1$) は
$$a_j = \frac{ 1 }{ N } \sum_k c_k \exp \left( \frac{ 2 \pi i j k }{ N } \right)$$
$$c_k = \sum_k a_j \exp \left( - \frac{ 2 \pi i j k }{ N } \right)$$
により定義されます. 以下では $\omega_N = \exp ( - 2 \pi / N )$ と略記します.
この記法では, DFT とはベクトル $a = ( a_j )$ に行列 $[ W ]_{k j} = \omega_N^{k j}$ を作用させることに過ぎません. 


# 直接計算

DFT の定義
$$c_k = \sum_{j = 0}^{N - 1} a_j ( \omega_N^k )^j$$
をそのままコードに起こすとこうなると思われます.

```rust
use num_complex::Complex;

pub fn fft(a: &[Complex<f64>]) -> Vec<Complex<f64>> {
    let n = a.len();
    let omega = crate::omega(n);
    
    (0..n).scan(Complex::new(1., 0.), |r, _k| {
        let (c, _) = a.iter()
            .fold((Complex::new(0.,0.), Complex::new(1., 0.)), |(acc, mode), a| {
                (acc + a*mode, mode * *r)
            });
        *r *= omega;
        Some(c)
    }).collect()
}
```

無論このコードは計算時間が $O ( N^2 )$ を要するため, 大きな $N$ に対してこれを用いることはできません.
手元の環境では $N = 2 \times 1024$ を超えると秒単位で待たされるので実用には厳しいと思います.


# Stockham 型 FFT

しかし DFT は極めて性質が良いため, 計算アルゴリズムを工夫すれば $O ( N \ln N )$ で計算できます.
そのようなアルゴリズムを総称して FFT と呼んでいます.
ここでは Stockham 型 FFT を取り上げます.

$N = 2^L$ である場合に議論を限定します.
$\alpha_l = 2^l$, $\beta_l = 2^{L - l - 1}$ として, $N$ 個の複素数の組 $X$ を
$$X_{l+1} [ 2 \alpha j + k ] = X_l ( \alpha j + k ) + \omega_N^{k \beta} X_l ( \alpha j + n/2 + k )$$
$$X_{l+1} [ 2 \alpha j + k + \alpha ] = X_l ( \alpha j + k ) - \omega_N^{k \beta} X_l ( \alpha j + n/2 + k )$$
(ただし $j$ は $0..\beta$ を, $k$ は $0..\alpha$ を走る) という漸化式に従って更新するとき,
$X_{L-1} ( j ) = c_j$ は $X_0 ( j ) = a_j$ の DFT を与えます.

```rust
use std::f64::consts::PI;
use num_complex::Complex;

pub fn fft_recur(a: &[Complex<f64>]) -> Vec<Complex<f64>> {
    let n = a.len();
    let lmax = n.trailing_zeros() as usize;
    assert_eq!(n, 2usize.pow(lmax as u32));

    let buf: Vec<_> = a.iter().cloned().collect();
    let tmp: Vec<_> = vec![ Complex::new(0., 0.); n ];
    
    stockham_recur(n, lmax, 0, buf, tmp)
}

fn stockham_recur(n: usize, lmax: usize, l: usize, buf: Vec<Complex<f64>>, mut tmp: Vec<Complex<f64>>) -> Vec<Complex<f64>> {
    let alpha = 1 << l;
    let beta = n >> l >> 1;

    let omega_beta = {
        let phase = - 2. * PI * (beta as f64) / (n as f64);
        Complex::from_polar(1., phase)
    };
    
    for j in 0..beta {
        let mut mode = Complex::new(1., 0.);
        
        for k in 0..alpha {
            let a = buf[alpha*j + k];
            let b = buf[alpha*j + n/2 + k] * mode;
            tmp[2*alpha*j + k] = a + b;
            tmp[2*alpha*j + k + alpha] = a - b;

            mode *= omega_beta;
        }
    }

    if l+1 == lmax {
        tmp
    } else {
        stockham_recur(n, lmax, l+1, tmp, buf)
    }
}
```

漸化式を解く際に, 不要なメモリコピーを避けるため, 
読み出し側 (`buf`) と書き込み側 (`tmp`) の役割を $l$ が進む度に入れ替えると良さそうです (手元ではこれで 25% 高速化できました).
$N = 4 \times 1024$ では定義通りだと2.6秒, Stockham 型 FFT だと0.4秒でした.

まだ最適化できるはずですが, 力尽きたのでここで一旦終わりとします.


# 参考文献 
* [高速フーリエ変換とその並列化 (I)](http://www.na.scitec.kobe-u.ac.jp/~yamamoto/lectures/parallelFFT/parallelFFT1.PDF)
* [Stockham FFT 入門](http://wwwa.pikara.ne.jp/okojisan/stockham/stockham1.html)
* [Stockham アルゴリズムについて](http://with137d.hatenablog.com/entry/20111224/1324757391)
