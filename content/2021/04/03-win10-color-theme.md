+++
title = "[Rust] Win10のカラーテーマを取得"
date = 2021-04-03
[extra]
toc = true
[taxonomies]
tags = ["Rust", "Windows", ]
+++

WinRT でアプリのカラーテーマ[^1]を取得するには `Windows::UI::ViewManagement::UISettings` クラスの 
[`GetColorValue`](https://microsoft.github.io/windows-docs-rs/doc/bindings/Windows/UI/ViewManagement/struct.UISettings.html#method.GetColorValue) 
メソッドを叩きます.


# 環境

本記事の内容は Win10 v20H2, Rust 1.51.0, windows-rs 0.7.0 で確認しました.


# import マクロ

`build.rs` で必要な WinRT API を指定し import します.

```rust
fn main() {
    windows::build!(
        Windows::UI::Color,
        Windows::UI::ViewManagement::{
            UISettings, UIColorType
        },
    )
}
```


# 色の取得

`UISettings` クラスの `GetColorValue` メソッドに欲しい色のタイプ 
([`UIColorType`](https://microsoft.github.io/windows-docs-rs/doc/bindings/Windows/UI/ViewManagement/struct.UIColorType.html)) を渡します.
戻り値は [`Color`](https://microsoft.github.io/windows-docs-rs/doc/bindings/Windows/UI/struct.Color.html) です.

## アクセントカラー

```rust
use bindings::Windows::UI::ViewManagement::{
    UISettings, UIColorType,
};

fn main() -> windows::Result<()> {
    let ui_settings = UISettings::new()?;
    let color = ui_settings.GetColorValue(UIColorType::Accent)?;

    println!("{:?}", &color);

    Ok(())
}
```

## ダークモード

ダークモードに設定されているときに `true`, ライトモードのときには `false` を返す関数です.

```rust
use bindings::Windows::UI::{Color, ViewManagement::{
    UISettings, UIColorType,
}};

const DARK: Color = Color { A: 255, R: 0, G: 0, B: 0 };

fn is_dark_mode() -> windows::Result<bool> {
    let ui_settings = UISettings::new()?;
    let color = ui_settings.GetColorValue(UIColorType::Background)?;
    
    Ok(color == DARK)
}
```

# 参考文献
* [UISettings Class](https://docs.microsoft.com/en-us/uwp/api/windows.ui.viewmanagement.uisettings?view=winrt-19041)


[^1]: 本記事のコードは「設定」でいう「Windows モード」ではなく「アプリ モード」を取得するものです.
