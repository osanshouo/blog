+++
title = "Windows TerminalでWSL2がルートディレクトリで開始される"
date = 2021-12-22
[extra]
toc = false
[taxonomies]
tags = ["Linux", "Windows", ]
+++

Windows Terminal + WSL2 (Debian) 環境がメインなのですが, 
気づいたらなぜかホームディレクトリ (`/home/user/`) ではなくルートディレクトリ (`/`) で起動するようになっていました. 
Windows Terminal の設定を見直しても確かにホームディレクトリが設定されており, すこし頭を捻りましたが, 
パスの区切り文字が `/` では認識しないように仕様変更されていたのが原因だったようです.

「設定 > Debian > 全般 > 開始ディレクトリ」の設定が

```
//wsl$/Debian/home/user
```

では正しく認識されません. `/` の代わりに `\` を用いた

```
\\wsl$\Debian\home\user
```

だと正しくホームディレクトリで開始できます.


# 参考文献

* [Windows Terminal General Profile Settings | Microsoft Docs](https://docs.microsoft.com/en-us/windows/terminal/customize-settings/profile-general)
