+++
title = "WSLでWindows側のフォントを使う"
date = 2022-05-30
[taxonomies]
tags = [ "Windows", "Linux", ]
+++

WSL 側で Windows 側のフォントを使うための設定メモ. Win11, WSL2, Debian で動作確認.


# 手順

フォントの設定ツールをインストールする.

```bash
sudo apt install fontconfig
```

設定ファイルを作成.

```bash
sudo touch /etc/fonts/local.conf
```

作成した設定ファイルに以下の内容を書き込む.

```xml
<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>
    <dir>/mnt/c/Windows/Fonts</dir>
</fontconfig>
```

フォントのキャッシュを更新.

```bash
sudo fc-cache -fv
```

フォントの一覧に Windows 側のフォントが含まれるか確認.

```bash
sudo fc-list | less
```


# 参考文献

* [ASCII.jp：WindowsでLinux GUIアプリを動かす「WSLg」のWindows 11での状況を見る](https://ascii.jp/elem/000/004/073/4073680/)
* [【備忘録】 WSL から游書体を使う方法 - Sokratesさんの備忘録ないし雑記帳](https://sokrates7chaos.hatenablog.com/entry/2021/06/25/142323)
* [fonts-conf](https://www.freedesktop.org/software/fontconfig/fontconfig-user.html)
* [[WSL] WSLでWindowsのフォントを使う時の注意点 ~ Windows10に更新した（メモ書き）](https://upgrade-windows10.blogspot.com/2020/01/wslwindows.html)
