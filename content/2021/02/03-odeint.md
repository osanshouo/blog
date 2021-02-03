+++
title = "Euler法, Heun法, Runge-Kutta法の比較"
date = 2021-02-03
draft = true
[extra]
toc = true
[taxonomies]
tags = ["Rust", "Python", "数学", "数値解析", ]
+++

Euler 法, Heun 法, 古典的 Runge-Kutta 法について誤差の収束性のプロットを作成したので, コードを残しておきます.

# コメント

例によって主な計算は Rust で実装し, それを PyO3 により Python から呼び出して可視化しています.
Rust 側は汎用のライブラリとして Python 側から ODE をコールバック関数として渡そうとしたのですが,
PyO3 が (現時点ではまだ) クロージャに陽に対応しておらず ([doc](https://pyo3.rs/master/function.html#closures)), 
`PyAny` を触るのはさすがに時間がかかりすぎるので諦めました.
なので解くべき微分方程式は `src/lib.rs` にハードコードしてあります.

そしていつのまにか PyO3 が version 0.13 になっていました.

# Rust 

## Cargo.toml

```toml
[lib]
name = "odeint"
crate-type = ["cdylib"]

[dependencies]
pyo3 = { version = "0.13", features = ["extension-module"] }
```

## src/solver.rs

```rust
pub fn euler<F>(f: &F, t: f64, x: f64, h: f64) -> f64
where 
    F: Fn(f64, f64) -> f64, 
{
    x + h*f(t, x)
}

pub fn heun<F>(f: &F, t: f64, x: f64, h: f64) -> f64
where 
    F: Fn(f64, f64) -> f64, 
{
    let k = f(t, x);

    x + h*( k + f(t+h, x+h*k))*0.5
}

pub fn rk4<F>(f: &F, t: f64, x: f64, h: f64) -> f64
where 
    F: Fn(f64, f64) -> f64, 
{
    let k1 = f(t, x);
    let k2 = f(t + 0.5*h, x + 0.5*h*k1);
    let k3 = f(t + 0.5*h, x + 0.5*h*k2);
    let k4 = f(t + h, x + h*k3);

    x + h*(k1 + 2.*(k2 + k3) + k4)/6.
}
```

## src/lib.rs

```rust
mod solver;

use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

fn f(_: f64, x: f64) -> f64 { x.cos() }

#[pyfunction]
fn solve(method: String, n: usize) -> PyResult<f64> {
    let method = match method.as_str() {
        "euler" => solver::euler,
        "heun" => solver::heun,
        "rk4" => solver::rk4,
        _ => unimplemented!(),
    };

    let h = 1. / n as f64;
    let mut t = 0.;
    let mut x = 0.;

    for _ in 0..n {
        x = method(&f, t, x, h);
        t += h;
    }

    Ok(x)
}

#[pymodule]
fn odeint(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!( solve ))?;

    Ok(())
}
```

# Python

## plot.py

```python
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Source Han Serif JP"
plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["font.size"] = 16

import odeint

Ns = np.array([ 3, 10, 30, 100, 301, 1_000, ], dtype=int)

exact = np.arcsin(np.tanh(1.))

def error(method):
    err = []
    for N in Ns:
        x = odeint.solve(method, N)
        err.append(x)
    return np.fabs(np.array(err) / exact - 1.)


fig = plt.figure()
plt.subplots_adjust(left=0.15, right=0.9, bottom=0.14, top=0.92)
ax = fig.add_subplot(111)

ax.plot( 1./Ns, error("euler"), "^-", label="Euler")
ax.plot( 1./Ns, error("heun"), "d-", label="Heun")
ax.plot( 1./Ns, error("rk4"), "o-", label="RK4")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_ylim([1e-13, 1e-1])
ax.grid()
ax.grid(which="minor", alpha=0.3)
ax.legend()

ax.set_xlabel(r"刻み幅",  fontsize=18)
ax.set_ylabel(r"相対誤差", fontsize=18)

plt.savefig("odesolver-comparison.svg")
plt.show()
plt.close()
```
