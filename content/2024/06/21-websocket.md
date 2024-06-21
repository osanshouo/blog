+++
title = "[Rust] WebSocketを試してみた"
date = 2024-06-21
[extra]
toc = true
[taxonomies]
tags = [ "Rust", "Web", ]
+++

WebSocket はチャットやリアルタイム対戦ゲームなど, サーバーとクライアントがリアルタイムで双方向通信を行うための通信プロトコルです.
HTTP ポーリングとは違い接続チャンネルが開かれたままになるため, サーバー側が任意のタイミングでクライアントにメッセージを送ることができます.


# サーバーサイド

Rust 向けのクレートとしては [websocket](https://crates.io/crates/websocket) や [ws](https://crates.io/crates/ws) が以前からありましたが,
現在は [tungstenite](https://crates.io/crates/tungstenite) というものが人気を集めているようなので, これを試してみます.

```toml
[dependencies]
tungstenite = "0.23.0"
```

`src/main.rs` はこんな感じです. 接続成功時に `Hello from Rust!` というメッセージをクライアントに送る他,
クライアントからテキストメッセージが送られてきたら, 
それを標準出力に出力した上で, 同じメッセージをクライアントにオウム返しします (echo).

```rust
use std::net::TcpListener;
use std::thread;
use tungstenite::{accept, protocol::Message};

fn main () {
    let server = TcpListener::bind("127.0.0.1:9001").unwrap();
    for stream in server.incoming() {
        thread::spawn (move || {
            let mut websocket = accept(stream.unwrap()).unwrap();
            websocket.send(Message::Text("Hello from Rust!".to_string())).unwrap();

            loop {
                let msg = websocket.read().unwrap();

                if let Message::Text(ref text) = msg {
                    println!("{}", text);
                    websocket.send(msg).unwrap();
                }
            }
        });
    }
}
```

# クライアントサイド

参考文献に挙げたものが大変参考になりました.
二番目の Google Chrome 用 WebExtension はシンプルな実装なのですが, jQuery を用いているので, バニラ JS で書き直しました.

## HTML

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>WebSocket Chat</title>
</head>
<body>
<div>
    <fieldset>
        <legend>Server Setting</legend>
        <div>
            <label>URL:</label>
            <input type="text" id="serverUrl" value="ws://"/>
            <button id="connectButton">Open</button>
            <button id="disconnectButton">Close</button>
        </div>
        <div>
            Status:
            <span id="connectionStatus">CLOSED</span>
        </div>
    </fieldset>

    <fieldset id="messageField">
        <legend>Message</legend>
        <div>
            <textarea id="messageText"></textarea>
        </div>
        <div>
            <button id="sendButton">Send</button>
        </div>
    </fieldset>

    <div id="chatHistory">
        <div>Chat Log <button id="clearButton">Clear</button></div>
        <div id="chatLog"></div>
    </div>
</div>
<script type="text/javascript" src="ws.js"></script>
</body>
</html>
```

## JavaScript

```javascript
let chatLog = document.getElementById("chatLog");
let connectionStatus = document.getElementById("connectionStatus");

let ws;

// メッセージをチャット欄に表示する処理
let addMessage = function (text) {
    let message = document.createElement('div');
    message.textContent = text;
    chatLog.prepend(message);
};


// `Open` ボタンを押すと WebSocket 通信を開始する.
let connectButton = document.getElementById("connectButton");
connectButton.addEventListener("click", () => {
    let serverUrl = document.getElementById("serverUrl");
    let url = serverUrl.value;
    console.log("WebSocket通信を開始します:", url);

    ws = new WebSocket(url);

    ws.onopen = function () {
        console.log("WebSocket通信に成功しました.");
        connectionStatus.textContent = "OPENED";
    };

    ws.onclose = function () {
        console.log('WebSocket通信を終了しました:', serverUrl.value);
        connectionStatus.textContent = "CLOSED";
        ws = null;
    };

    ws.onerror = function (error) {
        console.log(error);
    };

    ws.onmessage = function (e) {
        let data = e.data;
        console.log("受信メッセージ:", data);
        addMessage(data);
    };
});


// メッセージ送信ボタンを押した時の処理
let sendButton = document.getElementById("sendButton");
sendButton.addEventListener("click", () => {
    if (ws) {
        let messageText = document.getElementById("messageText");
        let text = messageText.value;
        console.log("送信メッセージ:", text);
        ws.send(text);
    }
});


// 接続終了ボタンを推した時の処理
let disconnectButton = document.getElementById("disconnectButton");
disconnectButton.addEventListener("click", () => {
    if (ws) {
        console.log("WebSocket通信を終了します.");
        ws.close();
    } else {
        console.log("WebSocket通信は開始されていません.");
    }
});


// クリアボタンを押した時の処理
let clearButton = document.getElementById("clearButton");
clearButton.addEventListener("click", () => {
    chatLog.innerHTML = "";
});
```





# 参考文献
* [WebSocketでチャットアプリを作ろう①　~WebSocketサーバの立て方~ – モナカプレス](https://press.monaca.io/atsushi/435)
* [GitHub - hakobera/Simple-WebSocket-Client](https://github.com/hakobera/Simple-WebSocket-Client)
* [tungstenite - crates.io: Rust Package Registry](https://crates.io/crates/tungstenite)
