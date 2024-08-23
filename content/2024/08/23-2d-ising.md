+++
title = "2次元 Ising 模型"
date = 2024-08-23
[taxonomies]
tags = [ "物理学", "統計力学", "Rust", "Python", ]
+++

2次元 Ising 模型の分配関数などを定義に従って計算する落書きコード.
遅すぎて役に立たないですが...

# Python

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc("text", usetex=True)
plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 16

def state(n, N):
    '''
    入力: n: 状態の名前 (0,1,...,N-1), N: 格子サイズ 
    出力: N*N 行列
    '''
    s = np.zeros((N,N))
    for l in range(N*N):
        if (n >> l)&1 == 0:
            s[l//N, l%N] = 1
        else:
            s[l//N, l%N] = -1
    return s

def hamiltonian(s, N):
    e = 0.
    for i in range(N):
        for j in range(N):
            e += s[i,j]*( s[i, (j+1)%N] + s[(i+1)%N, j] )
    return e
    

Tmin, Tmax, div = 0.1, 4, 128
T = np.linspace(Tmin, Tmax, div)

def ising(N):
    Z = 0. # 分配関数
    S = 0. # 磁化
    E = 0. # エネルギー
    C = 0. # エネルギー分散 (比熱)
    for n in range(2**(N*N)):
        s = state(n,N)
        e = hamiltonian(s,N)
        p = np.exp(-e/T)
        Z += p
        S += np.sum(s) * p
        E += e * p
        C += e**2 * p
    return Z, S/Z, E/Z, C/Z

fig = plt.figure()
ax = fig.add_subplot(111)

for N in [2, 4]:
    Z, S, E, C = ising(N)
    ax.plot(T, (C - E**2)/(N*T)**2, label="N={}".format(N))

ax.grid()
plt.show()
```

# Rust

```rust
/// 2次元 Ising 模型の状態を表す struct.
#[derive(Debug, Clone)]
struct State {
    // /// スピン状態 \pm 1 の一覧
    // vec: Vec<f64>,
    idx: usize,
    /// 格子サイズ (vec.len = size * size)
    size: usize,
}

impl State {
    /// 与えられた size を持つ Ising 模型の状態の総数.
    fn number(size: usize) -> usize {
        2usize.pow((size*size) as u32)
    }

    /// 与えられた size を持つ, n 番目の状態を生成する.
    fn new(n: usize, size: usize) -> Self {
        // let vec = (0..(size*size))
        //     .map(|l| 
        //         if (n >> l)&1 == 0 { 1. } else { -1. }
        //     ).collect();
        // State { vec, size }
        State { idx: n, size }
    }

    /// 与えられた状態における, 格子点 (i, j) のスピンの値.
    fn spin(&self, i: usize, j: usize) -> f64 {
        //self.vec[self.size * (i%self.size) + (j%self.size)]
        let l = self.size * (i%self.size) + (j%self.size);
        if (self.idx >> l)&1 == 0 { 1. } else { -1. }
    }

    /// 与えられた状態における, 模型全体でのスピンの平均値
    fn mag(&self) -> f64 {
        //self.vec.iter().sum::<f64>() / (self.size.pow(2) as f64)
        let s = (0..self.size*self.size)
            .map(|l| (self.idx >> l)&1)
            .sum::<usize>();
        (self.size*self.size - 2*s) as f64
    }

    /// 与えられた状態における, Hamiltonian の値.
    fn energy(&self) -> f64 {
        let mut e = 0.;
        for i in 0..self.size {
            for j in 0..self.size {
                e -= self.spin(i,j)*( self.spin(i,j+1) + self.spin(i+1, j) );
            }
        }
        e
    }
}
    

fn ising(temp: &[f64], size: usize) -> (Vec<f64>, Vec<f64>, Vec<f64>) {
    let mut z = vec![ 0.; temp.len() ];
    let mut mag = vec![ 0.; temp.len() ];
    let mut ene = vec![ 0.; temp.len() ];
    let mut cov = vec![ 0.; temp.len() ];

    for n in 0..State::number(size) {
        let state = State::new(n as usize, size as usize);
        let e = state.energy();
        for idx in 0..temp.len() {
            let prob = (- e / temp[idx]).exp();
            z[idx] += prob;
            mag[idx] += state.mag() * prob;
            ene[idx] += e * prob;
            cov[idx] += e*e * prob;
        }
    }
    for idx in 0..temp.len() {
        mag[idx] /= z[idx];
        ene[idx] /= z[idx];
        cov[idx] /= z[idx];
    }

    (mag, ene, cov)
}

fn main() {
    let temp: Vec<f64> = (1..8).map(|i| i as f64 * 0.5).collect();

    let size = 4;
    let (mag, ene, cov) = ising(&temp, size);
    println!("{:?}\n{:?}\n{:?}", &mag, &ene, &cov);
    for idx in 0..temp.len() {
        print!("{} ", ( cov[idx] - ene[idx].powi(2) )/(size as f64 * temp[idx]).powi(2) )
    }
}
```
