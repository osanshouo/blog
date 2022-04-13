+++
title = "Windows Terminalの背景透過について"
date = 2022-04-13
[taxonomies]
tags = [ "Windows", ]
+++

Microsoft が従来のコマンドプロンプトのコンソール `conhost.exe` に代わるターミナルアプリとして開発している 
[Windows Terminal](https://github.com/microsoft/terminal) は, 
開発初期から「背景ぼかし (アクリル)」機能には対応していたものの長らく「背景透過」に対応していませんでした.

* [Feature Request: Standard Opacity options like the traditional console. · Issue #603 · microsoft/terminal · GitHub](https://github.com/microsoft/terminal/issues/603)

これは必要な API を Windows 10 が提供していなかったためであり, 
Windows 11 でそれが実装された後の [PR #11180](https://github.com/microsoft/terminal/pull/11180) で解決し, 
プレビュー版では [v1.12.2922.0](https://github.com/microsoft/terminal/releases/tag/v1.12.2922.0), 
安定版では [v1.12.10732.0](https://github.com/microsoft/terminal/releases/tag/v1.12.10732.0) で実装されました.
つまり現在 Microsoft Store からダウンロードできる最新版ではめでたく背景透過が設定できるようになっています.


# 背景透過の設定

上述のように現時点では背景透過は Windows 11 でのみ対応しています. 公式ドキュメントが必要な情報を提供してくれています.

[Windows ターミナルの外観プロファイル設定 | Microsoft Docs](https://docs.microsoft.com/ja-jp/windows/terminal/customize-settings/profile-appearance#opacity)

アクリル効果はおしゃれではあるものの実用性はあまりありません.
背景透過には背後のウィンドウの文字が読めるという利点があり, この設定をする場合はそれが目当てになるでしょう.
