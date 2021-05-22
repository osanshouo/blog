+++
title = "Rust for Windowsでウィンドウを表示"
date = 2021-05-22
[extra]
toc = true
[taxonomies]
tags = ["Rust", "Windows", ]
+++

Rust for Windows は進化が非常に速い上に情報源がほとんどないのが面倒なところです.
本記事は Win10 v20H2, Rust 1.52.1, `windows=0.10.0` に基づいてウィンドウを描画してみます.
つまり, この記事は benki さんの [Rust で Windows プログラミング - CreateWindow編 - Qiita](https://qiita.com/benki/items/c01f7da1e1a71cc91d11) を 
Rust for Windows 向けにアップデートしたものです.


# 解説

## 文字列型について

Win32 には A 版と W 版があります. A 版は ANSI, W 版は Unicode の意味です. 問答無用で W 版を使えばよいでしょう.

ところが Windows では Unicode とはヌル終端つき UTF-16 のことです. しかし Rust の文字列は UTF-8 です.
std の `OsStr` を使ってもよいですが, ヌル終端の扱いが面倒なので, 参考文献にならって自前で `Vec<u16>` への変換を用意しておくと便利です.

```rust
fn wide_null(s: &str) -> Vec<u16> {
    s.encode_utf16().chain(Some(0)).collect()
}
```


## ウィンドウクラス

ひとつのウィンドウに対してひとつの [WNDCLASSW](https://docs.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-wndclassw) 型のインスタンスが必要です. 
以前は初期化が面倒だったようですが, Rust for Windows では `Default` が実装されたので, これを使えば簡単です.
ただし, 作成時に `lpfnWndProc`, `hInstance`, `lpszClassName` という三個のフィールドを次のように自分で設定しなければなりません.

```rust
let mut class_name = wide_null("main window class");

let mut wc = WNDCLASSW::default();
wc.lpfnWndProc = Some(window_proc);
wc.hInstance = HINSTANCE(0);
wc.lpszClassName = PWSTR(class_name.as_mut_ptr());
```

最初の `lpfnWndProc` については後で議論するのでここでは説明を飛ばします.
二番目の `hInstance` は本来は正しく設定すべきですが, とりあえずヌルを入れておけば動くのでこれでよいでしょう 
(そもそも `Default` で初期化するとヌルが入るのでこの行は不要なのですが, 公式がきちんと設定せよと言っているのでそれを忘れないためにもこう書いておけばよいと思います).
三番目の `lpszClassName` は作成した `WNDCLASSW` インスタンスの内部的な識別名で, ブッキングしなさそうな文字列なら何でもよいです.

`WNDCLASSW` インスタンスの初期化が完了したら, このインスタンスを OS に登録して管理してもらいます.

```rust
let atom = unsafe { RegisterClassW(&wc) };
assert_ne!(atom, 0);
```

返り値 `atom` が 0 ならば処理に失敗したことを意味します. 0 でなければこれは OS 側のこのインスタンスの識別名です.


* [RegisterClassW function (winuser.h) - Win32 apps | Microsoft Docs](https://docs.microsoft.com/ja-jp/windows/win32/api/winuser/nf-winuser-registerclassw)


## ウィンドウの表示

ウィンドウを表示するには, 作成した `WNDCLASSW` インスタンスを画面に描画せよ, と OS に指示を出す必要があります.
これは `CreateWindowExW` 関数を呼び出し, 得られた `HWND` インスタンスを `ShowWindow` 関数に渡すことによって可能です. 

`CreateWindowExW` 関数の第三引数にはタイトルバーに表示されるアプリ名を設定します.

```rust
let hwnd = unsafe {
    CreateWindowExW(
        WINDOW_EX_STYLE(0),
        PWSTR(class_name.as_mut_ptr()),
        PWSTR(app_title.as_mut_ptr()),
        WS_OVERLAPPEDWINDOW,
        CW_USEDEFAULT,
        CW_USEDEFAULT,
        CW_USEDEFAULT,
        CW_USEDEFAULT,
        HWND(0),
        HMENU(0),
        HINSTANCE(0),
        core::ptr::null_mut(),
    )
};
assert!(!hwnd.is_null());

unsafe { ShowWindow(hwnd, SHOW_WINDOW_CMD(5)) };
```

* [CreateWindowExW function (winuser.h) - Win32 apps | Microsoft Docs](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createwindowexw)


## メッセージループ

GUI アプリケーションは自身に対して発生したすべてのイベント (クリック, キーボード入力, OS がスリープ状態になったことの告知, など) に対して適切に応答する必要があります.
Win32 ではこの処理はメッセージループと呼ばれます.

すべてのイベントは内部的にキューとして保持されているので, `GetMessageW` 関数を呼び出して順にメッセージを取り出し, `msg` という変数に格納します.
そしてそのメッセージを `TranslateMessage`, `DispatchMessageW` というふたつの関数を渡します (これは定型文です).

```rust
let mut msg = MSG::default();
while BOOL(0) != unsafe { GetMessageW(&mut msg, HWND(0), 0, 0) } {
    unsafe {
        TranslateMessage(&msg); 
        DispatchMessageW(&msg);
    }
}
```

アプリケーションが終了することを表す `WM_QUIT` メッセージが現れたときのみ `GetMessageW` 関数は `Bool(0)` を返すので,
このメッセージを受け取ったらメッセージループを抜けてアプリケーションを終了するようにします.


## ウィンドウプロシージャ

`DispatchMessageW` は最初の方で登場した `window_proc` 関数を内部で呼び出します. 
この関数には, 各メッセージに対してアプリケーションが何をすればよいのかを実装します.

```rust
unsafe extern "system" fn window_proc(
    hwnd: HWND, msg: u32, w_param: WPARAM, l_param: LPARAM,
) -> LRESULT {

    match msg {
        WM_DESTROY => PostQuitMessage(0),
        _ => return DefWindowProcW(hwnd, msg, w_param, l_param),
    };

    LRESULT(0)
}
```

`WM_DESTROY` メッセージはウィンドウを閉じる処理が走ることを表します. 普通はこのとき 
`PostQuitMessage` 関数を呼ぶことで自分自身に `WM_QUIT` メッセージを発行し, アプリケーションを終了します.
それ以外のメッセージはデフォルトの処理 `DefWindowProcW` を呼びます.
なおこの部分に重い処理を実装するとアプリがフリーズしたように感じられるので, それは避けて別スレッドで処理したりするべきなのだそうです.

以上でウィンドウを描画し, 任意に終了することができるようになりました.


# コード全体

## `bindings/build.rs`

```rust
fn main() {
    windows::build!(
        Windows::Win32::UI::WindowsAndMessaging::{
            WNDCLASSW, WNDPROC, WNDCLASS_STYLES,
            WS_OVERLAPPEDWINDOW, CW_USEDEFAULT, WINDOW_EX_STYLE,
            SHOW_WINDOW_CMD, RegisterClassW, CreateWindowExW,
            ShowWindow, DefWindowProcW, PostQuitMessage, 
            GetMessageW, MSG, TranslateMessage, DispatchMessageW, WM_DESTROY, WM_SIZE, 
        },
        Windows::Win32::UI::MenusAndResources::{HICON, HCURSOR, HMENU},
        Windows::Win32::Graphics::Gdi::HBRUSH,
        Windows::Win32::System::SystemServices::{
            PWSTR, HINSTANCE, LRESULT, GetModuleHandleW,
        },
    )
}
```

## `src/main.rs`

```rust
#![windows_subsystem = "windows"]

use bindings::Windows::Win32::{
    UI::WindowsAndMessaging::*,
    UI::MenusAndResources::*,
    System::SystemServices::*,
};


fn wide_null(s: &str) -> Vec<u16> {
    s.encode_utf16().chain(Some(0)).collect()
}

fn main() {
    let mut app_title = wide_null("Hello from Rust!");
    let mut class_name = wide_null("main_window_class");

    let mut wc = WNDCLASSW::default();
    wc.lpfnWndProc = Some(window_proc);
    wc.hInstance = HINSTANCE(0);
    wc.lpszClassName = PWSTR(class_name.as_mut_ptr());

    let atom = unsafe { RegisterClassW(&wc) };
    assert_ne!(atom, 0);

    let hwnd = unsafe {
        CreateWindowExW(
            WINDOW_EX_STYLE(0),
            PWSTR(class_name.as_mut_ptr()),
            PWSTR(app_title.as_mut_ptr()),
            WS_OVERLAPPEDWINDOW,
            CW_USEDEFAULT,
            CW_USEDEFAULT,
            CW_USEDEFAULT,
            CW_USEDEFAULT,
            HWND(0),
            HMENU(0),
            HINSTANCE(0),
            core::ptr::null_mut(),
        )
    };
    assert!(!hwnd.is_null());
    
    unsafe { ShowWindow(hwnd, SHOW_WINDOW_CMD(5)) };

    let mut msg = MSG::default();
    while BOOL(0) != unsafe { GetMessageW(&mut msg, HWND(0), 0, 0) } {
        unsafe {
            TranslateMessage(&msg); 
            DispatchMessageW(&msg);
        }
    }
}


unsafe extern "system" fn window_proc(
    hwnd: HWND, msg: u32, w_param: WPARAM, l_param: LPARAM,
) -> LRESULT {

    match msg {
        WM_DESTROY => PostQuitMessage(0),
        _ => return DefWindowProcW(hwnd, msg, w_param, l_param),
    };

    LRESULT(0)
}
```

# 参考文献 
* [Creating a Window - Win32 apps | Microsoft Docs](https://docs.microsoft.com/en-us/windows/win32/learnwin32/creating-a-window)
* [Win32 - Triangle From Scratch](https://rust-tutorials.github.io/triangle-from-scratch/opening_a_window/win32.html)
* [Rust で Windows プログラミング - CreateWindow編 - Qiita](https://qiita.com/benki/items/c01f7da1e1a71cc91d11)
