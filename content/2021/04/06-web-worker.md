+++
title = "WebWorkerで並列計算"
date = 2021-04-06
[extra]
toc = true
[taxonomies]
tags = ["Web", "数値解析"]
+++

JavaScript では Web Workers API を通じて並列処理をサポートしています.
本記事ではこれを用いて並列計算を試してみます.


# 環境

* Deno 1.18.3 on Debian 10.9 on WSL2 (Win10 v20H2)
* Intel Core i7-8550U

Node.js をインストールしようと思っていたのですが, 
4月20日に次期 LTS の version 16 がリリース予定というタイミングだったので, 
Node.js はそれまで延期して deno を試すことにしました.


# シリアル計算

本記事で取り上げるお題は[以前](https://qiita.com/osanshouo/items/e5be8003f189dfe246f9)も使った Leibniz 級数
$$\frac{ \pi }{ 4 } = \sum_{n = 0}^\infty \frac{ ( - 1 )^n }{ 2 n + 1 }$$
です. 交代級数を愚直に評価することは基本的にするべきではないんですが, いまは円周率の評価がしたい訳ではないのでよいでしょう.

```javascript
const N = 1e9;

var sum = 0.0;
var signum = 1;
var denom = 1.0;

for (var i = 0; i<N; i++) {
    sum += signum / denom;
    signum *= -1;
    denom += 2.0;
}
console.log(4.0*sum);
```

上記環境ではこのコードの処理に 1.643 秒かかりました.


# 並列計算

メインスレッドの処理はこんな感じでしょう. 見ての通り, Web Worker を取得し, 級数の下限と上限を渡し, 
計算結果が返ってきたら `result` 変数に足し合わせていきます.

```javascript
const N = 1e9;
const THREAD = 4;
var result = 0;

for (var c=0; c<THREAD; c++) {
    const worker = new Worker(
	new URL("./worker.js", import.meta.url).href,
	{type: "module"}
    );

    var start = (N / THREAD) * c;
    var end = (N / THREAD) * (c+1);
    worker.postMessage([start, end]);
    
    worker.onmessage = function(e) {
        result += e.data;
        console.log(result*4.);
        worker.terminate();
    }
}
```

Web Worker には `classic` と `module` というふたつのタイプがあるようですが,
deno では現在のところ `module` しかサポートしていません.

すべての worker の処理が終了した時点で結果を表示すればよいのですが,
うまくそれを検出する方法に困って結果が返ってくる度に `result` を表示するようにしました.

`worker.js` はこうなります. これは級数を分割しただけなのでとても簡単です.

```javascript
onmessage = function(e) {
    let start = e.data[0];
    let end = e.data[1];

    var sum = 0.0;
    var signum = 1;
    var denom = 2.*start + 1.;

    for (var i = start; i<end; i++) {
        sum += signum / denom;
        signum *= -1;
        denom += 2.0;
    }

    postMessage(sum);
}
```

手元の環境ではこの処理に 0.642 秒という結果になりました.
約 2.56 倍の高速化ができました.


# 参考文献

* [Manual | Deno](https://deno.land/manual/runtime/workers)
* [Web Worker の使用 - Web API | MDN](https://developer.mozilla.org/ja/docs/Web/API/Web_Workers_API/Using_web_workers)
